from extras.update import update_from_git
from src.core.parser.cmdline import api

if api.updates:
    update_from_git()
    raise SystemExit

from src.logger.log import logger
from src.core.tester.gather import gather_exploit
from src.checker.checks import check_version
from extras.disclaimer import disclaimer
from extras.logo import logo
import src.core.setting.setting as settings
from src.core.parser.cmdline import url as _url
from src.core.parser.cmdline import beep
from src.core.shell.shell import shell_handler
from datetime import datetime
from src.core.controler.handler import handle_dbms_connection
from sqlmap.sqlmap import modulePath
from sqlmap.lib.core.common import setPaths
import src.core.setting.setting as settings
import traceback
import threading
import os
import sys
import warnings
from src.core.controler.checker import start

try:
    sys.path.append("./.venv/lib/python3.12/site-packages")
except:
    pass

warnings.filterwarnings("ignore", category=SyntaxWarning)



# handle_dbms_connection()



def main():
    try:
        setPaths(modulePath())
        print(logo)
        print(settings.LEGAL_DISCLAIMER_MSG)
        print(f"starting @ {settings.formatted_datetime}")
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
    
        
        elif any(["UnicodeError: encoding with 'idna' codec failed (UnicodeError: label empty or too long)" in errmsg,"UnicodeError: encoding with 'idna' " in errmsg]):
            _msg = "entered domain is wrong or does not exists.please check your domain.\n"
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

    except ModuleNotFoundError:
        pass

    except:
        traceback.print_exc()
    finally:
        try:
            if threading.active_count() > 1:
                os._exit(0)
            else:
                sys.exit(0)
        
        finally:
            print(f"ending @ {settings.formatted_datetime}")
            if beep:
                __import__("extra.beep.beep")
            


        

