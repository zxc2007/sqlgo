import threading
from lib.core.parser.cmdline import attack
from lib.core.tester.maintestcheck import main_exploit
from lib.intruder.intruder import Intruder_substring,MakeSet
from lib.core.request.POSt.post import subber
from lib.core.tester.union import union
from lib.core.tester.substring import substring
from lib.logger.log import logger
from lib.core.tester.timebased import time_based
from lib.core.request.connection import test_connection
from lib.core.request.cookies.cookies import extract_cookies



def main():
    try:
        test_connection()
        extract_cookies()
        threads = [
            union(),
            substring(),
            time_based()
        ]

        thread_objects = []

        for thread_func in threads:
            _thread = threading.Thread(target=thread_func)
            _thread.start()
            thread_objects.append(_thread)

        # Wait for all threads to finish
        for _thread in thread_objects:
            _thread.join()
    
    except Exception as e:
        logger.error(e)
if __name__ == "__main__":
    main()

    