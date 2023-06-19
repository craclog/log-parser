import os
import yaml
from setting import logger


class PatternReader:
    """Read yaml file and return pattern string. """

    PATTERN_YAML_FILE_NAME = "patterns.yaml"

    def __init__(self, yaml_path: str = "") -> None:
        self._read(yaml_path)

    def _read(self, path: str) -> None:
        """Read yaml file and store it as a dict."""

        if path == "":
            cur_executed_path = os.path.dirname(os.path.abspath(__file__))
            logger.debug(f"cur_executed_path: {cur_executed_path}")
            yaml_path = os.path.join(cur_executed_path, PatternReader.PATTERN_YAML_FILE_NAME)
        else:
            yaml_path = os.path.abspath(path)

        with open(yaml_path, "r") as file:
            self.pattern_dict = yaml.load(file, Loader=yaml.SafeLoader)

    def get_pattern(self, file_type: str, key: str) -> str:
        """Return pattern string using '|' as a delimiter."""
        return '|'.join(self.pattern_dict[file_type][key])

    def get_all_file_types(self) -> list:
        """Return all file types in pattern yaml file."""
        return list(self.pattern_dict.keys())

    def get_keys_for_type(self, file_type: str) -> list:
        """Return all keys for specified file type."""
        return list(self.pattern_dict[file_type].keys())

    def dump_pattern(self, file_type: str, key: str) -> None:
        """Print pattern string for specified file type and key."""
        logger.info(f"Patterns for [file type: {file_type}], [key: {key}]:")
        for pattern in self.pattern_dict[file_type][key]:
            logger.info(f"- {pattern}")
