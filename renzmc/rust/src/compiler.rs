use crate::bytecode::{BytecodeChunk, OpCode};
use crate::value::Value;
use serde_json;

pub struct BytecodeCompiler {
    chunk: BytecodeChunk,
    loop_starts: Vec<usize>,
    loop_ends: Vec<Vec<usize>>,
}

impl BytecodeCompiler {
    pub fn new() -> Self {
        BytecodeCompiler {
            chunk: BytecodeChunk::new(),
            loop_starts: Vec::new(),
            loop_ends: Vec::new(),
        }
    }

    pub fn compile_from_json(&mut self, ast_json: &str) -> Result<Vec<u8>, String> {
        let ast: serde_json::Value = serde_json::from_str(ast_json)
            .map_err(|e| format!("Failed to parse AST JSON: {}", e))?;

        self.compile_node(&ast)?;
        self.chunk.emit_opcode(OpCode::Halt);

        Ok(self.chunk.serialize())
    }

    pub fn compile_function(
        &mut self,
        name: &str,
        params: &[String],
        body_json: &str,
    ) -> Result<Vec<u8>, String> {
        let body: serde_json::Value = serde_json::from_str(body_json)
            .map_err(|e| format!("Failed to parse body JSON: {}", e))?;

        for param in params {
            self.chunk.add_name(param.clone());
        }

        let name_idx = self.chunk.add_name(name.to_string());

        if let Some(statements) = body.as_array() {
            for stmt in statements {
                self.compile_node(stmt)?;
            }
        } else {
            self.compile_node(&body)?;
        }

        let const_idx = self.chunk.add_constant(Value::Function {
            name: name.to_string(),
            params: params.to_vec(),
            bytecode_offset: 0,
        });
        self.chunk.emit_with_operand(OpCode::LoadConst, const_idx);
        self.chunk.emit_with_operand(OpCode::StoreName, name_idx);

        self.chunk.emit_opcode(OpCode::Halt);

        Ok(self.chunk.serialize())
    }

    fn compile_node(&mut self, node: &serde_json::Value) -> Result<(), String> {
        let node_type = node
            .get("type")
            .and_then(|t| t.as_str())
            .unwrap_or("");

        match node_type {
            "Program" => self.compile_program(node),
            "Block" => self.compile_block(node),
            "VarDecl" => self.compile_var_decl(node),
            "Assign" => self.compile_assign(node),
            "BinOp" => self.compile_binop(node),
            "UnaryOp" => self.compile_unary(node),
            "Num" => self.compile_num(node),
            "String" => self.compile_string(node),
            "Boolean" => self.compile_boolean(node),
            "NoneValue" => self.compile_none(),
            "Var" => self.compile_var(node),
            "List" => self.compile_list(node),
            "Dict" => self.compile_dict(node),
            "If" => self.compile_if(node),
            "While" => self.compile_while(node),
            "For" => self.compile_for(node),
            "ForEach" => self.compile_foreach(node),
            "FuncDecl" => self.compile_func_decl(node),
            "FuncCall" => self.compile_func_call(node),
            "Return" => self.compile_return(node),
            "Print" => self.compile_print(node),
            "Break" => self.compile_break(),
            "Continue" => self.compile_continue(),
            "IndexAccess" => self.compile_index_access(node),
            "CompoundAssign" => self.compile_compound_assign(node),
            "Ternary" => self.compile_ternary(node),
            "Lambda" => self.compile_lambda(node),
            "ListComp" => self.compile_list_comp(node),
            "" => {
                if node.is_number() {
                    let val = if let Some(i) = node.as_i64() {
                        Value::Int(i)
                    } else if let Some(f) = node.as_f64() {
                        Value::Float(f)
                    } else {
                        return Err("Invalid number".to_string());
                    };
                    let idx = self.chunk.add_constant(val);
                    self.chunk.emit_with_operand(OpCode::LoadConst, idx);
                    Ok(())
                } else if node.is_string() {
                    let s = node.as_str().unwrap().to_string();
                    let idx = self.chunk.add_constant(Value::String(s));
                    self.chunk.emit_with_operand(OpCode::LoadConst, idx);
                    Ok(())
                } else if node.is_boolean() {
                    let b = node.as_bool().unwrap();
                    let idx = self.chunk.add_constant(Value::Bool(b));
                    self.chunk.emit_with_operand(OpCode::LoadConst, idx);
                    Ok(())
                } else if node.is_null() {
                    let idx = self.chunk.add_constant(Value::None);
                    self.chunk.emit_with_operand(OpCode::LoadConst, idx);
                    Ok(())
                } else if node.is_array() {
                    if let Some(arr) = node.as_array() {
                        for item in arr {
                            self.compile_node(item)?;
                        }
                    }
                    Ok(())
                } else {
                    Ok(())
                }
            }
            _ => {
                Ok(())
            }
        }
    }

