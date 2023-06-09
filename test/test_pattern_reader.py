import os
import unittest
from src.pattern_reader import PatternReader

TEST_PATTERN_YAML_PATH = "src/patterns.yaml"

class TestPatternReader(unittest.TestCase):
    """ Test for PatternReader class. """

    def setUp(self):
        self.pattern = PatternReader(TEST_PATTERN_YAML_PATH)

    def test_read(self):
        """ Test for _read() method. _read is called in __init__(). """
        expected_pattern_dict = {
            "log": {
                "foo": ["FOO"],
                "bar": ["BAR"],
                "foobar": ["FOO", "BAR"],
                "dgx": ["DGX"]
            },
            "txt": {
                "kizero": ["KIZERO"]
            }
        }
        self.assertEqual(expected_pattern_dict, self.pattern.pattern_dict)

    def test_get_pattern_multiple_pattern(self):
        """ Test for get_pattern() method which returns pattern string. """
        expected_pattern = "FOO|BAR"
        self.assertEqual(expected_pattern,
                         self.pattern.get_pattern(file_type="log", key="foobar"))
