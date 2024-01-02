import http.cookies
import urllib.request
import os
import sys
sys.path.append(os.getcwd())
from lib.core.parser.cmdline import url as _url
from lib.logger.log import logger
from utilis.colorago.colorago import Fore

def extract_cookies(url=_url):
    user_input = ""
    try:
        response = urllib.request.urlopen(url)
        
        headers = response.info()
        cookies = http.cookies.SimpleCookie(headers.get("Set-Cookie"))

        logger.info("cookies from %s"%url)
        for cookie in cookies.values():
            logger.info(f"Name: {cookie.key}, Value: {cookie.value}")

        user_input = input(f"{Fore.BRIGHT_GREEN}Do you want to continue(your cookies has not been set or accepted by the server)? (y/n): {Fore.RESET}").lower()
        if user_input != 'y':
            logger.error("Canceled by the user.")
            raise SystemExit

    except Exception as e:
        logger.error(e)

# Example usage
# url_to_extract_cookies = "http://testfire.net/index.jsp?content=business_deposit.htm"
# extract_cookies(url_to_extract_cookies)