    fn compile_program(&mut self, node: &serde_json::Value) -> Result<(), String> {
        if let Some(statements) = node.get("statements").and_then(|s| s.as_array()) {
            for stmt in statements {
                self.compile_node(stmt)?;
            }
        }
        Ok(())
    }

    fn compile_block(&mut self, node: &serde_json::Value) -> Result<(), String> {
        if let Some(statements) = node.get("statements").and_then(|s| s.as_array()) {
            for stmt in statements {
                self.compile_node(stmt)?;
            }
        }
        Ok(())
    }

    fn compile_var_decl(&mut self, node: &serde_json::Value) -> Result<(), String> {
        if let Some(value) = node.get("value") {
            self.compile_node(value)?;
        } else {
            let idx = self.chunk.add_constant(Value::None);
            self.chunk.emit_with_operand(OpCode::LoadConst, idx);
        }

        let var_name = node
            .get("var_name")
            .and_then(|n| n.as_str())
            .unwrap_or("_");
        let name_idx = self.chunk.add_name(var_name.to_string());
        self.chunk.emit_with_operand(OpCode::StoreName, name_idx);

        Ok(())
    }

    fn compile_assign(&mut self, node: &serde_json::Value) -> Result<(), String> {
        if let Some(value) = node.get("value") {
            self.compile_node(value)?;
        }

        let var_name = if let Some(var) = node.get("var") {
            if let Some(name) = var.get("name").and_then(|n| n.as_str()) {
                name.to_string()
            } else if let Some(name) = var.as_str() {
                name.to_string()
            } else {
                "_".to_string()
            }
        } else {
            "_".to_string()
        };

        let name_idx = self.chunk.add_name(var_name);
        self.chunk.emit_with_operand(OpCode::StoreName, name_idx);

        Ok(())
    }

    fn compile_binop(&mut self, node: &serde_json::Value) -> Result<(), String> {
        if let Some(left) = node.get("left") {
            self.compile_node(left)?;
        }
        if let Some(right) = node.get("right") {
            self.compile_node(right)?;
        }

        let op = node
            .get("op")
            .and_then(|o| o.get("type"))
            .and_then(|t| t.as_str())
            .unwrap_or("");

        let opcode = match op {
            "TAMBAH" => OpCode::Add,
            "KURANG" => OpCode::Sub,
            "KALI" | "KALI_OP" => OpCode::Mul,
            "BAGI" => OpCode::Div,
            "PEMBAGIAN_BULAT" => OpCode::FloorDiv,
            "SISA_BAGI" => OpCode::Mod,
            "PANGKAT" => OpCode::Pow,
            "SAMA_DENGAN" => OpCode::Eq,
            "TIDAK_SAMA" => OpCode::Ne,
            "KURANG_DARI" => OpCode::Lt,
            "KURANG_SAMA" => OpCode::Le,
            "LEBIH_DARI" => OpCode::Gt,
            "LEBIH_SAMA" => OpCode::Ge,
            "DAN" => OpCode::And,
            "ATAU" => OpCode::Or,
            "BIT_DAN" | "BITWISE_AND" => OpCode::BitAnd,
            "BIT_ATAU" | "BITWISE_OR" => OpCode::BitOr,
            "BIT_XOR" | "BITWISE_XOR" => OpCode::BitXor,
            "GESER_KIRI" => OpCode::Shl,
            "GESER_KANAN" => OpCode::Shr,
            "DALAM" => OpCode::Contains,
            "TIDAK_DALAM" => OpCode::NotContains,
            _ => OpCode::Nop,
        };

        self.chunk.emit_opcode(opcode);
        Ok(())
    }

    fn compile_unary(&mut self, node: &serde_json::Value) -> Result<(), String> {
        if let Some(expr) = node.get("expr") {
            self.compile_node(expr)?;
        }

        let op = node
            .get("op")
            .and_then(|o| o.get("type"))
            .and_then(|t| t.as_str())
            .unwrap_or("");

        let opcode = match op {
            "KURANG" => OpCode::Neg,
            "TIDAK" | "NOT" | "BUKAN" => OpCode::Not,
            "BIT_NOT" | "BITWISE_NOT" => OpCode::BitNot,
            _ => OpCode::Nop,
        };

        self.chunk.emit_opcode(opcode);
        Ok(())
    }

