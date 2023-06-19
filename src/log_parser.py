#!/usr/bin/env python3
# coding: utf-8
import time
import os
import subprocess
import textwrap
from pattern_reader import PatternReader
from setting import logger
from argument_parser import ArgumentParser


class LogParser:
    """Log parser class reads log file and generates outputs with patterns.

    Attributes:
        pttrn_reader (PatternReader): PatternReader instance.
        log_file (str): Log file path.
        out_dir (str): Output directory path.
        file_type (str): File type (e.g. log, txt).
    """

    def __init__(self, pttrn_reader: PatternReader, log_file: str, out_dir: str, file_type: str="") -> None:
        self.pttrn_reader = pttrn_reader
        self.log_file = log_file
        self.out_dir = out_dir
        self.file_type = file_type

    def run_egrep(self, pattern: str) -> str:
        """Run egrep with i option and return the result."""
        target_file_abspath = os.path.abspath(self.log_file)
        cmd_list = ["egrep", "-i", pattern, target_file_abspath]
        logger.debug(f"cmd_list: {cmd_list}")
        try:
            output = subprocess.check_output(cmd_list)
            # Print output for debug
            # logger.debug("\n" + output.decode("utf-8"))
            return output.decode("utf-8")
        except subprocess.CalledProcessError as err:
            logger.error(f"Error: {err}")
            return ""

    def get_file_type(self, filename: str):
        """Get file type from file name if it is not specified.
        If file type is specified, return it.

        Args:
            filename (str): File name.

        Returns:
            str: File type.
        """
        if self.file_type:
            return self.file_type

        if '.' not in filename:
            msg = textwrap.dedent(f"""\
                    File name {filename} is invalid. It must have extension
                    when file type is not specified, it is determined by extension.""")
            raise ValueError(msg)
        return filename.split('.')[-1]

    def parse_log_file_and_generate_outputs(self) -> None:
        """Parse log file and generate outputs with patterns"""
        try:
            file_type = self.get_file_type(self.log_file)
            logger.debug(f"file_type: {file_type}")

            if file_type not in self.pttrn_reader.get_all_file_types():
                logger.error(f"File type {file_type} is not supported.")
                return

            for key in self.pttrn_reader.get_keys_for_type(file_type):
                logger.info(f"Grep pattern: {key}")
                self.pttrn_reader.dump_pattern(file_type=file_type, key=key)
                pattern = self.pttrn_reader.get_pattern(file_type=file_type, key=key)
                output = self.run_egrep(pattern=pattern)
                if output:
                    file_name = f"{key}.{file_type}"
                    with open(os.path.join(self.out_dir, file_name), "w") as file:
                        file.write(output)
                        logger.info(f"Output file: {file_name}")
        except ValueError as verr:
            logger.error(f"Error: {verr}")
        except Exception as err:
            logger.error(f"Error: {err}")

def main():
    """Main function"""
    start_time = time.time()

    args = ArgumentParser().parse_args()
    pttrn_reader = PatternReader(yaml_path=args.pattern)

    log_parser = LogParser(pttrn_reader=pttrn_reader, log_file=args.file,
                           out_dir=args.out, file_type=args.type)
    log_parser.parse_log_file_and_generate_outputs()
    logger.info(f"Elapsed time: {time.time() - start_time:.3f} seconds")


if __name__ == '__main__':
    main()
