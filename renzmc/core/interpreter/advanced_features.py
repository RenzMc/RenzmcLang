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

"""
RenzmcLang Interpreter Advanced Features Module

This module contains advanced features like decorators, generators, and async.
"""

import asyncio


class AdvancedFeaturesMixin:
    """
    Mixin class for advanced features functionality.

    Provides decorators, context managers, generators, and async support.
    """

    def _create_decorator(self, name, decorator_func):
        """
        Create a decorator.

        Args:
            name: Decorator name
            decorator_func: Decorator function

        Returns:
            Created decorator
        """
        return self.advanced_features.create_decorator(name, decorator_func)

    def _apply_decorator(self, decorator_name, func):
        """
        Apply a decorator to a function.

        Args:
            decorator_name: Name of the decorator
            func: Function to decorate

        Returns:
            Decorated function
        """
        return self.advanced_features.apply_decorator(decorator_name, func)

    def _create_context_manager(self, name, enter_func=None, exit_func=None):
        """
        Create a context manager.

        Args:
            name: Context manager name
            enter_func: Enter function
            exit_func: Exit function

        Returns:
            Created context manager
        """
        return self.advanced_features.create_context_manager(
            name, enter_func, exit_func
        )

    def _use_context_manager(self, context_manager, action_func):
        """
        Use a context manager.

        Args:
            context_manager: The context manager
            action_func: Function to execute in context

        Returns:
            Result of action_func

        Raises:
            RuntimeError: If context manager usage fails
        """
        try:
            with context_manager:
                return action_func()
        except Exception as e:
            raise RuntimeError(f"Error menggunakan context manager: {str(e)}")

    def _create_advanced_generator(self, name, generator_func, *args, **kwargs):
        """
        Create an advanced generator.

        Args:
            name: Generator name
            generator_func: Generator function
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            Created generator
        """
        return self.advanced_features.create_generator(
            name, generator_func, *args, **kwargs
        )

    def _create_async_function(self, name, func):
        """
        Create an async function.

        Args:
            name: Function name
            func: Function to make async

        Returns:
            Async function
        """
        return self.advanced_features.create_async_function(name, func)

    def _list_advanced_features(self):
        """
        List all advanced features.

        Returns:
            List of feature names
        """
        return self.advanced_features.list_features()

    def _create_generator(self, func, *args, **kwargs):
        """
        Create a generator from a function.

        Args:
            func: Generator function
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            Generator object

        Raises:
            TypeError: If func is not callable
        """
        if callable(func):
            return func(*args, **kwargs)
        else:
            raise TypeError(f"Objek '{func}' tidak dapat dipanggil sebagai generator")

    def _run_async_function(self, coro):
        """
        Run an async function.

        Args:
            coro: Coroutine to run

        Returns:
            Result of coroutine

        Raises:
            TypeError: If coro is not a coroutine
        """
        if asyncio.iscoroutine(coro):
            return self.loop.run_until_complete(coro)
        else:
            raise TypeError(f"Objek '{coro}' bukan coroutine")

    def _wait_all_async(self, coros):
        """
        Wait for all async functions to complete.

        Args:
            coros: List of coroutines

        Returns:
            List of results

        Raises:
            TypeError: If any item is not a coroutine
        """
        if all((asyncio.iscoroutine(coro) for coro in coros)):
            return self.loop.run_until_complete(asyncio.gather(*coros))
        else:
            raise TypeError("Semua objek harus berupa coroutine")

    def _list_to_generator(self, lst):
        """
        Convert a list to a generator.

        Args:
            lst: Iterable to convert

        Returns:
            Generator object

        Raises:
            TypeError: If lst is not iterable
        """
        if hasattr(lst, "__iter__"):

            def gen():
                for item in lst:
                    yield item

            return gen()
        else:
            raise TypeError(f"Objek '{lst}' tidak dapat diiterasi")
