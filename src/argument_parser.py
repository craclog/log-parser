import argparse
from os.path import abspath
from setting import logger

class ArgumentParser:
    '''
    Argument parser class.
    '''
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Log Parser')

    def parse_args(self):
        '''
        Parse arguments

        Attributes:
            file (str): target log file path
            out (str): output directory
            pattern (str): pattern yaml file path
            type (str): file type (e.g. log, txt)
            verbose (bool): verbose mode
        '''
        self.parser.add_argument('--file', help='target log file path',
                                 required=True)
        self.parser.add_argument('--out', help='output directory',
                                 required=False, default=".")
        self.parser.add_argument('--pattern', help='pattern yaml file path',
                                 required=False, default="")
        self.parser.add_argument('--type', help='Force file type (e.g. log, txt)',
                                 required=False, default="")
        self.parser.add_argument('-v', '--verbose', help='verbose mode',
                                 action='store_true', default=False)
        args = self.parser.parse_args()
        args.out = abspath(args.out)
        if args.verbose:
            logger.setLevel("DEBUG")
        logger.debug(f"args: {args}")
        return args
