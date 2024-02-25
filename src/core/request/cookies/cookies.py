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
import http.cookies
import urllib.request
import os
import sys
from src.logger.log import logger
from utilis.colorago.colorago import Fore
from src.core.parser.cmdline import beep
from src.data import arg

def extract_cookies(url=arg.url):
    user_input = ""
    try:
        response = urllib.request.urlopen(url)
        
        headers = response.info()
        cookies = http.cookies.SimpleCookie(headers.get("Set-Cookie"))

        logger.info("cookies from %s"%url)
        for cookie in cookies.values():
            if arg.beep:
                __import__("extra.beep.beep")
            logger.info(f"Cookie name: {cookie.key}, cookie value by the server: {cookie.value}")
        if arg.accept_cookie or arg.batch:
            user_input = 'y'
        
        else:
            user_input = input(f"{Fore.BRIGHT_GREEN}you have not declared any cookies while the server want to set its own,do you want to use those?(y,n)?: {Fore.RESET}").lower()
  
        if user_input != 'y':
            logger.error("Canceled by the user.")
            raise SystemExit

    except Exception as e:
        logger.error(e)

# Example usage
# url_to_extract_cookies = "http://testfire.net/index.jsp?content=business_deposit.htm"
# extract_cookies(url_to_extract_cookies)
