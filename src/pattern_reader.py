import yaml
import os
from setting import logger


class PatternReader:
    """ Read yaml file and return pattern string. """

    PATTERN_YAML_FILE_NAME = "patterns.yaml"

    def __init__(self, yaml_path: str = "") -> None:
        self._read(yaml_path)

    def _read(self, path: str) -> None:
        """ Read yaml file and store it as a dict."""

        if (path == ""):
            cur_executed_path = os.path.dirname(os.path.abspath(__file__))
            logger.debug(f"cur_executed_path: {cur_executed_path}")
            yaml_path = os.path.join(cur_executed_path, PatternReader.PATTERN_YAML_FILE_NAME)
        else:
            yaml_path = os.path.abspath(path)

        with open(yaml_path, "r") as f:
            self.pattern_dict = yaml.load(f, Loader=yaml.SafeLoader)

    def get_pattern(self, file_type: str, key: str) -> str:
        """ Return pattern string using '|' as a delimiter."""
        return '|'.join(self.pattern_dict[file_type][key])