    fn compile_num(&mut self, node: &serde_json::Value) -> Result<(), String> {
        let value = if let Some(v) = node.get("value") {
            if let Some(i) = v.as_i64() {
                Value::Int(i)
            } else if let Some(f) = v.as_f64() {
                Value::Float(f)
            } else {
                Value::Int(0)
            }
        } else {
            Value::Int(0)
        };

        let idx = self.chunk.add_constant(value);
        self.chunk.emit_with_operand(OpCode::LoadConst, idx);
        Ok(())
    }

    fn compile_string(&mut self, node: &serde_json::Value) -> Result<(), String> {
        let value = node
            .get("value")
            .and_then(|v| v.as_str())
            .unwrap_or("")
            .to_string();

        let idx = self.chunk.add_constant(Value::String(value));
        self.chunk.emit_with_operand(OpCode::LoadConst, idx);
        Ok(())
    }

    fn compile_boolean(&mut self, node: &serde_json::Value) -> Result<(), String> {
        let value = node.get("value").and_then(|v| v.as_bool()).unwrap_or(false);

        let idx = self.chunk.add_constant(Value::Bool(value));
        self.chunk.emit_with_operand(OpCode::LoadConst, idx);
        Ok(())
    }

    fn compile_none(&mut self) -> Result<(), String> {
        let idx = self.chunk.add_constant(Value::None);
        self.chunk.emit_with_operand(OpCode::LoadConst, idx);
        Ok(())
    }

    fn compile_var(&mut self, node: &serde_json::Value) -> Result<(), String> {
        let name = node
            .get("name")
            .and_then(|n| n.as_str())
            .unwrap_or("_")
            .to_string();

        let name_idx = self.chunk.add_name(name);
        self.chunk.emit_with_operand(OpCode::LoadName, name_idx);
        Ok(())
    }

    fn compile_list(&mut self, node: &serde_json::Value) -> Result<(), String> {
        let elements = node.get("elements").and_then(|e| e.as_array());
        let count = if let Some(elems) = elements {
            for elem in elems {
                self.compile_node(elem)?;
            }
            elems.len() as u32
        } else {
            0
        };

        self.chunk.emit_with_operand(OpCode::BuildList, count);
        Ok(())
    }

    fn compile_dict(&mut self, node: &serde_json::Value) -> Result<(), String> {
        let pairs = node.get("pairs").and_then(|p| p.as_array());
        let count = if let Some(ps) = pairs {
            for pair in ps {
                if let Some(key) = pair.get(0) {
                    self.compile_node(key)?;
                }
                if let Some(value) = pair.get(1) {
                    self.compile_node(value)?;
                }
            }
            ps.len() as u32
        } else {
            0
        };

        self.chunk.emit_with_operand(OpCode::BuildDict, count);
        Ok(())
    }

    fn compile_if(&mut self, node: &serde_json::Value) -> Result<(), String> {
        if let Some(condition) = node.get("condition") {
            self.compile_node(condition)?;
        }

        let jump_if_false = self.chunk.current_offset();
        self.chunk.emit_with_operand(OpCode::JumpIfFalse, 0);

        if let Some(if_body) = node.get("if_body").and_then(|b| b.as_array()) {
            for stmt in if_body {
                self.compile_node(stmt)?;
            }
        }

        let jump_end = self.chunk.current_offset();
        self.chunk.emit_with_operand(OpCode::Jump, 0);

        let else_start = self.chunk.current_offset();
        self.chunk.patch_jump(jump_if_false, else_start as u32);

        if let Some(else_body) = node.get("else_body").and_then(|b| b.as_array()) {
            for stmt in else_body {
                self.compile_node(stmt)?;
            }
        }

        let end = self.chunk.current_offset();
        self.chunk.patch_jump(jump_end, end as u32);

        Ok(())
    }

