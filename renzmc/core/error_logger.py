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
RenzmcLang Advanced Error Logger Module

Provides comprehensive error logging with structured logging, file rotation,
error statistics, and analytics capabilities.
"""

import json
import logging
import os
import traceback
from collections import defaultdict
from datetime import datetime
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any, Dict, List, Optional

from renzmc.core.error_catalog import suggest_error_code


class ErrorLogger:
    """Advanced error logger with structured logging and analytics."""

    def __init__(
        self,
        log_dir: Optional[str] = None,
        max_bytes: int = 10 * 1024 * 1024,  # 10MB
        backup_count: int = 5,
        enable_console: bool = True,
        enable_file: bool = True,
    ):
        """
        Initialize error logger.

        Args:
            log_dir: Directory for log files (default: ~/.renzmc/logs)
            max_bytes: Maximum size of log file before rotation
            backup_count: Number of backup files to keep
            enable_console: Enable console logging
            enable_file: Enable file logging
        """
        self.log_dir = log_dir or self._get_default_log_dir()
        self.max_bytes = max_bytes
        self.backup_count = backup_count
        self.enable_console = enable_console
        self.enable_file = enable_file

        # Create log directory if it doesn't exist
        Path(self.log_dir).mkdir(parents=True, exist_ok=True)

        # Initialize loggers
        self.error_logger = self._setup_logger("renzmc.errors", "errors.log", logging.ERROR)
        self.warning_logger = self._setup_logger("renzmc.warnings", "warnings.log", logging.WARNING)
        self.debug_logger = self._setup_logger("renzmc.debug", "debug.log", logging.DEBUG)

        # Error statistics
        self.error_stats = defaultdict(int)
        self.error_history: List[Dict[str, Any]] = []

    def _get_default_log_dir(self) -> str:
        """Get default log directory."""
        home = Path.home()
        log_dir = home / ".renzmc" / "logs"
        return str(log_dir)

    def _setup_logger(self, name: str, filename: str, level: int) -> logging.Logger:
        """
        Setup a logger with file and console handlers.

        Args:
            name: Logger name
            filename: Log file name
            level: Logging level

        Returns:
            Configured logger
        """
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        logger.handlers.clear()

        # File handler with rotation
        if self.enable_file:
            log_file = os.path.join(self.log_dir, filename)
            file_handler = RotatingFileHandler(
                log_file,
                maxBytes=self.max_bytes,
                backupCount=self.backup_count,
                encoding="utf-8",
            )
            file_handler.setLevel(level)
            file_formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)

        # Console handler
        if self.enable_console and level >= logging.WARNING:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(level)
            console_formatter = logging.Formatter("%(levelname)s: %(message)s")
            console_handler.setFormatter(console_formatter)
            logger.addHandler(console_handler)

        return logger

    def log_error(
        self,
        error: Exception,
        error_code: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
        source_code: Optional[str] = None,
        filename: Optional[str] = None,
    ) -> str:
        """
        Log an error with full context and analytics.

        Args:
            error: The exception object
            error_code: Optional error code (will be auto-detected if None)
            context: Additional context information
            source_code: Source code where error occurred
            filename: Filename where error occurred

        Returns:
            Error code assigned to this error
        """
        # Auto-detect error code if not provided
        if error_code is None:
            error_type = type(error).__name__
            error_message = str(error)
            error_code = suggest_error_code(error_type, error_message)
            if error_code is None:
                error_code = "RMC-R001"  # Generic runtime error

        # Extract clean error message
        error_message = str(error)
        if hasattr(error, "args") and error.args:
            error_message = error.args[0] if isinstance(error.args[0], str) else str(error.args[0])
            # Unwrap nested tuples
            while isinstance(error_message, tuple) and len(error_message) >= 1:
                error_message = error_message[0]
            error_message = str(error_message)

        # Extract line and column if available
        line = None
        column = None
        if hasattr(error, "args") and len(error.args) >= 3:
            if isinstance(error.args[1], int):
                line = error.args[1]
            if isinstance(error.args[2], int):
                column = error.args[2]
        if line is None:
            line = getattr(error, "line", None)
        if column is None:
            column = getattr(error, "column", None)

        # Build error record
        error_record = {
            "timestamp": datetime.now().isoformat(),
            "error_code": error_code,
            "error_type": type(error).__name__,
            "error_message": error_message,
            "filename": filename or "<unknown>",
            "line": line,
            "column": column,
            "traceback": traceback.format_exc(),
            "context": context or {},
        }

        # Add source code snippet if available
        if source_code and line is not None:
            error_record["source_snippet"] = self._get_source_snippet(source_code, line)

        # Log to file
        self.error_logger.error(json.dumps(error_record, ensure_ascii=False))

        # Update statistics
        self.error_stats[error_code] += 1
        self.error_history.append(error_record)

        # Keep only last 1000 errors in memory
        if len(self.error_history) > 1000:
            self.error_history = self.error_history[-1000:]

        return error_code

    def log_warning(
        self,
        message: str,
        context: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Log a warning message.

        Args:
            message: Warning message
            context: Additional context information
        """
        warning_record = {
            "timestamp": datetime.now().isoformat(),
            "message": message,
            "context": context or {},
        }
        self.warning_logger.warning(json.dumps(warning_record, ensure_ascii=False))

    def log_debug(
        self,
        message: str,
        context: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Log a debug message.

        Args:
            message: Debug message
            context: Additional context information
        """
        debug_record = {
            "timestamp": datetime.now().isoformat(),
            "message": message,
            "context": context or {},
        }
        self.debug_logger.debug(json.dumps(debug_record, ensure_ascii=False))

    def _get_source_snippet(self, source_code: str, line: int, context_lines: int = 3) -> Dict[str, Any]:
        """
        Get source code snippet around error line.

        Args:
            source_code: Full source code
            line: Line number where error occurred
            context_lines: Number of context lines to include

        Returns:
            Dictionary with source snippet information
        """
        lines = source_code.split("\n")
        start_line = max(0, line - context_lines - 1)
        end_line = min(len(lines), line + context_lines)

        snippet_lines = []
        for i in range(start_line, end_line):
            snippet_lines.append(
                {
                    "line_number": i + 1,
                    "content": lines[i],
                    "is_error_line": i + 1 == line,
                }
            )

        return {
            "start_line": start_line + 1,
            "end_line": end_line,
            "lines": snippet_lines,
        }

    def get_error_statistics(self) -> Dict[str, Any]:
        """
        Get error statistics.

        Returns:
            Dictionary with error statistics
        """
        total_errors = sum(self.error_stats.values())
        most_common = sorted(self.error_stats.items(), key=lambda x: x[1], reverse=True)[:10]

        return {
            "total_errors": total_errors,
            "unique_error_codes": len(self.error_stats),
            "most_common_errors": [{"code": code, "count": count} for code, count in most_common],
            "error_breakdown": dict(self.error_stats),
        }

    def get_recent_errors(self, count: int = 10) -> List[Dict[str, Any]]:
        """
        Get recent errors.

        Args:
            count: Number of recent errors to return

        Returns:
            List of recent error records
        """
        return self.error_history[-count:]

    def export_statistics(self, output_file: str) -> None:
        """
        Export error statistics to JSON file.

        Args:
            output_file: Path to output file
        """
        stats = self.get_error_statistics()
        stats["export_timestamp"] = datetime.now().isoformat()
        stats["recent_errors"] = self.get_recent_errors(50)

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)

    def clear_statistics(self) -> None:
        """Clear error statistics and history."""
        self.error_stats.clear()
        self.error_history.clear()

    def get_log_files(self) -> List[str]:
        """
        Get list of log files.

        Returns:
            List of log file paths
        """
        log_files = []
        for filename in ["errors.log", "warnings.log", "debug.log"]:
            log_file = os.path.join(self.log_dir, filename)
            if os.path.exists(log_file):
                log_files.append(log_file)
        return log_files


# Global error logger instance
_global_logger: Optional[ErrorLogger] = None


def get_error_logger() -> ErrorLogger:
    """
    Get global error logger instance.

    Returns:
        Global ErrorLogger instance
    """
    global _global_logger
    if _global_logger is None:
        _global_logger = ErrorLogger()
    return _global_logger


def log_error(
    error: Exception,
    error_code: Optional[str] = None,
    context: Optional[Dict[str, Any]] = None,
    source_code: Optional[str] = None,
    filename: Optional[str] = None,
) -> str:
    """
    Log an error using global logger.

    Args:
        error: The exception object
        error_code: Optional error code
        context: Additional context information
        source_code: Source code where error occurred
        filename: Filename where error occurred

    Returns:
        Error code assigned to this error
    """
    logger = get_error_logger()
    return logger.log_error(error, error_code, context, source_code, filename)


def log_warning(message: str, context: Optional[Dict[str, Any]] = None) -> None:
    """
    Log a warning using global logger.

    Args:
        message: Warning message
        context: Additional context information
    """
    logger = get_error_logger()
    logger.log_warning(message, context)


def log_debug(message: str, context: Optional[Dict[str, Any]] = None) -> None:
    """
    Log a debug message using global logger.

    Args:
        message: Debug message
        context: Additional context information
    """
    logger = get_error_logger()
    logger.log_debug(message, context)


def get_error_statistics() -> Dict[str, Any]:
    """
    Get error statistics from global logger.

    Returns:
        Dictionary with error statistics
    """
    logger = get_error_logger()
    return logger.get_error_statistics()
