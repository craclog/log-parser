import argparse
from os.path import abspath
from setting import logger

class ArgumentParser:
    """
    Usage:
    python3 log_parser.py --file <TARGET_FILE> [--verbose]
    """
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Log Parser')

    def parse_args(self):
        """ Parse arguments """
        self.parser.add_argument('--file', help='target log file path',
                                 required=True)
        self.parser.add_argument('--out', help='output directory',
                                 required=False, default=".")
        self.parser.add_argument('--pattern', help='pattern yaml file path',
                                 required=False, default="")
        self.parser.add_argument('--verbose', help='verbose mode',
                                 action='store_true', default=False)
        args = self.parser.parse_args()
        args.out = abspath(args.out)
        if args.verbose:
            logger.setLevel("DEBUG")
        logger.debug(f"args: {args}")
        return args
