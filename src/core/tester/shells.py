import os
import sys
sys.path.append(os.getcwd())
from src.core.shell.shell import shell_handler
from src.core.parser.cmdline import shell

if shell:
    shell_handler()
    