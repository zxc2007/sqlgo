"""
# SQLGO License - Version 1.1

Copyright (C) 2023-2024 Heisenberg

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""

import logging
import os
import sys

from colorama import Fore,init
from src.core.parser.cmdline import verbose

init()

import logging

try:
    from termcolor.termcolor import colored
except:
    from termcolor import colored

class CustomColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red',
    }

    def format(self, record):
        log_level_color = self.COLORS.get(record.levelname, 'white')
        log_level_name = colored(record.levelname, log_level_color)

        timestamp = self.formatTime(record, self.datefmt)
        timestamp_colored = colored(timestamp, 'blue')

        record.log_level = log_level_name  # Add a custom log level field
        record.timestamp_colored = timestamp_colored  # Add a custom timestamp field

        return super(CustomColoredFormatter, self).format(record)

def setup_logger():
    # Create a logger
    logger = logging.getLogger("sqlgo_logger")
    if verbose > 1:
        logger.setLevel(logging.DEBUG)
    
    else:
        logger.setLevel(logging.INFO)

    # Create a console handler and set the level to debug
    console_handler = logging.StreamHandler()
    if verbose == 5:
        console_handler.setLevel(logging.DEBUG)
    
    else:
        console_handler.setLevel(logging.DEBUG)

    # Create a colored formatter and add it to the handler
    formatter = CustomColoredFormatter(
        "[%(timestamp_colored)s] [%(log_level)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    console_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(console_handler)

    return logger

logger = setup_logger()


