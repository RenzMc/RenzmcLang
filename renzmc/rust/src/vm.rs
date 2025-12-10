use std::collections::HashMap;
use std::io::{self, Write};

use crate::bytecode::{BytecodeChunk, Instruction, OpCode};
use crate::value::Value;

#[derive(Debug)]
struct CallFrame {
    return_addr: usize,
    base_pointer: usize,
    locals: HashMap<String, Value>,
}

pub struct VirtualMachine {
    stack: Vec<Value>,
    globals: HashMap<String, Value>,
    call_stack: Vec<CallFrame>,
    instructions_executed: usize,
    iterator_stack: Vec<Box<dyn Iterator<Item = Value> + Send>>,
}

impl VirtualMachine {
    pub fn new() -> Self {
        VirtualMachine {
            stack: Vec::with_capacity(1024),
            globals: HashMap::new(),
            call_stack: Vec::new(),
            instructions_executed: 0,
            iterator_stack: Vec::new(),
        }
    }

    pub fn execute(&mut self, bytecode: &[u8]) -> Result<Value, String> {
        let chunk = BytecodeChunk::deserialize(bytecode)?;
        self.run(&chunk)
    }

    pub fn set_global(&mut self, name: String, value: Value) {
        self.globals.insert(name, value);
    }

    pub fn get_global(&self, name: &str) -> Option<&Value> {
        self.globals.get(name)
    }

    pub fn clear(&mut self) {
        self.stack.clear();
        self.globals.clear();
        self.call_stack.clear();
        self.instructions_executed = 0;
        self.iterator_stack.clear();
    }

    pub fn instructions_executed(&self) -> usize {
        self.instructions_executed
    }

    pub fn memory_used(&self) -> usize {
        self.stack.len() * std::mem::size_of::<Value>()
            + self.globals.len() * std::mem::size_of::<(String, Value)>()
    }

    fn run(&mut self, chunk: &BytecodeChunk) -> Result<Value, String> {
        let mut ip = 0;
        let code = &chunk.code;

        while ip < code.len() {
            let (instr, size) = Instruction::decode(code, ip);
            ip += size;
            self.instructions_executed += 1;

            match instr.opcode {
                OpCode::Nop => {}

                OpCode::LoadConst => {
                    let idx = instr.operand.unwrap_or(0) as usize;
                    if idx < chunk.constants.len() {
                        self.stack.push(chunk.constants[idx].clone());
                    } else {
                        self.stack.push(Value::None);
                    }
                }

                OpCode::LoadName => {
                    let idx = instr.operand.unwrap_or(0) as usize;
                    let name = chunk.names.get(idx).cloned().unwrap_or_default();

                    let value = if let Some(frame) = self.call_stack.last() {
                        frame
                            .locals
                            .get(&name)
                            .cloned()
                            .or_else(|| self.globals.get(&name).cloned())
                    } else {
                        self.globals.get(&name).cloned()
                    };

                    self.stack.push(value.unwrap_or(Value::None));
                }

                OpCode::StoreName => {
                    let idx = instr.operand.unwrap_or(0) as usize;
                    let name = chunk.names.get(idx).cloned().unwrap_or_default();
                    let value = self.stack.pop().unwrap_or(Value::None);

                    if let Some(frame) = self.call_stack.last_mut() {
                        frame.locals.insert(name, value);
                    } else {
                        self.globals.insert(name, value);
                    }
                }

                OpCode::LoadGlobal => {
                    let idx = instr.operand.unwrap_or(0) as usize;
                    let name = chunk.names.get(idx).cloned().unwrap_or_default();
                    let value = self.globals.get(&name).cloned().unwrap_or(Value::None);
                    self.stack.push(value);
                }

                OpCode::StoreGlobal => {
                    let idx = instr.operand.unwrap_or(0) as usize;
                    let name = chunk.names.get(idx).cloned().unwrap_or_default();
                    let value = self.stack.pop().unwrap_or(Value::None);
                    self.globals.insert(name, value);
                }

                OpCode::LoadLocal => {
                    let idx = instr.operand.unwrap_or(0) as usize;
                    let name = chunk.names.get(idx).cloned().unwrap_or_default();
                    let value = if let Some(frame) = self.call_stack.last() {
                        frame.locals.get(&name).cloned().unwrap_or(Value::None)
                    } else {
                        Value::None
                    };
                    self.stack.push(value);
                }

                OpCode::StoreLocal => {
                    let idx = instr.operand.unwrap_or(0) as usize;
                    let name = chunk.names.get(idx).cloned().unwrap_or_default();
                    let value = self.stack.pop().unwrap_or(Value::None);
                    if let Some(frame) = self.call_stack.last_mut() {
                        frame.locals.insert(name, value);
                    }
                }

                OpCode::Add => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(a.add(&b)?);
                }

                OpCode::Sub => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(a.sub(&b)?);
                }

                OpCode::Mul => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(a.mul(&b)?);
                }

