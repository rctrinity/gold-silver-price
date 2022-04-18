import logging

GoldForexURL = "https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/XAU/USD"
SilverForexURL = "https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/XAG/USD"
BtcURL = "https://api.coindesk.com/v1/bpi/currentprice.json"

class Color:
    """A class for terminal color codes."""

    BOLD = "\033[1m"
    BLUE = "\033[94m"
    WHITE = "\033[97m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    SILVER = "\033[37m"
    RED = "\033[91m"
    ORANGE = "\033[33m"
    BOLD_WHITE = BOLD + WHITE
    BOLD_BLUE = BOLD + BLUE
    BOLD_GREEN = BOLD + GREEN
    BOLD_YELLOW = BOLD + YELLOW
    BOLD_RED = BOLD + RED
    BOLD_ORANGE = BOLD + ORANGE
    END = "\033[0m"


class ColorLogFormatter(logging.Formatter):
    """A class for formatting colored logs."""

    FORMAT = '%(prefix)s%(levelname)s%(suffix)s [%(asctime)-15s] %(prefix)s%(message)s%(suffix)s'
    
    LOG_LEVEL_COLOR = {
        "DEBUG": {'prefix': '', 'suffix': ''},
        "INFO": {'prefix': Color.GREEN, 'suffix': Color.END},
        "WARNING": {'prefix': Color.BOLD_YELLOW, 'suffix': Color.END},
        "ERROR": {'prefix': Color.BOLD_RED, 'suffix': Color.END},
        "CRITICAL": {'prefix': Color.BOLD_RED, 'suffix': Color.END},
    }

    def format(self, record):
        """Format log records with a default prefix and suffix to terminal color codes that corresponds to the log level name."""
        if not hasattr(record, 'prefix'):
            record.prefix = self.LOG_LEVEL_COLOR.get(record.levelname.upper()).get('prefix')
        
        if not hasattr(record, 'suffix'):
            record.suffix = self.LOG_LEVEL_COLOR.get(record.levelname.upper()).get('suffix')

        formatter = logging.Formatter(self.FORMAT, datefmt='%Y-%m-%d %I:%M:%S %p')
        return formatter.format(record)