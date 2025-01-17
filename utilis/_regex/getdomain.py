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
import re
import socket

def extract_domain(url):
    pattern = re.compile(r'https?://(?:www\.)?([^/]+)') if "https" in url else re.compile(r'https?://(?:www\.)?([^/]+)')
    match = pattern.match(url)
    if match:
        return str(socket.gethostbyname(match.group(1)))
    else:
        return None

