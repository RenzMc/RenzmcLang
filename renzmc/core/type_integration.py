from renzmc.core.type_system import TypeChecker, TypeValidator, BaseType
from renzmc.core.error import RuntimeError as RenzmcRuntimeError


class TypeIntegrationMixin:

    def _init_type_system(self, strict_mode=False):
        self.type_checker = TypeChecker(strict_mode=strict_mode)
        self.type_validator = TypeValidator()
        self.type_checking_enabled = True

    def _check_variable_type(self, var_name, value, type_hint):
        if not self.type_checking_enabled:
            return

        if not type_hint:
            return

        type_hint_str = type_hint.type_name if hasattr(type_hint, 'type_name') else str(type_hint)

        is_valid, error_msg = self.type_checker.check_variable_assignment(
            var_name, value, type_hint_str
        )

        if not is_valid:
            raise RenzmcRuntimeError(error_msg)

    def _check_function_parameters(self, func_name, params, param_types, args, kwargs):
        if not self.type_checking_enabled:
            return

        if not param_types:
            return

        param_values = {}
        for i, arg in enumerate(args):
            if i < len(params):
                param_values[params[i]] = arg

        for param_name, value in kwargs.items():
            param_values[param_name] = value

        for param_name, value in param_values.items():
            if param_name in param_types:
                type_hint = param_types[param_name]
                type_hint_str = type_hint.type_name if hasattr(type_hint, 'type_name') else str(type_hint)

                is_valid, error_msg = self.type_checker.check_function_parameter(
                    param_name, value, type_hint_str, func_name
                )

                if not is_valid:
                    raise RenzmcRuntimeError(error_msg)

    def _check_function_return(self, func_name, return_value, return_type):
        if not self.type_checking_enabled:
            return

        if not return_type:
            return

        if return_value is None:
            return

        type_hint_str = return_type.type_name if hasattr(return_type, 'type_name') else str(return_type)

        is_valid, error_msg = self.type_checker.check_function_return(
            return_value, type_hint_str, func_name
        )

        if not is_valid:
            raise RenzmcRuntimeError(error_msg)

    def enable_type_checking(self):
        self.type_checking_enabled = True

    def disable_type_checking(self):
        self.type_checking_enabled = False

    def set_strict_mode(self, strict: bool):
        if hasattr(self, 'type_checker'):
            self.type_checker.strict_mode = strict
