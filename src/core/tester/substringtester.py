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
import os
import sys
from src.core.payloads.substringpayload import _sorted as substring_payload
from src.data import arg
from src.core.parser.cmdline import port as _port
from src.core.parser.cmdline import attack
from src.core.request.POSt.post import SubData
import src.core.setting.setting as settings
from src.logger.log import logger

class SubstringTester:
    def __init__(self,data, url= arg.url,  port=_port) -> None:
        self.url = url
        self.data = data if data is not None else substring_payload
        self.port = port
        self.sub = SubData(self.url, self.port)

    def test(self):
        self.sub.submit_data(self.url, self.data)
        logger.debug("submitting the data on the server %s"%self.url)



def run_substring():
    if attack == "sub_string":
        test = SubstringTester(data=None)
        test.test()

# test = SubstringTester(url="http://testfire.net/login.jsp",port=80,data=None)
# test.test()