import yaml
import os

class PatternReader:

    def __init__(self, yaml_path: str) -> None:
        self._read(yaml_path)

    def _read(self, path: str) -> None:
        """ Read yaml file and store it as a dict."""
        abs_path = os.path.abspath(path)
        with open(abs_path, "r") as f:
            self.pattern_dict = yaml.load(f, Loader=yaml.SafeLoader)

    def get_pattern(self, file_type: str, key: str) -> str:
        """ Return pattern string using '|' as a delimiter."""
        return '|'.join(self.pattern_dict[file_type][key])
