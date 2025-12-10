use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[repr(u8)]
pub enum OpCode {
    Nop = 0,
    LoadConst = 1,
    LoadName = 2,
    StoreName = 3,
    LoadGlobal = 4,
    StoreGlobal = 5,
    LoadLocal = 6,
    StoreLocal = 7,
    
    Add = 10,
    Sub = 11,
    Mul = 12,
    Div = 13,
    FloorDiv = 14,
    Mod = 15,
    Pow = 16,
    Neg = 17,
    
    BitAnd = 20,
    BitOr = 21,
    BitXor = 22,
    BitNot = 23,
    Shl = 24,
    Shr = 25,
    
    Eq = 30,
    Ne = 31,
    Lt = 32,
    Le = 33,
    Gt = 34,
    Ge = 35,
    
    And = 40,
    Or = 41,
    Not = 42,
    
    Jump = 50,
    JumpIfTrue = 51,
    JumpIfFalse = 52,
    
    Call = 60,
    Return = 61,
    
    BuildList = 70,
    BuildDict = 71,
    BuildTuple = 72,
    BuildSet = 73,
    
    GetIndex = 80,
    SetIndex = 81,
    GetAttr = 82,
    SetAttr = 83,
    GetSlice = 84,
    
    Pop = 90,
    Dup = 91,
    Rot2 = 92,
    Rot3 = 93,
    
    MakeFunction = 100,
    MakeClosure = 101,
    
    ForIter = 110,
    GetIter = 111,
    
    Print = 120,
    Input = 121,
    
    Contains = 130,
    NotContains = 131,
    Len = 132,
    
    Halt = 255,
}

