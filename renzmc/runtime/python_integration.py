"""
MIT License

Copyright (c) 2025 RenzMc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import builtins as py_builtins
import importlib
import sys

from renzmc.core.error import (
    RenzmcAttributeError,
    RenzmcImportError,
    RenzmcTypeError,
)


class SmartPythonWrapper:

    def __init__(self, obj, integration_manager):
        self._obj = obj
        self._integration = integration_manager
        self._obj_type = type(obj).__name__

    def __getattr__(self, name):
        try:
            attr = getattr(self._obj, name)
            return self._integration.convert_python_to_renzmc(attr)
        except AttributeError:
            raise RenzmcAttributeError(
                f"Objek Python '{self._obj_type}' tidak memiliki atribut '{name}'"
            )

    def __setattr__(self, name, value):
        if name.startswith("_"):
            super().__setattr__(name, value)
        else:
            try:
                setattr(
                    self._obj, name, self._integration.convert_renzmc_to_python(value)
                )
            except AttributeError:
                raise RenzmcAttributeError(
                    f"Tidak dapat mengatur atribut '{name}' pada objek Python '{self._obj_type}'"  # noqa: E501
                )

    def __call__(self, *args, **kwargs):
        if callable(self._obj):
            py_args = [self._integration.convert_renzmc_to_python(arg) for arg in args]
            py_kwargs = {
                k: self._integration.convert_renzmc_to_python(v)
                for k, v in kwargs.items()
            }
            result = self._obj(*py_args, **py_kwargs)
            return self._integration.convert_python_to_renzmc(result)
        else:
            raise RenzmcTypeError(
                f"Objek Python '{self._obj_type}' tidak dapat dipanggil"
            )

    def __getitem__(self, key):
        try:
            result = self._obj[self._integration.convert_renzmc_to_python(key)]
            return self._integration.convert_python_to_renzmc(result)
        except (KeyError, IndexError, TypeError) as e:
            raise RenzmcAttributeError(
                f"Error mengakses indeks pada objek Python: {str(e)}"
            )

    def __setitem__(self, key, value):
        try:
            self._obj[self._integration.convert_renzmc_to_python(key)] = (
                self._integration.convert_renzmc_to_python(value)
            )
        except (KeyError, IndexError, TypeError) as e:
            raise RenzmcAttributeError(
                f"Error mengatur indeks pada objek Python: {str(e)}"
            )

    def __delitem__(self, key):
        try:
            del self._obj[self._integration.convert_renzmc_to_python(key)]
        except (KeyError, IndexError, TypeError) as e:
            raise RenzmcAttributeError(
                f"Error menghapus indeks pada objek Python: {str(e)}"
            )

    def __iter__(self):
        try:
            for item in self._obj:
                yield self._integration.convert_python_to_renzmc(item)
        except TypeError:
            raise RenzmcTypeError(
                f"Objek Python '{self._obj_type}' tidak dapat diiterasi"
            )

    def __next__(self):
        try:
            result = next(self._obj)
            return self._integration.convert_python_to_renzmc(result)
        except StopIteration:
            raise StopIteration
        except TypeError:
            raise RenzmcTypeError(f"Objek Python '{self._obj_type}' bukan iterator")

    def __len__(self):
        try:
            return len(self._obj)
        except TypeError:
            raise RenzmcTypeError(
                f"Objek Python '{self._obj_type}' tidak memiliki panjang"
            )

    def __contains__(self, item):
        try:
            return self._integration.convert_renzmc_to_python(item) in self._obj
        except TypeError:
            return False

    def __enter__(self):
        try:
            result = self._obj.__enter__()
            return self._integration.convert_python_to_renzmc(result)
        except AttributeError:
            raise RenzmcTypeError(
                f"Objek Python '{self._obj_type}' tidak mendukung context manager"
            )

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            return self._obj.__exit__(exc_type, exc_val, exc_tb)
        except AttributeError:
            raise RenzmcTypeError(
                f"Objek Python '{self._obj_type}' tidak mendukung context manager"
            )

    def __eq__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            return self._obj == other_py
        except (TypeError, ValueError, AttributeError):
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            return self._obj < other_py
        except TypeError:
            raise RenzmcTypeError(
                f"Tidak dapat membandingkan objek Python '{self._obj_type}'"
            )

    def __le__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            return self._obj <= other_py
        except TypeError:
            raise RenzmcTypeError(
                f"Tidak dapat membandingkan objek Python '{self._obj_type}'"
            )

    def __gt__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            return self._obj > other_py
        except TypeError:
            raise RenzmcTypeError(
                f"Tidak dapat membandingkan objek Python '{self._obj_type}'"
            )

    def __ge__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            return self._obj >= other_py
        except TypeError:
            raise RenzmcTypeError(
                f"Tidak dapat membandingkan objek Python '{self._obj_type}'"
            )

    def __add__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj + other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(
                f"Tidak dapat menambahkan pada objek Python '{self._obj_type}'"
            )

    def __sub__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj - other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(
                f"Tidak dapat mengurangi pada objek Python '{self._obj_type}'"
            )

    def __mul__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj * other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(
                f"Tidak dapat mengalikan pada objek Python '{self._obj_type}'"
            )

    def __truediv__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj / other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(
                f"Tidak dapat membagi pada objek Python '{self._obj_type}'"
            )

    def __mod__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj % other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(
                f"Tidak dapat modulo pada objek Python '{self._obj_type}'"
            )

    def __pow__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj**other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(
                f"Tidak dapat pangkat pada objek Python '{self._obj_type}'"
            )

    def __bool__(self):
        try:
            return bool(self._obj)
        except (TypeError, ValueError):
            return True

    def __hash__(self):
        try:
            return hash(self._obj)
        except TypeError:
            raise RenzmcTypeError(
                f"Objek Python '{self._obj_type}' tidak dapat di-hash"
            )

    def __str__(self):
        try:
            return str(self._obj)
        except (TypeError, ValueError):
            return f"SmartWrapper({self._obj_type})"

    def __repr__(self):
        try:
            return repr(self._obj)
        except (TypeError, ValueError):
            return f"<SmartPythonWrapper for {self._obj_type}>"

    def __dir__(self):
        try:
            return dir(self._obj)
        except (TypeError, AttributeError):
            return []

    def __format__(self, format_spec):
        try:
            return format(self._obj, format_spec)
        except (TypeError, ValueError):
            return str(self._obj)

    def __sizeof__(self):
        try:
            return self._obj.__sizeof__()
        except (TypeError, AttributeError):
            return object.__sizeof__(self)

    def __reduce__(self):
        try:
            return self._obj.__reduce__()
        except (TypeError, AttributeError):
            raise RenzmcTypeError(
                f"Objek Python '{self._obj_type}' tidak dapat di-pickle"
            )

    def __reduce_ex__(self, protocol):
        try:
            return self._obj.__reduce_ex__(protocol)
        except (TypeError, AttributeError):
            raise RenzmcTypeError(
                f"Objek Python '{self._obj_type}' tidak dapat di-pickle dengan protocol {protocol}"  # noqa: E501
            )

    def __copy__(self):
        try:
            import copy

            result = copy.copy(self._obj)
            return self._integration.convert_python_to_renzmc(result)
        except (TypeError, AttributeError) as e:
            raise RenzmcTypeError(
                f"Objek Python '{self._obj_type}' tidak dapat di-copy: {e}"
            )

    def __deepcopy__(self, memo):
        try:
            import copy

            result = copy.deepcopy(self._obj, memo)
            return self._integration.convert_python_to_renzmc(result)
        except (TypeError, AttributeError) as e:
            raise RenzmcTypeError(
                f"Objek Python '{self._obj_type}' tidak dapat di-deepcopy: {e}"
            )

    def __await__(self):
        try:
            if hasattr(self._obj, "__await__"):
                return self._obj.__await__()
            else:
                raise RenzmcTypeError(
                    f"Objek Python '{self._obj_type}' tidak mendukung await"
                )
        except Exception as e:
            raise RenzmcTypeError(f"Error dalam await: {str(e)}")

    def __aiter__(self):
        try:
            if hasattr(self._obj, "__aiter__"):
                result = self._obj.__aiter__()
                return self._integration.convert_python_to_renzmc(result)
            else:
                raise RenzmcTypeError(
                    f"Objek Python '{self._obj_type}' tidak mendukung async iteration"
                )
        except Exception as e:
            raise RenzmcTypeError(f"Error dalam async iteration: {str(e)}")

    def __anext__(self):
        try:
            if hasattr(self._obj, "__anext__"):
                result = self._obj.__anext__()
                return self._integration.convert_python_to_renzmc(result)
            else:
                raise RenzmcTypeError(
                    f"Objek Python '{self._obj_type}' tidak mendukung async next"
                )
        except Exception as e:
            raise RenzmcTypeError(f"Error dalam async next: {str(e)}")

    def __aenter__(self):
        try:
            if hasattr(self._obj, "__aenter__"):
                result = self._obj.__aenter__()
                return self._integration.convert_python_to_renzmc(result)
            else:
                raise RenzmcTypeError(
                    f"Objek Python '{self._obj_type}' tidak mendukung async context manager"  # noqa: E501
                )
        except Exception as e:
            raise RenzmcTypeError(f"Error dalam async context manager entry: {str(e)}")

    def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            if hasattr(self._obj, "__aexit__"):
                return self._obj.__aexit__(exc_type, exc_val, exc_tb)
            else:
                raise RenzmcTypeError(
                    f"Objek Python '{self._obj_type}' tidak mendukung async context manager"  # noqa: E501
                )
        except Exception as e:
            raise RenzmcTypeError(f"Error dalam async context manager exit: {str(e)}")

    def __and__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj & other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(
                f"Tidak dapat melakukan operasi AND pada objek Python '{self._obj_type}'"  # noqa: E501
            )

    def __or__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj | other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(
                f"Tidak dapat melakukan operasi OR pada objek Python '{self._obj_type}'"
            )

    def __xor__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj ^ other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(
                f"Tidak dapat melakukan operasi XOR pada objek Python '{self._obj_type}'"  # noqa: E501
            )

    def __lshift__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj << other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(
                f"Tidak dapat melakukan left shift pada objek Python '{self._obj_type}'"
            )

    def __rshift__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj >> other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(
                f"Tidak dapat melakukan right shift pada objek Python '{self._obj_type}'"  # noqa: E501
            )

    def __floordiv__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj // other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(
                f"Tidak dapat melakukan floor division pada objek Python '{self._obj_type}'"  # noqa: E501
            )

    def __divmod__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = divmod(self._obj, other_py)
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(
                f"Tidak dapat melakukan divmod pada objek Python '{self._obj_type}'"
            )

    def __matmul__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj @ other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(
                f"Tidak dapat melakukan matrix multiplication pada objek Python '{self._obj_type}'"  # noqa: E501
            )

    def __radd__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = other_py + self._obj
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(
                f"Tidak dapat menambahkan objek Python '{self._obj_type}' dari kanan"
            )

    def __rsub__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = other_py - self._obj
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(
                f"Tidak dapat mengurangi objek Python '{self._obj_type}' dari kanan"
            )

    def __rmul__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = other_py * self._obj
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(
                f"Tidak dapat mengalikan objek Python '{self._obj_type}' dari kanan"
            )

    def __rtruediv__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = other_py / self._obj
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(
                f"Tidak dapat membagi objek Python '{self._obj_type}' dari kanan"
            )


class PythonModule:

    def __init__(self, module):
        self._module = module
        self._module_name = module.__name__
        self._cached_attributes = {}
        self._submodule_cache = {}

    def __getattr__(self, name):
        try:
            attr = getattr(self._module, name)
            if hasattr(attr, "__name__") and hasattr(attr, "__file__"):
                return PythonModule(attr)
            return attr
        except AttributeError:
            raise RenzmcAttributeError(
                f"Modul Python '{self._module_name}' tidak memiliki atribut '{name}'"
            )

    def __getitem__(self, key):
        try:
            if hasattr(self._module, "__getitem__"):
                return self._module[key]
            else:
                raise RenzmcAttributeError(
                    f"Modul Python '{self._module_name}' tidak mendukung indexing"
                )
        except (KeyError, IndexError, TypeError) as e:
            raise RenzmcAttributeError(
                f"Error mengakses indeks '{key}' pada modul '{self._module_name}': {str(e)}"  # noqa: E501
            )

    def __setitem__(self, key, value):
        try:
            if hasattr(self._module, "__setitem__"):
                self._module[key] = value
            else:
                raise RenzmcAttributeError(
                    f"Modul Python '{self._module_name}' tidak mendukung assignment"
                )
        except (KeyError, IndexError, TypeError) as e:
            raise RenzmcAttributeError(
                f"Error mengatur indeks '{key}' pada modul '{self._module_name}': {str(e)}"  # noqa: E501
            )

    def __iter__(self):
        if hasattr(self._module, "__iter__"):
            return iter(self._module)
        else:
            raise RenzmcTypeError(
                f"Modul Python '{self._module_name}' tidak dapat diiterasi"
            )

    def __len__(self):
        if hasattr(self._module, "__len__"):
            return len(self._module)
        else:
            raise RenzmcTypeError(
                f"Modul Python '{self._module_name}' tidak memiliki panjang"
            )

    def __call__(self, *args, **kwargs):
        if callable(self._module):
            return self._module(*args, **kwargs)
        raise RenzmcTypeError(
            f"Modul Python '{self._module_name}' tidak dapat dipanggil"
        )

    def __repr__(self):
        return f"<PythonModule '{self._module_name}'>"

    def __str__(self):
        return f"PythonModule({self._module_name})"

    def __dir__(self):
        return dir(self._module)


class PythonIntegration:

    def __init__(self):
        self.imported_modules = {}
        self.module_aliases = {}
        self.from_imports = {}

    def setup_python_builtins(self, global_scope):
        for name in dir(py_builtins):
            if not name.startswith("_"):
                global_scope[f"py_{name}"] = getattr(py_builtins, name)

    def import_python_module(self, module_name, alias=None, from_items=None):
        try:
            if module_name in self.imported_modules:
                module = self.imported_modules[module_name]
            else:
                module = importlib.import_module(module_name)
                self.imported_modules[module_name] = module
            if from_items:
                imported_items = {}
                for item in from_items:
                    if hasattr(module, item):
                        imported_items[item] = getattr(module, item)
                    else:
                        raise RenzmcImportError(
                            f"Tidak dapat mengimpor '{item}' dari modul Python '{module_name}'"  # noqa: E501
                        )
                self.from_imports[module_name] = imported_items
                return imported_items
            wrapped_module = PythonModule(module)
            if alias:
                self.module_aliases[alias] = wrapped_module
            return wrapped_module
        except ImportError as e:
            raise RenzmcImportError(
                f"Tidak dapat mengimpor modul Python '{module_name}': {str(e)}"
            )
        except Exception as e:
            raise RenzmcImportError(
                f"Error saat mengimpor modul Python '{module_name}': {str(e)}"
            )

    def get_module_attribute(self, module_name, attribute_name):
        if module_name in self.module_aliases:
            module = self.module_aliases[module_name]._module
        elif module_name in self.imported_modules:
            module = self.imported_modules[module_name]
        else:
            raise RenzmcImportError(f"Modul Python '{module_name}' belum diimpor")
        try:
            return getattr(module, attribute_name)
        except AttributeError:
            raise RenzmcAttributeError(
                f"Modul Python '{module_name}' tidak memiliki atribut '{attribute_name}'"  # noqa: E501
            )

    def call_python_function(self, func, *args, **kwargs):
        try:
            if callable(func):
                return func(*args, **kwargs)
            else:
                raise RenzmcTypeError(f"Objek '{func}' tidak dapat dipanggil")
        except Exception as e:
            raise RenzmcTypeError(f"Error dalam pemanggilan fungsi Python: {str(e)}")

    def create_python_object(self, class_obj, *args, **kwargs):
        try:
            if isinstance(class_obj, type):
                return class_obj(*args, **kwargs)
            else:
                raise RenzmcTypeError(f"'{class_obj}' bukan kelas Python yang valid")
        except Exception as e:
            raise RenzmcTypeError(f"Error saat membuat objek Python: {str(e)}")

    def list_module_attributes(self, module_name):
        if module_name in self.module_aliases:
            module = self.module_aliases[module_name]._module
        elif module_name in self.imported_modules:
            module = self.imported_modules[module_name]
        else:
            raise RenzmcImportError(f"Modul Python '{module_name}' belum diimpor")
        return [attr for attr in dir(module) if not attr.startswith("_")]

    def get_python_help(self, obj):
        try:
            import pydoc

            return pydoc.render_doc(obj)
        except Exception:
            return f"Tidak dapat mendapatkan bantuan untuk objek: {obj}"

    def install_package(self, package_name):
        try:
            import subprocess

            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", package_name],
                capture_output=True,
                text=True,
            )
            return result.returncode == 0
        except Exception:
            return False

    def get_all_python_modules(self):
        try:
            import pkgutil

            return [name for _, name, _ in pkgutil.iter_modules()]
        except Exception:
            return []

    def auto_import_on_demand(self, module_name):
        try:
            if module_name not in self.imported_modules:
                module = importlib.import_module(module_name)
                self.imported_modules[module_name] = module
                return PythonModule(module)
            else:
                return PythonModule(self.imported_modules[module_name])
        except ImportError:
            return None

    def import_all_from_module(self, module_name):
        try:
            if module_name in self.imported_modules:
                module = self.imported_modules[module_name]
            else:
                module = importlib.import_module(module_name)
                self.imported_modules[module_name] = module
            all_attrs = {}
            if hasattr(module, "__all__"):
                for name in module.__all__:
                    if hasattr(module, name):
                        all_attrs[name] = self.convert_python_to_renzmc(
                            getattr(module, name)
                        )
            else:
                for name in dir(module):
                    if not name.startswith("_"):
                        all_attrs[name] = self.convert_python_to_renzmc(
                            getattr(module, name)
                        )
            return all_attrs
        except ImportError as e:
            raise RenzmcImportError(
                f"Tidak dapat mengimpor semua dari modul Python '{module_name}': {str(e)}"  # noqa: E501
            )
        except Exception as e:
            raise RenzmcImportError(
                f"Error saat mengimpor semua dari modul Python '{module_name}': {str(e)}"  # noqa: E501
            )

    def reload_module(self, module_name):
        try:
            if module_name in self.imported_modules:
                module = importlib.reload(self.imported_modules[module_name])
                self.imported_modules[module_name] = module
                return PythonModule(module)
            else:
                raise RenzmcImportError(f"Modul Python '{module_name}' belum diimpor")
        except Exception as e:
            raise RenzmcImportError(
                f"Error saat reload modul Python '{module_name}': {str(e)}"
            )

    def get_module_path(self, module_name):
        if module_name in self.imported_modules:
            module = self.imported_modules[module_name]
            if hasattr(module, "__file__"):
                return module.__file__
            else:
                return f"<built-in module '{module_name}'>"
        else:
            raise RenzmcImportError(f"Modul Python '{module_name}' belum diimpor")

    def list_available_modules(self):
        try:
            import pkgutil

            modules = []
            for importer, modname, ispkg in pkgutil.iter_modules():
                modules.append(modname)
            return sorted(modules)
        except Exception:
            return []

    def check_module_available(self, module_name):
        try:
            importlib.util.find_spec(module_name)
            return True
        except (ImportError, ModuleNotFoundError, ValueError):
            return False

    def get_module_version(self, module_name):
        if module_name in self.imported_modules:
            module = self.imported_modules[module_name]
            for attr in ["__version__", "VERSION", "version"]:
                if hasattr(module, attr):
                    return str(getattr(module, attr))
            return "Unknown"
        else:
            raise RenzmcImportError(f"Modul Python '{module_name}' belum diimpor")

    def import_submodule(self, parent_module, submodule_name):
        try:
            full_name = f"{parent_module}.{submodule_name}"
            if full_name in self.imported_modules:
                module = self.imported_modules[full_name]
            else:
                module = importlib.import_module(full_name)
                self.imported_modules[full_name] = module
            return PythonModule(module)
        except ImportError as e:
            raise RenzmcImportError(
                f"Tidak dapat mengimpor submodul '{submodule_name}' dari '{parent_module}': {str(e)}"  # noqa: E501
            )

    def execute_python_code(self, code_string, local_vars=None):
        try:
            if local_vars is None:
                local_vars = {}
            exec(code_string, globals(), local_vars)
            converted_vars = {}
            for key, value in local_vars.items():
                if not key.startswith("_"):
                    converted_vars[key] = self.convert_python_to_renzmc(value)
            return converted_vars
        except Exception as e:
            raise Exception(f"Error saat menjalankan kode Python: {str(e)}")

    def evaluate_python_expression(self, expression):
        try:
            result = eval(expression)
            return self.convert_python_to_renzmc(result)
        except Exception as e:
            raise Exception(f"Error saat evaluasi ekspresi Python: {str(e)}")

    def convert_python_to_renzmc(self, obj):  # noqa: C901
        if obj is None:
            return None
        if isinstance(obj, (int, float, str, bool, bytes)):
            return obj
        if self._is_module_object(obj):
            return PythonModule(obj)
        if isinstance(obj, type):
            return self.create_smart_wrapper(obj)
        if hasattr(obj, "__iter__") and hasattr(obj, "__next__"):
            return self.create_smart_wrapper(obj)
        if hasattr(obj, "__iter__") and (not isinstance(obj, (str, bytes))):
            try:
                if isinstance(obj, dict):
                    return {
                        self.convert_python_to_renzmc(k): self.convert_python_to_renzmc(
                            v
                        )
                        for k, v in obj.items()
                    }
                elif isinstance(obj, list):
                    return [self.convert_python_to_renzmc(item) for item in obj]
                elif isinstance(obj, tuple):
                    return tuple((self.convert_python_to_renzmc(item) for item in obj))
                elif isinstance(obj, set):
                    return {self.convert_python_to_renzmc(item) for item in obj}
                else:
                    return self.create_smart_wrapper(obj)
            except (TypeError, RecursionError):
                return self.create_smart_wrapper(obj)
        if callable(obj) and (not isinstance(obj, type)):

            def enhanced_wrapper(*args, **kwargs):
                try:
                    py_args = [self.convert_renzmc_to_python(arg) for arg in args]
                    py_kwargs = {
                        k: self.convert_renzmc_to_python(v) for k, v in kwargs.items()
                    }
                    result = obj(*py_args, **py_kwargs)
                    return self.convert_python_to_renzmc(result)
                except Exception as e:
                    raise RenzmcTypeError(
                        f"Error dalam pemanggilan fungsi Python: {str(e)}"
                    )

            try:
                enhanced_wrapper.__name__ = getattr(obj, "__name__", "python_function")
                enhanced_wrapper.__doc__ = getattr(obj, "__doc__", None)
            except (TypeError, AttributeError):
                pass
            return enhanced_wrapper
        if hasattr(obj, "__dict__") or hasattr(obj, "__getattr__"):
            return self.create_smart_wrapper(obj)
        special_methods = [
            "__getitem__",
            "__setitem__",
            "__len__",
            "__contains__",
            "__enter__",
            "__exit__",
            "__add__",
            "__sub__",
            "__mul__",
            "__call__",
            "__getattribute__",
            "__delattr__",
            "__hash__",
            "__repr__",
            "__str__",
            "__bool__",
            "__format__",
            "__sizeof__",
        ]
        if any((hasattr(obj, method) for method in special_methods)):
            return self.create_smart_wrapper(obj)
        if self._is_coroutine_or_async(obj):
            return self.create_smart_wrapper(obj)
        if self._is_file_like(obj):
            return self.create_smart_wrapper(obj)
        if isinstance(obj, BaseException):
            return self.create_smart_wrapper(obj)
        try:
            import json

            json.dumps(obj)
            return obj
        except (TypeError, ValueError):
            return self.create_smart_wrapper(obj)

    def convert_renzmc_to_python(self, obj):  # noqa: C901
        if obj is None:
            return None
        if isinstance(obj, (int, float, str, bool, bytes)):
            return obj
        if isinstance(obj, SmartPythonWrapper):
            return obj._obj
        if isinstance(obj, PythonModule):
            return obj._module
        if hasattr(obj, "__iter__") and (not isinstance(obj, (str, bytes))):
            try:
                if isinstance(obj, dict):
                    return {
                        self.convert_renzmc_to_python(k): self.convert_renzmc_to_python(
                            v
                        )
                        for k, v in obj.items()
                    }
                elif isinstance(obj, list):
                    return [self.convert_renzmc_to_python(item) for item in obj]
                elif isinstance(obj, tuple):
                    return tuple((self.convert_renzmc_to_python(item) for item in obj))
                elif isinstance(obj, set):
                    return {self.convert_renzmc_to_python(item) for item in obj}
                else:
                    try:
                        return [self.convert_renzmc_to_python(item) for item in obj]
                    except (TypeError, AttributeError):
                        return obj
            except (TypeError, RecursionError):
                return obj
        if callable(obj):
            if hasattr(obj, "__name__") and obj.__name__ == "enhanced_wrapper":
                return obj
            return obj
        return obj

    def create_smart_wrapper(self, obj):
        return SmartPythonWrapper(obj, self)

    def enable_star_imports(self, module_name, global_scope):
        try:
            module_wrapper = self.import_python_module(module_name)
            imported_count = 0
            if isinstance(module_wrapper, PythonModule):
                actual_module = module_wrapper._module
            elif isinstance(module_wrapper, dict):
                for key, value in module_wrapper.items():
                    if isinstance(value, PythonModule):
                        actual_module = value._module
                        break
                else:
                    return 0
            else:
                actual_module = module_wrapper
            if hasattr(actual_module, "__all__"):
                items = actual_module.__all__
            else:
                items = [
                    name for name in dir(actual_module) if not name.startswith("_")
                ]
            for item_name in items:
                if hasattr(actual_module, item_name):
                    global_scope[item_name] = self.convert_python_to_renzmc(
                        getattr(actual_module, item_name)
                    )
                    imported_count += 1
            return imported_count
        except Exception:
            return 0

    def _is_module_object(self, obj):
        if hasattr(obj, "__name__") and hasattr(obj, "__file__"):
            return True
        if hasattr(obj, "__name__") and hasattr(obj, "__package__"):
            return True
        import types as module_types

        return isinstance(obj, module_types.ModuleType)

    def _is_coroutine_or_async(self, obj):
        import inspect as inspect_module

        return (
            inspect_module.iscoroutine(obj)
            or inspect_module.iscoroutinefunction(obj)
            or inspect_module.isasyncgenfunction(obj)
            or inspect_module.isasyncgen(obj)
            or hasattr(obj, "__await__")
            or hasattr(obj, "__aenter__")
            or hasattr(obj, "__aexit__")
        )

    def _is_file_like(self, obj):
        file_methods = ["read", "write", "close", "flush", "seek", "tell"]
        return any((hasattr(obj, method) for method in file_methods))

    def enhance_smart_wrapper_compatibility(self, wrapper_obj):
        if not isinstance(wrapper_obj, SmartPythonWrapper):
            return wrapper_obj
        original_obj = wrapper_obj._obj
        special_methods = [
            "__format__",
            "__sizeof__",
            "__reduce__",
            "__reduce_ex__",
            "__getstate__",
            "__setstate__",
            "__copy__",
            "__deepcopy__",
            "__enter__",
            "__exit__",
            "__aenter__",
            "__aexit__",
            "__await__",
            "__aiter__",
            "__anext__",
        ]
        for method_name in special_methods:
            if hasattr(original_obj, method_name) and (
                not hasattr(wrapper_obj, method_name)
            ):

                def create_method_wrapper(method):

                    def wrapper_method(*args, **kwargs):
                        try:
                            result = method(*args, **kwargs)
                            return self.convert_python_to_renzmc(result)
                        except Exception as e:
                            raise RenzmcTypeError(
                                f"Error dalam method {method.__name__}: {str(e)}"
                            )

                    return wrapper_method

                setattr(
                    wrapper_obj,
                    method_name,
                    create_method_wrapper(getattr(original_obj, method_name)),
                )
        return wrapper_obj
