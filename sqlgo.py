from lib.core.parser.cmdline import attack
from lib.core.tester.maintestcheck import main_exploit
from lib.intruder.intruder import Intruder_substring,MakeSet

if __name__ == "__main__":
    # main_exploit()
    obj = MakeSet("http://testfire.net/index.jsp?content=business_deposit.htm",8080)
    obj._send_payload_make_set()
    