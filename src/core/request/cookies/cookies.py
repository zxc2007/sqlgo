import http.cookies
import urllib.request
import os
import sys
sys.path.append(os.getcwd())
from src.core.parser.cmdline import url as _url
from src.logger.log import logger
from utilis.colorago.colorago import Fore
from src.core.parser.cmdline import beep

def extract_cookies(url=_url):
    user_input = ""
    try:
        response = urllib.request.urlopen(url)
        
        headers = response.info()
        cookies = http.cookies.SimpleCookie(headers.get("Set-Cookie"))

        logger.info("cookies from %s"%url)
        for cookie in cookies.values():
            if beep:
                __import__("extra.beep.beep")
            logger.info(f"Cookie name: {cookie.key}, cookie value by the server: {cookie.value}")

        user_input = input(f"{Fore.BRIGHT_GREEN}you have not declared any cookies while the server want to set its own,do you want to use those?(y,n)?: {Fore.RESET}").lower()
        if user_input != 'y':
            logger.error("Canceled by the user.")
            raise SystemExit

    except Exception as e:
        logger.error(e)

# Example usage
# url_to_extract_cookies = "http://testfire.net/index.jsp?content=business_deposit.htm"
# extract_cookies(url_to_extract_cookies)
