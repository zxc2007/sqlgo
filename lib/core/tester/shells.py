import os
import sys
sys.path.append(os.getcwd())
from lib.core.shell.shell import shell_handler
from lib.core.parser.cmdline import shell

if shell:
    shell_handler()
    