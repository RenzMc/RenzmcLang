mod bytecode;
mod compiler;
mod vm;
mod value;

use pyo3::prelude::*;
use pyo3::types::{PyDict, PyList};

pub use bytecode::{Instruction, OpCode};
pub use compiler::BytecodeCompiler;
pub use value::Value;
pub use vm::VirtualMachine;

#[pyclass]
pub struct RenzmcVM {
    vm: VirtualMachine,
    compiler: BytecodeCompiler,
}

#[pymethods]
impl RenzmcVM {
    #[new]
    pub fn new() -> Self {
        RenzmcVM {
            vm: VirtualMachine::new(),
            compiler: BytecodeCompiler::new(),
        }
    }

    pub fn compile(&mut self, ast_json: &str) -> PyResult<Vec<u8>> {
        match self.compiler.compile_from_json(ast_json) {
            Ok(bytecode) => Ok(bytecode),
            Err(e) => Err(PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e)),
        }
    }

    pub fn execute(&mut self, py: Python<'_>, bytecode: Vec<u8>) -> PyResult<PyObject> {
        match self.vm.execute(&bytecode) {
            Ok(result) => value_to_pyobject(py, result),
            Err(e) => Err(PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e)),
        }
    }

    pub fn compile_and_execute(&mut self, py: Python<'_>, ast_json: &str) -> PyResult<PyObject> {
        let bytecode = self.compile(ast_json)?;
        self.execute(py, bytecode)
    }

    pub fn set_variable(&mut self, name: String, value: &Bound<'_, PyAny>) -> PyResult<()> {
        let rust_value = pyobject_to_value(value)?;
        self.vm.set_global(name, rust_value);
        Ok(())
    }

    pub fn get_variable(&self, py: Python<'_>, name: &str) -> PyResult<PyObject> {
        match self.vm.get_global(name) {
            Some(value) => value_to_pyobject(py, value.clone()),
            None => Ok(py.None()),
        }
    }

    pub fn clear(&mut self) {
        self.vm.clear();
    }

    pub fn get_stats(&self) -> PyResult<String> {
        Ok(format!(
            "{{\"instructions_executed\": {}, \"memory_used\": {}}}",
            self.vm.instructions_executed(),
            self.vm.memory_used()
        ))
    }
}

fn value_to_pyobject(py: Python<'_>, value: Value) -> PyResult<PyObject> {
    match value {
        Value::None => Ok(py.None()),
        Value::Bool(b) => Ok(b.to_object(py)),
        Value::Int(i) => Ok(i.to_object(py)),
        Value::Float(f) => Ok(f.to_object(py)),
        Value::String(s) => Ok(s.to_object(py)),
        Value::List(items) => {
            let pyitems: Vec<PyObject> = items
                .into_iter()
                .map(|item| value_to_pyobject(py, item))
                .collect::<PyResult<Vec<_>>>()?;
            Ok(PyList::new_bound(py, pyitems).to_object(py))
        }
        Value::Dict(pairs) => {
            let dict = PyDict::new_bound(py);
            for (k, v) in pairs {
                dict.set_item(k, value_to_pyobject(py, v)?)?;
            }
            Ok(dict.to_object(py))
        }
        Value::Function { .. } => Ok(py.None()),
    }
}

fn pyobject_to_value(obj: &Bound<'_, PyAny>) -> PyResult<Value> {
    if obj.is_none() {
        return Ok(Value::None);
    }
    if let Ok(b) = obj.extract::<bool>() {
        return Ok(Value::Bool(b));
    }
    if let Ok(i) = obj.extract::<i64>() {
        return Ok(Value::Int(i));
    }
    if let Ok(f) = obj.extract::<f64>() {
        return Ok(Value::Float(f));
    }
    if let Ok(s) = obj.extract::<String>() {
        return Ok(Value::String(s));
    }
    if let Ok(list) = obj.downcast::<PyList>() {
        let mut items = Vec::new();
        for item in list.iter() {
            items.push(pyobject_to_value(&item)?);
        }
        return Ok(Value::List(items));
    }
    if let Ok(dict) = obj.downcast::<PyDict>() {
        let mut pairs = Vec::new();
        for (k, v) in dict.iter() {
            let key = k.extract::<String>()?;
            let value = pyobject_to_value(&v)?;
            pairs.push((key, value));
        }
        return Ok(Value::Dict(pairs));
    }
    Ok(Value::None)
}

#[pyfunction]
fn compile_function(name: String, params: Vec<String>, body_json: String) -> PyResult<Vec<u8>> {
    let mut compiler = BytecodeCompiler::new();
    match compiler.compile_function(&name, &params, &body_json) {
        Ok(bytecode) => Ok(bytecode),
        Err(e) => Err(PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e)),
    }
}

#[pyfunction]
#[pyo3(signature = (bytecode, globals_json=None))]
fn execute_bytecode(py: Python<'_>, bytecode: Vec<u8>, globals_json: Option<String>) -> PyResult<PyObject> {
    let mut vm = VirtualMachine::new();
    
    if let Some(json) = globals_json {
        if let Ok(globals) = serde_json::from_str::<serde_json::Value>(&json) {
            if let Some(obj) = globals.as_object() {
                for (k, v) in obj {
                    vm.set_global(k.clone(), json_to_value(v));
                }
            }
        }
    }
    
    match vm.execute(&bytecode) {
        Ok(result) => value_to_pyobject(py, result),
        Err(e) => Err(PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e)),
    }
}

fn json_to_value(v: &serde_json::Value) -> Value {
    match v {
        serde_json::Value::Null => Value::None,
        serde_json::Value::Bool(b) => Value::Bool(*b),
        serde_json::Value::Number(n) => {
            if let Some(i) = n.as_i64() {
                Value::Int(i)
            } else if let Some(f) = n.as_f64() {
                Value::Float(f)
            } else {
                Value::None
            }
        }
        serde_json::Value::String(s) => Value::String(s.clone()),
        serde_json::Value::Array(arr) => {
            Value::List(arr.iter().map(json_to_value).collect())
        }
        serde_json::Value::Object(obj) => {
            Value::Dict(obj.iter().map(|(k, v)| (k.clone(), json_to_value(v))).collect())
        }
    }
}

#[pyfunction]
fn is_available() -> bool {
    true
}

#[pyfunction]
fn version() -> &'static str {
    "0.1.0"
}

#[pymodule]
fn renzmc_vm(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<RenzmcVM>()?;
    m.add_function(wrap_pyfunction!(compile_function, m)?)?;
    m.add_function(wrap_pyfunction!(execute_bytecode, m)?)?;
    m.add_function(wrap_pyfunction!(is_available, m)?)?;
    m.add_function(wrap_pyfunction!(version, m)?)?;
    Ok(())
}
