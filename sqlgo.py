from lib.core.parser.cmdline import shell
if shell:
    __import__("lib.core.tester.shells")
    raise SystemExit
from lib.logger.log import logger
from lib.core.tester.gather import gather_exploit
from lib.checker.checks import check_version
from extra.disclaimer import disclaimer
from extra.logo import logo
import lib.core.setting.setting as settings
from lib.core.parser.cmdline import url as _url
from lib.core.shell.shell import shell_handler
import traceback
import threading
import os
import sys





def main():
    try:
        print(logo)
        print(settings.LEGAL_DISCLAIMER_MSG)
        check_version()
        gather_exploit()
    
    except KeyboardInterrupt:
        logger.error("User exit")
        raise SystemExit
    except Exception as _errmsg:
        errmsg = str(_errmsg)
        if "Invalid URL 'None': No scheme supplied. Perhaps you meant" in errmsg:
            _msg = "no url has been set for the targeting/testing connection.\n"
            _msg += "QUITTING!!!"
            logger.critical(_msg)
            raise SystemExit
        
        elif "HTTPConnectionPool" in errmsg:
            _msg = "Connection refused by the host %s try reaching it by using another port or check your internet connection."
            logger.critical(_msg)
            print(errmsg)
            raise SystemExit
        
        elif "ValueError: unknown url type: 'None'" in errmsg:
            _msg = "no url has been set for testing connection to the url,at least url should be given by : -u/--url\n"
            logger.critical(_msg)
            raise SystemExit
        
        
        elif any(["Invalid URL" in errmsg,"No scheme supplied" in errmsg]):
            _msg = "no scheme has been set for the target url, try using http:// https://\n on the url and then parse it."
            logger.critical(_msg)
            raise SystemExit
        
        elif any(["Errno 8] nodename nor servname provided, or not known" in errmsg,".HTTPConnection object at" in errmsg]):
            _msg = "invalid host has been set for testing.\n"
            _msg += "QUITTING!!!"
            logger.critical(_msg)
            raise SystemExit
        
            

    

if __name__ == "__main__":
    try:
        
        main()
    
    except SystemExit:
        raise
    except KeyboardInterrupt:
        pass

    except:
        traceback.print_exc()
    finally:
        if threading.active_count() > 1:
            os._exit(0)
        else:
            sys.exit(0)
            


        

