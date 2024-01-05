from lib.logger.log import logger
from lib.core.tester.gather import gather_exploit
from extra.disclaimer import disclaimer
from extra.logo import logo
import lib.core.setting.setting as settings




def main():
    try:
        print(logo)
        print(settings.LEGAL_DISCLAIMER_MSG)
        gather_exploit()
    except Exception as e:
        logger.error(e)
    
    except KeyboardInterrupt:
        logger.error("User exit")
if __name__ == "__main__":
    main()
