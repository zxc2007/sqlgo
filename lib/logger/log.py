import logging
import os
import sys

sys.path.append(os.getcwd())
from thirdparty.colorama import Fore,init
from lib.core.parser.cmdline import verbose

init()

class ColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': f'{Fore.CYAN}',          # Cyan
        'INFO': '\033[1;32m',          # Bold Green
        'WARNING': f'{Fore.YELLOW}',         # Yellow
        'ERROR': f'{Fore.RED}',         # Bold Red
        'CRITICAL': '\033[1;37;41m',   # White on Red (Bold)
        'DIM': '\033[2m',              # Dim text
        'RESET': '\033[0m'             # Reset color
    }

    def format(self, record):
        log_level = record.levelname
        log_message = super().format(record)
        colored_message = f"{self.COLORS.get(log_level, '')}{log_message}{self.COLORS['DIM']}{self.COLORS['RESET']}"
        return colored_message

logger = logging.getLogger('sqlgo_log')

if verbose == 1:
    logger.setLevel(level=logging.INFO)

elif verbose == 2:
    logger.setLevel(level=logging.WARNING)

elif verbose == 3:
    logger.setLevel(level=logging.ERROR)

elif verbose == 4:
    logger.setLevel(level=logging.CRITICAL)

elif verbose == 5:
    logger.setLevel(level=logging.DEBUG)

formatter = ColoredFormatter(
    "[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

# Log an info message with the default message
