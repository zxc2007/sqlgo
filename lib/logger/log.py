import logging

class ColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[36m',  # Cyan
        'INFO': '\033[34m',   # Blue
        'WARNING': '\033[33m',  # Yellow
        'ERROR': '\033[31m',  # Red
        'CRITICAL': '\033[1;37;41m',  # White on Red (Bold)
        'RESET': '\033[0m'  # Reset color
    }

    def format(self, record):
        log_level = record.levelname
        log_message = super().format(record)
        colored_message = f"{self.COLORS.get(log_level, '')}{log_message}{self.COLORS['RESET']}"
        return colored_message

logger = logging.getLogger('sqlgo_log')
logger.setLevel(level=logging.INFO)

formatter = ColoredFormatter(
    "[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

# Log an info message with the default message