    fn compile_while(&mut self, node: &serde_json::Value) -> Result<(), String> {
        let loop_start = self.chunk.current_offset();
        self.loop_starts.push(loop_start);
        self.loop_ends.push(Vec::new());

        if let Some(condition) = node.get("condition") {
            self.compile_node(condition)?;
        }

        let jump_if_false = self.chunk.current_offset();
        self.chunk.emit_with_operand(OpCode::JumpIfFalse, 0);

        if let Some(body) = node.get("body").and_then(|b| b.as_array()) {
            for stmt in body {
                self.compile_node(stmt)?;
            }
        }

        self.chunk.emit_with_operand(OpCode::Jump, loop_start as u32);

        let loop_end = self.chunk.current_offset();
        self.chunk.patch_jump(jump_if_false, loop_end as u32);

        self.loop_starts.pop();
        if let Some(breaks) = self.loop_ends.pop() {
            for break_offset in breaks {
                self.chunk.patch_jump(break_offset, loop_end as u32);
            }
        }

        Ok(())
    }

    fn compile_for(&mut self, node: &serde_json::Value) -> Result<(), String> {
        let var_name = node
            .get("var_name")
            .and_then(|n| n.as_str())
            .unwrap_or("i")
            .to_string();

        if let Some(start) = node.get("start") {
            self.compile_node(start)?;
        }
        let var_idx = self.chunk.add_name(var_name.clone());
        self.chunk.emit_with_operand(OpCode::StoreName, var_idx);

        let loop_start = self.chunk.current_offset();
        self.loop_starts.push(loop_start);
        self.loop_ends.push(Vec::new());

        self.chunk.emit_with_operand(OpCode::LoadName, var_idx);
        if let Some(end) = node.get("end") {
            self.compile_node(end)?;
        }
        self.chunk.emit_opcode(OpCode::Le);

        let jump_if_false = self.chunk.current_offset();
        self.chunk.emit_with_operand(OpCode::JumpIfFalse, 0);

        if let Some(body) = node.get("body").and_then(|b| b.as_array()) {
            for stmt in body {
                self.compile_node(stmt)?;
            }
        }

        self.chunk.emit_with_operand(OpCode::LoadName, var_idx);
        let one_idx = self.chunk.add_constant(Value::Int(1));
        self.chunk.emit_with_operand(OpCode::LoadConst, one_idx);
        self.chunk.emit_opcode(OpCode::Add);
        self.chunk.emit_with_operand(OpCode::StoreName, var_idx);

        self.chunk.emit_with_operand(OpCode::Jump, loop_start as u32);

        let loop_end = self.chunk.current_offset();
        self.chunk.patch_jump(jump_if_false, loop_end as u32);

        self.loop_starts.pop();
        if let Some(breaks) = self.loop_ends.pop() {
            for break_offset in breaks {
                self.chunk.patch_jump(break_offset, loop_end as u32);
            }
        }

        Ok(())
    }

    fn compile_foreach(&mut self, node: &serde_json::Value) -> Result<(), String> {
        let var_name = node
            .get("var_name")
            .and_then(|n| n.as_str())
            .unwrap_or("item")
            .to_string();

        if let Some(iterable) = node.get("iterable") {
            self.compile_node(iterable)?;
        }
        self.chunk.emit_opcode(OpCode::GetIter);

        let loop_start = self.chunk.current_offset();
        self.loop_starts.push(loop_start);
        self.loop_ends.push(Vec::new());

        self.chunk.emit_opcode(OpCode::ForIter);
        let jump_if_false = self.chunk.current_offset();
        self.chunk.emit_with_operand(OpCode::JumpIfFalse, 0);

        let var_idx = self.chunk.add_name(var_name);
        self.chunk.emit_with_operand(OpCode::StoreName, var_idx);

        if let Some(body) = node.get("body").and_then(|b| b.as_array()) {
            for stmt in body {
                self.compile_node(stmt)?;
            }
        }

        self.chunk.emit_with_operand(OpCode::Jump, loop_start as u32);

        let loop_end = self.chunk.current_offset();
        self.chunk.patch_jump(jump_if_false, loop_end as u32);

        self.loop_starts.pop();
        if let Some(breaks) = self.loop_ends.pop() {
            for break_offset in breaks {
                self.chunk.patch_jump(break_offset, loop_end as u32);
            }
        }

        Ok(())
    }

