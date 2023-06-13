import time
import os
import subprocess
from pattern_reader import PatternReader
from setting import logger
from argument_parser import ArgumentParser


def run_egrep(pattern: str, target_file_path: str) -> str:
    """ Run egrep with i option and return the result. """
    target_file_abspath = os.path.abspath(target_file_path)
    cmd_list = ["egrep", "-i", pattern, target_file_abspath]
    logger.debug(f"cmd_list: {cmd_list}")
    try:
        output = subprocess.check_output(cmd_list)
        logger.debug("\n" + output.decode("utf-8"))
        return output.decode("utf-8")
    except subprocess.CalledProcessError as err:
        logger.error(f"Error: {err}")
        return ""

def get_file_type(filename: str):
    """ Get file type from file name. """
    return filename.split('.')[-1]

def parse_log_file_and_generate_outputs(args, pttrn_reader: PatternReader) -> None:
    file_type = get_file_type(args.file)
    logger.debug(f"file_type: {file_type}")

    if (file_type not in pttrn_reader.pattern_dict.keys()):
        logger.error(f"File type {file_type} is not supported.")
        return

    for key in pttrn_reader.pattern_dict[file_type].keys():
        logger.info(f"Grep pattern: {key}")
        pattern = pttrn_reader.get_pattern(file_type=file_type, key=key)
        output = run_egrep(pattern=pattern, target_file_path=args.file)
        if output:
            with open(os.path.join(args.out, f"{key}.{file_type}"), "w") as f:
                f.write(output)

def main():
    start_time = time.time()

    args = ArgumentParser().parse_args()
    pttrn_reader = PatternReader(yaml_path=args.pattern)

    parse_log_file_and_generate_outputs(args, pttrn_reader)
    logger.info(f"Elapsed time: {time.time() - start_time:.3f} seconds")


if __name__ == '__main__':
    main()
