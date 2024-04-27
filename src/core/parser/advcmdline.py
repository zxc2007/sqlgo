#!/usr/bin/env python
"""
# SQLGO License - Version 1.4

Copyright (C) 2023-2024 AliMirmohammad

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
import argparse

class BaseAdvCmd(argparse.ArgumentParser):
    def __init__(self):
        super().__init__(description="sqlgo")

    def add_arguments(self, action):
        action.add_argument(
            '--hh',
            dest='advanced_help',
            action='store_true',
            default=False,
            help='Show the helping menu'
        )
        super().add_argument(action)

class AdvCmd(BaseAdvCmd):
    def __init__(self):
        super(AdvCmd, self).__init__()