    fn compile_func_decl(&mut self, node: &serde_json::Value) -> Result<(), String> {
        let name = node
            .get("name")
            .and_then(|n| n.as_str())
            .unwrap_or("anonymous")
            .to_string();

        let params: Vec<String> = node
            .get("params")
            .and_then(|p| p.as_array())
            .map(|arr| {
                arr.iter()
                    .filter_map(|p| p.as_str().map(|s| s.to_string()))
                    .collect()
            })
            .unwrap_or_default();

        let func_start = self.chunk.current_offset();

        let jump_over = self.chunk.current_offset();
        self.chunk.emit_with_operand(OpCode::Jump, 0);

        let func_body_start = self.chunk.current_offset();

        if let Some(body) = node.get("body").and_then(|b| b.as_array()) {
            for stmt in body {
                self.compile_node(stmt)?;
            }
        }

        let none_idx = self.chunk.add_constant(Value::None);
        self.chunk.emit_with_operand(OpCode::LoadConst, none_idx);
        self.chunk.emit_opcode(OpCode::Return);

        let after_func = self.chunk.current_offset();
        self.chunk.patch_jump(jump_over, after_func as u32);

        let func_value = Value::Function {
            name: name.clone(),
            params,
            bytecode_offset: func_body_start,
        };
        let const_idx = self.chunk.add_constant(func_value);
        self.chunk.emit_with_operand(OpCode::LoadConst, const_idx);

        let name_idx = self.chunk.add_name(name);
        self.chunk.emit_with_operand(OpCode::StoreName, name_idx);

        Ok(())
    }

    fn compile_func_call(&mut self, node: &serde_json::Value) -> Result<(), String> {
        let func_name = node
            .get("name")
            .and_then(|n| n.as_str())
            .unwrap_or("");

        if let Some(args) = node.get("args").and_then(|a| a.as_array()) {
            for arg in args {
                self.compile_node(arg)?;
            }

            if !func_name.is_empty() {
                let name_idx = self.chunk.add_name(func_name.to_string());
                self.chunk.emit_with_operand(OpCode::LoadName, name_idx);
            } else if let Some(func_expr) = node.get("func_expr") {
                self.compile_node(func_expr)?;
            }

            self.chunk.emit_with_operand(OpCode::Call, args.len() as u32);
        }

        Ok(())
    }

    fn compile_return(&mut self, node: &serde_json::Value) -> Result<(), String> {
        if let Some(expr) = node.get("expr") {
            self.compile_node(expr)?;
        } else {
            let idx = self.chunk.add_constant(Value::None);
            self.chunk.emit_with_operand(OpCode::LoadConst, idx);
        }

        self.chunk.emit_opcode(OpCode::Return);
        Ok(())
    }

    fn compile_print(&mut self, node: &serde_json::Value) -> Result<(), String> {
        if let Some(expr) = node.get("expr") {
            self.compile_node(expr)?;
        }

        self.chunk.emit_opcode(OpCode::Print);
        Ok(())
    }

    fn compile_break(&mut self) -> Result<(), String> {
        let offset = self.chunk.current_offset();
        self.chunk.emit_with_operand(OpCode::Jump, 0);

        if let Some(breaks) = self.loop_ends.last_mut() {
            breaks.push(offset);
        }

        Ok(())
    }

    fn compile_continue(&mut self) -> Result<(), String> {
        if let Some(&loop_start) = self.loop_starts.last() {
            self.chunk.emit_with_operand(OpCode::Jump, loop_start as u32);
        }

        Ok(())
    }

    fn compile_index_access(&mut self, node: &serde_json::Value) -> Result<(), String> {
        if let Some(obj) = node.get("obj") {
            self.compile_node(obj)?;
        }
        if let Some(index) = node.get("index") {
            self.compile_node(index)?;
        }

        self.chunk.emit_opcode(OpCode::GetIndex);
        Ok(())
    }

    fn compile_compound_assign(&mut self, node: &serde_json::Value) -> Result<(), String> {
        let var_name = if let Some(var) = node.get("var") {
            var.get("name").and_then(|n| n.as_str()).unwrap_or("_")
        } else {
            "_"
        };

        let name_idx = self.chunk.add_name(var_name.to_string());
        self.chunk.emit_with_operand(OpCode::LoadName, name_idx);

        if let Some(value) = node.get("value") {
            self.compile_node(value)?;
        }

        let op = node
            .get("op")
            .and_then(|o| o.get("type"))
            .and_then(|t| t.as_str())
            .unwrap_or("");

        let opcode = match op {
            "TAMBAH_SAMA_DENGAN" => OpCode::Add,
            "KURANG_SAMA_DENGAN" => OpCode::Sub,
            "KALI_SAMA_DENGAN" => OpCode::Mul,
            "BAGI_SAMA_DENGAN" => OpCode::Div,
            "PEMBAGIAN_BULAT_SAMA_DENGAN" => OpCode::FloorDiv,
            "SISA_SAMA_DENGAN" => OpCode::Mod,
            "PANGKAT_SAMA_DENGAN" => OpCode::Pow,
            _ => OpCode::Add,
        };

        self.chunk.emit_opcode(opcode);
        self.chunk.emit_with_operand(OpCode::StoreName, name_idx);

        Ok(())
    }

