from lib.core.parser.cmdline import attack
from lib.core.tester.maintestcheck import main_exploit
from lib.intruder.intruder import Intruder

if __name__ == "__main__":
    # main_exploit()
    obj = Intruder("http://testfire.net/index.jsp?content=business_deposit.htm",8080)
    obj.run_substring()
    