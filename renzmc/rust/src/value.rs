use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum Value {
    None,
    Bool(bool),
    Int(i64),
    Float(f64),
    String(String),
    List(Vec<Value>),
    Dict(Vec<(String, Value)>),
    Function {
        name: String,
        params: Vec<String>,
        bytecode_offset: usize,
    },
}

impl Value {
    pub fn is_truthy(&self) -> bool {
        match self {
            Value::None => false,
            Value::Bool(b) => *b,
            Value::Int(i) => *i != 0,
            Value::Float(f) => *f != 0.0,
            Value::String(s) => !s.is_empty(),
            Value::List(l) => !l.is_empty(),
            Value::Dict(d) => !d.is_empty(),
            Value::Function { .. } => true,
        }
    }

    pub fn type_name(&self) -> &'static str {
        match self {
            Value::None => "none",
            Value::Bool(_) => "bool",
            Value::Int(_) => "int",
            Value::Float(_) => "float",
            Value::String(_) => "string",
            Value::List(_) => "list",
            Value::Dict(_) => "dict",
            Value::Function { .. } => "function",
        }
    }

    pub fn add(&self, other: &Value) -> Result<Value, String> {
        match (self, other) {
            (Value::Int(a), Value::Int(b)) => Ok(Value::Int(a + b)),
            (Value::Float(a), Value::Float(b)) => Ok(Value::Float(a + b)),
            (Value::Int(a), Value::Float(b)) => Ok(Value::Float(*a as f64 + b)),
            (Value::Float(a), Value::Int(b)) => Ok(Value::Float(a + *b as f64)),
            (Value::String(a), Value::String(b)) => Ok(Value::String(format!("{}{}", a, b))),
            (Value::List(a), Value::List(b)) => {
                let mut result = a.clone();
                result.extend(b.clone());
                Ok(Value::List(result))
            }
            _ => Err(format!(
                "Cannot add {} and {}",
                self.type_name(),
                other.type_name()
            )),
        }
    }

    pub fn sub(&self, other: &Value) -> Result<Value, String> {
        match (self, other) {
            (Value::Int(a), Value::Int(b)) => Ok(Value::Int(a - b)),
            (Value::Float(a), Value::Float(b)) => Ok(Value::Float(a - b)),
            (Value::Int(a), Value::Float(b)) => Ok(Value::Float(*a as f64 - b)),
            (Value::Float(a), Value::Int(b)) => Ok(Value::Float(a - *b as f64)),
            _ => Err(format!(
                "Cannot subtract {} from {}",
                other.type_name(),
                self.type_name()
            )),
        }
    }

    pub fn mul(&self, other: &Value) -> Result<Value, String> {
        match (self, other) {
            (Value::Int(a), Value::Int(b)) => Ok(Value::Int(a * b)),
            (Value::Float(a), Value::Float(b)) => Ok(Value::Float(a * b)),
            (Value::Int(a), Value::Float(b)) => Ok(Value::Float(*a as f64 * b)),
            (Value::Float(a), Value::Int(b)) => Ok(Value::Float(a * *b as f64)),
            (Value::String(s), Value::Int(n)) | (Value::Int(n), Value::String(s)) => {
                Ok(Value::String(s.repeat(*n as usize)))
            }
            (Value::List(l), Value::Int(n)) | (Value::Int(n), Value::List(l)) => {
                let mut result = Vec::new();
                for _ in 0..*n {
                    result.extend(l.clone());
                }
                Ok(Value::List(result))
            }
            _ => Err(format!(
                "Cannot multiply {} and {}",
                self.type_name(),
                other.type_name()
            )),
        }
    }

    pub fn div(&self, other: &Value) -> Result<Value, String> {
        match (self, other) {
            (Value::Int(a), Value::Int(b)) => {
                if *b == 0 {
                    Err("Division by zero".to_string())
                } else {
                    Ok(Value::Float(*a as f64 / *b as f64))
                }
            }
            (Value::Float(a), Value::Float(b)) => {
                if *b == 0.0 {
                    Err("Division by zero".to_string())
                } else {
                    Ok(Value::Float(a / b))
                }
            }
            (Value::Int(a), Value::Float(b)) => {
                if *b == 0.0 {
                    Err("Division by zero".to_string())
                } else {
                    Ok(Value::Float(*a as f64 / b))
                }
            }
            (Value::Float(a), Value::Int(b)) => {
                if *b == 0 {
                    Err("Division by zero".to_string())
                } else {
                    Ok(Value::Float(a / *b as f64))
                }
            }
            _ => Err(format!(
                "Cannot divide {} by {}",
                self.type_name(),
                other.type_name()
            )),
        }
    }

    pub fn floor_div(&self, other: &Value) -> Result<Value, String> {
        match (self, other) {
            (Value::Int(a), Value::Int(b)) => {
                if *b == 0 {
                    Err("Division by zero".to_string())
                } else {
                    Ok(Value::Int(a / b))
                }
            }
            (Value::Float(a), Value::Float(b)) => {
                if *b == 0.0 {
                    Err("Division by zero".to_string())
                } else {
                    Ok(Value::Int((a / b).floor() as i64))
                }
            }
            (Value::Int(a), Value::Float(b)) => {
                if *b == 0.0 {
                    Err("Division by zero".to_string())
                } else {
                    Ok(Value::Int((*a as f64 / b).floor() as i64))
                }
            }
            (Value::Float(a), Value::Int(b)) => {
                if *b == 0 {
                    Err("Division by zero".to_string())
                } else {
                    Ok(Value::Int((a / *b as f64).floor() as i64))
                }
            }
            _ => Err(format!(
                "Cannot floor divide {} by {}",
                self.type_name(),
                other.type_name()
            )),
        }
    }

    pub fn modulo(&self, other: &Value) -> Result<Value, String> {
        match (self, other) {
            (Value::Int(a), Value::Int(b)) => {
                if *b == 0 {
                    Err("Modulo by zero".to_string())
                } else {
                    Ok(Value::Int(a % b))
                }
            }
            (Value::Float(a), Value::Float(b)) => {
                if *b == 0.0 {
                    Err("Modulo by zero".to_string())
                } else {
                    Ok(Value::Float(a % b))
                }
            }
            (Value::Int(a), Value::Float(b)) => {
                if *b == 0.0 {
                    Err("Modulo by zero".to_string())
                } else {
                    Ok(Value::Float(*a as f64 % b))
                }
            }
            (Value::Float(a), Value::Int(b)) => {
                if *b == 0 {
                    Err("Modulo by zero".to_string())
                } else {
                    Ok(Value::Float(a % *b as f64))
                }
            }
            _ => Err(format!(
                "Cannot modulo {} by {}",
                self.type_name(),
                other.type_name()
            )),
        }
    }

    pub fn power(&self, other: &Value) -> Result<Value, String> {
        match (self, other) {
            (Value::Int(a), Value::Int(b)) => {
                if *b >= 0 {
                    Ok(Value::Int(a.pow(*b as u32)))
                } else {
                    Ok(Value::Float((*a as f64).powi(*b as i32)))
                }
            }
            (Value::Float(a), Value::Float(b)) => Ok(Value::Float(a.powf(*b))),
            (Value::Int(a), Value::Float(b)) => Ok(Value::Float((*a as f64).powf(*b))),
            (Value::Float(a), Value::Int(b)) => Ok(Value::Float(a.powi(*b as i32))),
            _ => Err(format!(
                "Cannot raise {} to power {}",
                self.type_name(),
                other.type_name()
            )),
        }
    }

    pub fn eq(&self, other: &Value) -> bool {
        match (self, other) {
            (Value::None, Value::None) => true,
            (Value::Bool(a), Value::Bool(b)) => a == b,
            (Value::Int(a), Value::Int(b)) => a == b,
            (Value::Float(a), Value::Float(b)) => (a - b).abs() < f64::EPSILON,
            (Value::Int(a), Value::Float(b)) => (*a as f64 - b).abs() < f64::EPSILON,
            (Value::Float(a), Value::Int(b)) => (a - *b as f64).abs() < f64::EPSILON,
            (Value::String(a), Value::String(b)) => a == b,
            (Value::List(a), Value::List(b)) => {
                if a.len() != b.len() {
                    return false;
                }
                a.iter().zip(b.iter()).all(|(x, y)| x.eq(y))
            }
            _ => false,
        }
    }

    pub fn lt(&self, other: &Value) -> Result<bool, String> {
        match (self, other) {
            (Value::Int(a), Value::Int(b)) => Ok(a < b),
            (Value::Float(a), Value::Float(b)) => Ok(a < b),
            (Value::Int(a), Value::Float(b)) => Ok((*a as f64) < *b),
            (Value::Float(a), Value::Int(b)) => Ok(*a < (*b as f64)),
            (Value::String(a), Value::String(b)) => Ok(a < b),
            _ => Err(format!(
                "Cannot compare {} and {}",
                self.type_name(),
                other.type_name()
            )),
        }
    }

    pub fn le(&self, other: &Value) -> Result<bool, String> {
        match (self, other) {
            (Value::Int(a), Value::Int(b)) => Ok(a <= b),
            (Value::Float(a), Value::Float(b)) => Ok(a <= b),
            (Value::Int(a), Value::Float(b)) => Ok((*a as f64) <= *b),
            (Value::Float(a), Value::Int(b)) => Ok(*a <= (*b as f64)),
            (Value::String(a), Value::String(b)) => Ok(a <= b),
            _ => Err(format!(
                "Cannot compare {} and {}",
                self.type_name(),
                other.type_name()
            )),
        }
    }

    pub fn gt(&self, other: &Value) -> Result<bool, String> {
        self.lt(other).map(|r| !r && !self.eq(other))
    }

    pub fn ge(&self, other: &Value) -> Result<bool, String> {
        self.lt(other).map(|r| !r)
    }

    pub fn negate(&self) -> Result<Value, String> {
        match self {
            Value::Int(i) => Ok(Value::Int(-i)),
            Value::Float(f) => Ok(Value::Float(-f)),
            _ => Err(format!("Cannot negate {}", self.type_name())),
        }
    }

    pub fn not(&self) -> Value {
        Value::Bool(!self.is_truthy())
    }

    pub fn bit_and(&self, other: &Value) -> Result<Value, String> {
        match (self, other) {
            (Value::Int(a), Value::Int(b)) => Ok(Value::Int(a & b)),
            _ => Err(format!(
                "Cannot bitwise AND {} and {}",
                self.type_name(),
                other.type_name()
            )),
        }
    }

    pub fn bit_or(&self, other: &Value) -> Result<Value, String> {
        match (self, other) {
            (Value::Int(a), Value::Int(b)) => Ok(Value::Int(a | b)),
            _ => Err(format!(
                "Cannot bitwise OR {} and {}",
                self.type_name(),
                other.type_name()
            )),
        }
    }

    pub fn bit_xor(&self, other: &Value) -> Result<Value, String> {
        match (self, other) {
            (Value::Int(a), Value::Int(b)) => Ok(Value::Int(a ^ b)),
            _ => Err(format!(
                "Cannot bitwise XOR {} and {}",
                self.type_name(),
                other.type_name()
            )),
        }
    }

    pub fn bit_not(&self) -> Result<Value, String> {
        match self {
            Value::Int(i) => Ok(Value::Int(!i)),
            _ => Err(format!("Cannot bitwise NOT {}", self.type_name())),
        }
    }

    pub fn shl(&self, other: &Value) -> Result<Value, String> {
        match (self, other) {
            (Value::Int(a), Value::Int(b)) => Ok(Value::Int(a << b)),
            _ => Err(format!(
                "Cannot left shift {} by {}",
                self.type_name(),
                other.type_name()
            )),
        }
    }

    pub fn shr(&self, other: &Value) -> Result<Value, String> {
        match (self, other) {
            (Value::Int(a), Value::Int(b)) => Ok(Value::Int(a >> b)),
            _ => Err(format!(
                "Cannot right shift {} by {}",
                self.type_name(),
                other.type_name()
            )),
        }
    }

    pub fn get_index(&self, index: &Value) -> Result<Value, String> {
        match (self, index) {
            (Value::List(list), Value::Int(i)) => {
                let idx = if *i < 0 {
                    (list.len() as i64 + i) as usize
                } else {
                    *i as usize
                };
                list.get(idx)
                    .cloned()
                    .ok_or_else(|| format!("Index {} out of range", i))
            }
            (Value::String(s), Value::Int(i)) => {
                let idx = if *i < 0 {
                    (s.len() as i64 + i) as usize
                } else {
                    *i as usize
                };
                s.chars()
                    .nth(idx)
                    .map(|c| Value::String(c.to_string()))
                    .ok_or_else(|| format!("Index {} out of range", i))
            }
            (Value::Dict(dict), Value::String(key)) => {
                dict.iter()
                    .find(|(k, _)| k == key)
                    .map(|(_, v)| v.clone())
                    .ok_or_else(|| format!("Key '{}' not found", key))
            }
            _ => Err(format!(
                "Cannot index {} with {}",
                self.type_name(),
                index.type_name()
            )),
        }
    }

    pub fn set_index(&mut self, index: &Value, value: Value) -> Result<(), String> {
        match self {
            Value::List(list) => {
                if let Value::Int(i) = index {
                    let idx = if *i < 0 {
                        (list.len() as i64 + i) as usize
                    } else {
                        *i as usize
                    };
                    if idx < list.len() {
                        list[idx] = value;
                        Ok(())
                    } else {
                        Err(format!("Index {} out of range", i))
                    }
                } else {
                    Err(format!("Cannot index list with {}", index.type_name()))
                }
            }
            Value::Dict(dict) => {
                if let Value::String(key) = index {
                    for (k, v) in dict.iter_mut() {
                        if k == key {
                            *v = value;
                            return Ok(());
                        }
                    }
                    dict.push((key.clone(), value));
                    Ok(())
                } else {
                    Err(format!("Cannot index dict with {}", index.type_name()))
                }
            }
            _ => Err(format!(
                "Cannot set index on {}",
                self.type_name()
            )),
        }
    }

    pub fn len(&self) -> Result<Value, String> {
        match self {
            Value::String(s) => Ok(Value::Int(s.len() as i64)),
            Value::List(l) => Ok(Value::Int(l.len() as i64)),
            Value::Dict(d) => Ok(Value::Int(d.len() as i64)),
            _ => Err(format!("Cannot get length of {}", self.type_name())),
        }
    }

    pub fn contains(&self, item: &Value) -> Result<bool, String> {
        match self {
            Value::String(s) => {
                if let Value::String(sub) = item {
                    Ok(s.contains(sub))
                } else {
                    Err(format!("Cannot check if {} contains {}", self.type_name(), item.type_name()))
                }
            }
            Value::List(list) => Ok(list.iter().any(|v| v.eq(item))),
            Value::Dict(dict) => {
                if let Value::String(key) = item {
                    Ok(dict.iter().any(|(k, _)| k == key))
                } else {
                    Err(format!("Dict keys must be strings"))
                }
            }
            _ => Err(format!("Cannot check membership in {}", self.type_name())),
        }
    }
}

impl std::fmt::Display for Value {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            Value::None => write!(f, "kosong"),
            Value::Bool(true) => write!(f, "benar"),
            Value::Bool(false) => write!(f, "salah"),
            Value::Int(i) => write!(f, "{}", i),
            Value::Float(fl) => write!(f, "{}", fl),
            Value::String(s) => write!(f, "{}", s),
            Value::List(items) => {
                write!(f, "[")?;
                for (i, item) in items.iter().enumerate() {
                    if i > 0 {
                        write!(f, ", ")?;
                    }
                    write!(f, "{}", item)?;
                }
                write!(f, "]")
            }
            Value::Dict(pairs) => {
                write!(f, "{{")?;
                for (i, (k, v)) in pairs.iter().enumerate() {
                    if i > 0 {
                        write!(f, ", ")?;
                    }
                    write!(f, "\"{}\": {}", k, v)?;
                }
                write!(f, "}}")
            }
            Value::Function { name, .. } => write!(f, "<fungsi {}>", name),
        }
    }
}