    fn compile_ternary(&mut self, node: &serde_json::Value) -> Result<(), String> {
        if let Some(condition) = node.get("condition") {
            self.compile_node(condition)?;
        }

        let jump_if_false = self.chunk.current_offset();
        self.chunk.emit_with_operand(OpCode::JumpIfFalse, 0);

        if let Some(if_expr) = node.get("if_expr") {
            self.compile_node(if_expr)?;
        }

        let jump_end = self.chunk.current_offset();
        self.chunk.emit_with_operand(OpCode::Jump, 0);

        let else_start = self.chunk.current_offset();
        self.chunk.patch_jump(jump_if_false, else_start as u32);

        if let Some(else_expr) = node.get("else_expr") {
            self.compile_node(else_expr)?;
        }

        let end = self.chunk.current_offset();
        self.chunk.patch_jump(jump_end, end as u32);

        Ok(())
    }

    fn compile_lambda(&mut self, node: &serde_json::Value) -> Result<(), String> {
        let params: Vec<String> = node
            .get("params")
            .and_then(|p| p.as_array())
            .map(|arr| {
                arr.iter()
                    .filter_map(|p| p.as_str().map(|s| s.to_string()))
                    .collect()
            })
            .unwrap_or_default();

        let jump_over = self.chunk.current_offset();
        self.chunk.emit_with_operand(OpCode::Jump, 0);

        let lambda_start = self.chunk.current_offset();

        if let Some(body) = node.get("body") {
            self.compile_node(body)?;
        }
        self.chunk.emit_opcode(OpCode::Return);

        let after_lambda = self.chunk.current_offset();
        self.chunk.patch_jump(jump_over, after_lambda as u32);

        let func_value = Value::Function {
            name: "<lambda>".to_string(),
            params,
            bytecode_offset: lambda_start,
        };
        let const_idx = self.chunk.add_constant(func_value);
        self.chunk.emit_with_operand(OpCode::LoadConst, const_idx);

        Ok(())
    }

    fn compile_list_comp(&mut self, node: &serde_json::Value) -> Result<(), String> {
        let zero_idx = self.chunk.add_constant(Value::Int(0));
        self.chunk.emit_with_operand(OpCode::BuildList, 0);

        if let Some(iterable) = node.get("iterable") {
            self.compile_node(iterable)?;
        }
        self.chunk.emit_opcode(OpCode::GetIter);

        let loop_start = self.chunk.current_offset();

        self.chunk.emit_opcode(OpCode::ForIter);
        let jump_if_false = self.chunk.current_offset();
        self.chunk.emit_with_operand(OpCode::JumpIfFalse, 0);

        let var_name = node
            .get("var_name")
            .and_then(|n| n.as_str())
            .unwrap_or("item")
            .to_string();
        let var_idx = self.chunk.add_name(var_name);
        self.chunk.emit_with_operand(OpCode::StoreName, var_idx);

        let mut should_add = true;
        if let Some(condition) = node.get("condition") {
            self.compile_node(condition)?;
            let skip_jump = self.chunk.current_offset();
            self.chunk.emit_with_operand(OpCode::JumpIfFalse, 0);

            if let Some(expr) = node.get("expr") {
                self.compile_node(expr)?;
            }

            self.chunk.emit_with_operand(OpCode::Jump, loop_start as u32);
            let skip_target = self.chunk.current_offset();
            self.chunk.patch_jump(skip_jump, skip_target as u32);
            should_add = false;
        }

        if should_add {
            if let Some(expr) = node.get("expr") {
                self.compile_node(expr)?;
            }
        }

        self.chunk.emit_with_operand(OpCode::Jump, loop_start as u32);

        let loop_end = self.chunk.current_offset();
        self.chunk.patch_jump(jump_if_false, loop_end as u32);

        Ok(())
    }
}

impl Default for BytecodeCompiler {
    fn default() -> Self {
        Self::new()
    }
}