                OpCode::Div => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(a.div(&b)?);
                }

                OpCode::FloorDiv => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(a.floor_div(&b)?);
                }

                OpCode::Mod => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(a.modulo(&b)?);
                }

                OpCode::Pow => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(a.power(&b)?);
                }

                OpCode::Neg => {
                    let a = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(a.negate()?);
                }

                OpCode::BitAnd => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(a.bit_and(&b)?);
                }

                OpCode::BitOr => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(a.bit_or(&b)?);
                }

                OpCode::BitXor => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(a.bit_xor(&b)?);
                }

                OpCode::BitNot => {
                    let a = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(a.bit_not()?);
                }

                OpCode::Shl => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(a.shl(&b)?);
                }

                OpCode::Shr => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(a.shr(&b)?);
                }

                OpCode::Eq => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(Value::Bool(a.eq(&b)));
                }

                OpCode::Ne => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(Value::Bool(!a.eq(&b)));
                }

                OpCode::Lt => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(Value::Bool(a.lt(&b)?));
                }

                OpCode::Le => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(Value::Bool(a.le(&b)?));
                }

                OpCode::Gt => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(Value::Bool(a.gt(&b)?));
                }

                OpCode::Ge => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(Value::Bool(a.ge(&b)?));
                }

                OpCode::And => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(Value::Bool(a.is_truthy() && b.is_truthy()));
                }

                OpCode::Or => {
                    let b = self.stack.pop().unwrap_or(Value::None);
                    let a = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(Value::Bool(a.is_truthy() || b.is_truthy()));
                }

                OpCode::Not => {
                    let a = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(a.not());
                }

                OpCode::Jump => {
                    ip = instr.operand.unwrap_or(0) as usize;
                }

                OpCode::JumpIfTrue => {
                    let cond = self.stack.pop().unwrap_or(Value::None);
                    if cond.is_truthy() {
                        ip = instr.operand.unwrap_or(0) as usize;
                    }
                }

                OpCode::JumpIfFalse => {
                    let cond = self.stack.pop().unwrap_or(Value::None);
                    if !cond.is_truthy() {
                        ip = instr.operand.unwrap_or(0) as usize;
                    }
                }

                OpCode::Call => {
                    let arg_count = instr.operand.unwrap_or(0) as usize;
                    let func = self.stack.pop().unwrap_or(Value::None);

                    if let Value::Function {
                        name: _,
                        params,
                        bytecode_offset,
                    } = func
                    {
                        let mut locals = HashMap::new();

                        let args_start = self.stack.len().saturating_sub(arg_count);
                        let args: Vec<Value> = self.stack.drain(args_start..).collect();

                        for (i, param) in params.iter().enumerate() {
                            let value = args.get(i).cloned().unwrap_or(Value::None);
                            locals.insert(param.clone(), value);
                        }

                        self.call_stack.push(CallFrame {
                            return_addr: ip,
                            base_pointer: self.stack.len(),
                            locals,
                        });

                        ip = bytecode_offset;
                    } else {
                        self.stack.push(Value::None);
                    }
                }

                OpCode::Return => {
                    let return_value = self.stack.pop().unwrap_or(Value::None);

                    if let Some(frame) = self.call_stack.pop() {
                        self.stack.truncate(frame.base_pointer);
                        self.stack.push(return_value);
                        ip = frame.return_addr;
                    } else {
                        return Ok(return_value);
                    }
                }

                OpCode::BuildList => {
                    let count = instr.operand.unwrap_or(0) as usize;
                    let start = self.stack.len().saturating_sub(count);
                    let elements: Vec<Value> = self.stack.drain(start..).collect();
                    self.stack.push(Value::List(elements));
                }

                OpCode::BuildDict => {
                    let count = instr.operand.unwrap_or(0) as usize;
                    let start = self.stack.len().saturating_sub(count * 2);
                    let items: Vec<Value> = self.stack.drain(start..).collect();
                    let mut pairs = Vec::new();

                    for i in (0..items.len()).step_by(2) {
                        if i + 1 < items.len() {
                            let key = match &items[i] {
                                Value::String(s) => s.clone(),
                                _ => format!("{}", items[i]),
                            };
                            pairs.push((key, items[i + 1].clone()));
                        }
                    }

                    self.stack.push(Value::Dict(pairs));
                }

                OpCode::BuildTuple => {
                    let count = instr.operand.unwrap_or(0) as usize;
                    let start = self.stack.len().saturating_sub(count);
                    let elements: Vec<Value> = self.stack.drain(start..).collect();
                    self.stack.push(Value::List(elements));
                }

                OpCode::BuildSet => {
                    let count = instr.operand.unwrap_or(0) as usize;
                    let start = self.stack.len().saturating_sub(count);
                    let elements: Vec<Value> = self.stack.drain(start..).collect();
                    self.stack.push(Value::List(elements));
                }

                OpCode::GetIndex => {
                    let index = self.stack.pop().unwrap_or(Value::None);
                    let obj = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(obj.get_index(&index)?);
                }

                OpCode::SetIndex => {
                    let value = self.stack.pop().unwrap_or(Value::None);
                    let index = self.stack.pop().unwrap_or(Value::None);
                    let mut obj = self.stack.pop().unwrap_or(Value::None);
                    obj.set_index(&index, value)?;
                    self.stack.push(obj);
                }

                OpCode::GetAttr => {
                    let idx = instr.operand.unwrap_or(0) as usize;
                    let _attr_name = chunk.names.get(idx).cloned().unwrap_or_default();
                    let _obj = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(Value::None);
                }

                OpCode::SetAttr => {
                    let idx = instr.operand.unwrap_or(0) as usize;
                    let _attr_name = chunk.names.get(idx).cloned().unwrap_or_default();
                    let _value = self.stack.pop().unwrap_or(Value::None);
                    let _obj = self.stack.pop().unwrap_or(Value::None);
                }

                OpCode::GetSlice => {
                    self.stack.push(Value::None);
                }

                OpCode::Pop => {
                    self.stack.pop();
                }

                OpCode::Dup => {
                    if let Some(top) = self.stack.last().cloned() {
                        self.stack.push(top);
                    }
                }

                OpCode::Rot2 => {
                    let len = self.stack.len();
                    if len >= 2 {
                        self.stack.swap(len - 1, len - 2);
                    }
                }

                OpCode::Rot3 => {
                    let len = self.stack.len();
                    if len >= 3 {
                        let top = self.stack.pop().unwrap();
                        let second = self.stack.pop().unwrap();
                        let third = self.stack.pop().unwrap();
                        self.stack.push(second);
                        self.stack.push(top);
                        self.stack.push(third);
                    }
                }

                OpCode::MakeFunction | OpCode::MakeClosure => {}

                OpCode::GetIter => {
                    let obj = self.stack.pop().unwrap_or(Value::None);
                    match obj {
                        Value::List(items) => {
                            let iter = items.into_iter();
                            self.iterator_stack.push(Box::new(iter));
                            self.stack.push(Value::Bool(true));
                        }
                        Value::String(s) => {
                            let chars: Vec<Value> = s
                                .chars()
                                .map(|c| Value::String(c.to_string()))
                                .collect();
                            let iter = chars.into_iter();
                            self.iterator_stack.push(Box::new(iter));
                            self.stack.push(Value::Bool(true));
                        }
                        _ => {
                            self.stack.push(Value::Bool(false));
                        }
                    }
                }

                OpCode::ForIter => {
                    if let Some(iter) = self.iterator_stack.last_mut() {
                        if let Some(value) = iter.next() {
                            self.stack.push(Value::Bool(true));
                            self.stack.push(value);
                        } else {
                            self.iterator_stack.pop();
                            self.stack.push(Value::Bool(false));
                        }
                    } else {
                        self.stack.push(Value::Bool(false));
                    }
                }

                OpCode::Print => {
                    let value = self.stack.pop().unwrap_or(Value::None);
                    println!("{}", value);
                    io::stdout().flush().ok();
                }

                OpCode::Input => {
                    let mut input = String::new();
                    io::stdin().read_line(&mut input).ok();
                    self.stack.push(Value::String(input.trim().to_string()));
                }

                OpCode::Contains => {
                    let item = self.stack.pop().unwrap_or(Value::None);
                    let container = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(Value::Bool(container.contains(&item)?));
                }

                OpCode::NotContains => {
                    let item = self.stack.pop().unwrap_or(Value::None);
                    let container = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(Value::Bool(!container.contains(&item)?));
                }

                OpCode::Len => {
                    let obj = self.stack.pop().unwrap_or(Value::None);
                    self.stack.push(obj.len()?);
                }

                OpCode::Halt => {
                    break;
                }
            }
        }

        Ok(self.stack.pop().unwrap_or(Value::None))
    }
}

impl Default for VirtualMachine {
    fn default() -> Self {
        Self::new()
    }
}