impl From<u8> for OpCode {
    fn from(byte: u8) -> Self {
        match byte {
            0 => OpCode::Nop,
            1 => OpCode::LoadConst,
            2 => OpCode::LoadName,
            3 => OpCode::StoreName,
            4 => OpCode::LoadGlobal,
            5 => OpCode::StoreGlobal,
            6 => OpCode::LoadLocal,
            7 => OpCode::StoreLocal,
            10 => OpCode::Add,
            11 => OpCode::Sub,
            12 => OpCode::Mul,
            13 => OpCode::Div,
            14 => OpCode::FloorDiv,
            15 => OpCode::Mod,
            16 => OpCode::Pow,
            17 => OpCode::Neg,
            20 => OpCode::BitAnd,
            21 => OpCode::BitOr,
            22 => OpCode::BitXor,
            23 => OpCode::BitNot,
            24 => OpCode::Shl,
            25 => OpCode::Shr,
            30 => OpCode::Eq,
            31 => OpCode::Ne,
            32 => OpCode::Lt,
            33 => OpCode::Le,
            34 => OpCode::Gt,
            35 => OpCode::Ge,
            40 => OpCode::And,
            41 => OpCode::Or,
            42 => OpCode::Not,
            50 => OpCode::Jump,
            51 => OpCode::JumpIfTrue,
            52 => OpCode::JumpIfFalse,
            60 => OpCode::Call,
            61 => OpCode::Return,
            70 => OpCode::BuildList,
            71 => OpCode::BuildDict,
            72 => OpCode::BuildTuple,
            73 => OpCode::BuildSet,
            80 => OpCode::GetIndex,
            81 => OpCode::SetIndex,
            82 => OpCode::GetAttr,
            83 => OpCode::SetAttr,
            84 => OpCode::GetSlice,
            90 => OpCode::Pop,
            91 => OpCode::Dup,
            92 => OpCode::Rot2,
            93 => OpCode::Rot3,
            100 => OpCode::MakeFunction,
            101 => OpCode::MakeClosure,
            110 => OpCode::ForIter,
            111 => OpCode::GetIter,
            120 => OpCode::Print,
            121 => OpCode::Input,
            130 => OpCode::Contains,
            131 => OpCode::NotContains,
            132 => OpCode::Len,
            255 => OpCode::Halt,
            _ => OpCode::Nop,
        }
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Instruction {
    pub opcode: OpCode,
    pub operand: Option<u32>,
}

impl Instruction {
    pub fn new(opcode: OpCode) -> Self {
        Instruction {
            opcode,
            operand: None,
        }
    }

    pub fn with_operand(opcode: OpCode, operand: u32) -> Self {
        Instruction {
            opcode,
            operand: Some(operand),
        }
    }

    pub fn encode(&self) -> Vec<u8> {
        let mut bytes = vec![self.opcode as u8];
        if let Some(op) = self.operand {
            bytes.extend_from_slice(&op.to_le_bytes());
        }
        bytes
    }

    pub fn decode(bytes: &[u8], offset: usize) -> (Self, usize) {
        let opcode = OpCode::from(bytes[offset]);
        let needs_operand = matches!(
            opcode,
            OpCode::LoadConst
                | OpCode::LoadName
                | OpCode::StoreName
                | OpCode::LoadGlobal
                | OpCode::StoreGlobal
                | OpCode::LoadLocal
                | OpCode::StoreLocal
                | OpCode::Jump
                | OpCode::JumpIfTrue
                | OpCode::JumpIfFalse
                | OpCode::Call
                | OpCode::BuildList
                | OpCode::BuildDict
                | OpCode::BuildTuple
                | OpCode::BuildSet
                | OpCode::MakeFunction
                | OpCode::MakeClosure
                | OpCode::GetAttr
                | OpCode::SetAttr
        );

        if needs_operand && offset + 4 < bytes.len() {
            let operand = u32::from_le_bytes([
                bytes[offset + 1],
                bytes[offset + 2],
                bytes[offset + 3],
                bytes[offset + 4],
            ]);
            (
                Instruction {
                    opcode,
                    operand: Some(operand),
                },
                5,
            )
        } else {
            (
                Instruction {
                    opcode,
                    operand: None,
                },
                1,
            )
        }
    }
}

#[derive(Debug, Clone, Default, Serialize, Deserialize)]
pub struct BytecodeChunk {
    pub code: Vec<u8>,
    pub constants: Vec<crate::value::Value>,
    pub names: Vec<String>,
    pub line_numbers: Vec<(usize, u32)>,
}

impl BytecodeChunk {
    pub fn new() -> Self {
        BytecodeChunk {
            code: Vec::new(),
            constants: Vec::new(),
            names: Vec::new(),
            line_numbers: Vec::new(),
        }
    }

    pub fn emit(&mut self, instruction: Instruction) {
        self.code.extend(instruction.encode());
    }

    pub fn emit_opcode(&mut self, opcode: OpCode) {
        self.emit(Instruction::new(opcode));
    }

    pub fn emit_with_operand(&mut self, opcode: OpCode, operand: u32) {
        self.emit(Instruction::with_operand(opcode, operand));
    }

    pub fn add_constant(&mut self, value: crate::value::Value) -> u32 {
        self.constants.push(value);
        (self.constants.len() - 1) as u32
    }

    pub fn add_name(&mut self, name: String) -> u32 {
        if let Some(idx) = self.names.iter().position(|n| n == &name) {
            return idx as u32;
        }
        self.names.push(name);
        (self.names.len() - 1) as u32
    }

    pub fn current_offset(&self) -> usize {
        self.code.len()
    }

    pub fn patch_jump(&mut self, offset: usize, target: u32) {
        let bytes = target.to_le_bytes();
        self.code[offset + 1] = bytes[0];
        self.code[offset + 2] = bytes[1];
        self.code[offset + 3] = bytes[2];
        self.code[offset + 4] = bytes[3];
    }

    pub fn serialize(&self) -> Vec<u8> {
        let mut result = Vec::new();
        
        let magic = b"RMCB";
        result.extend_from_slice(magic);
        
        result.push(0x01);
        
        let code_len = self.code.len() as u32;
        result.extend_from_slice(&code_len.to_le_bytes());
        result.extend_from_slice(&self.code);
        
        let const_json = serde_json::to_string(&self.constants).unwrap_or_default();
        let const_len = const_json.len() as u32;
        result.extend_from_slice(&const_len.to_le_bytes());
        result.extend_from_slice(const_json.as_bytes());
        
        let names_json = serde_json::to_string(&self.names).unwrap_or_default();
        let names_len = names_json.len() as u32;
        result.extend_from_slice(&names_len.to_le_bytes());
        result.extend_from_slice(names_json.as_bytes());
        
        result
    }

    pub fn deserialize(data: &[u8]) -> Result<Self, String> {
        if data.len() < 9 {
            return Err("Invalid bytecode: too short".to_string());
        }

        if &data[0..4] != b"RMCB" {
            return Err("Invalid bytecode: wrong magic number".to_string());
        }

        let _version = data[4];
        let mut offset = 5;

        let code_len = u32::from_le_bytes([
            data[offset],
            data[offset + 1],
            data[offset + 2],
            data[offset + 3],
        ]) as usize;
        offset += 4;

        let code = data[offset..offset + code_len].to_vec();
        offset += code_len;

        let const_len = u32::from_le_bytes([
            data[offset],
            data[offset + 1],
            data[offset + 2],
            data[offset + 3],
        ]) as usize;
        offset += 4;

        let const_json = std::str::from_utf8(&data[offset..offset + const_len])
            .map_err(|e| format!("Invalid UTF-8 in constants: {}", e))?;
        let constants: Vec<crate::value::Value> = serde_json::from_str(const_json)
            .map_err(|e| format!("Failed to parse constants: {}", e))?;
        offset += const_len;

        let names_len = u32::from_le_bytes([
            data[offset],
            data[offset + 1],
            data[offset + 2],
            data[offset + 3],
        ]) as usize;
        offset += 4;

        let names_json = std::str::from_utf8(&data[offset..offset + names_len])
            .map_err(|e| format!("Invalid UTF-8 in names: {}", e))?;
        let names: Vec<String> = serde_json::from_str(names_json)
            .map_err(|e| format!("Failed to parse names: {}", e))?;

        Ok(BytecodeChunk {
            code,
            constants,
            names,
            line_numbers: Vec::new(),
        })
    }
}
