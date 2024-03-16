#!/usr/bin/env python
"""
# SQLGO License - Version 1.4

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
import random
import string

def generateUserAgent():
    browser = random.choice(["Chrome", "Firefox", "Safari", "Edge"])
    version = ".".join([str(random.randint(1, 15)) for _ in range(3)])
    platform = random.choice(["Windows", "Macintosh", "Linux"])
    user_agent = "%s/%s(%s; %s)" % (browser, version, platform, generate_random_string(10))

    return user_agent

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def generate_user_agent_headers(num_headers):
    user_agent_headers = []
    for _ in range(num_headers):
        user_agent =  generateUserAgent()
        user_agent_headers.append({"User-Agent": user_agent})
    return user_agent_headers

def Prepare_the_headers():
    user_agent_headers =  generate_user_agent_headers(100)
    headers = []
    for header in user_agent_headers:
        headers.append(header["User-Agent"])
    return headers

headers = Prepare_the_headers()

# Usage with requests
url = "https://www.google.com"
payload = {"key1": "value1", "key2": "value2"}

headers_sqlgo = []

for header in headers:
    headers_sqlgo.append(header)