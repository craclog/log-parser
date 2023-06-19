import os
import unittest
from src.pattern_reader import PatternReader
from test.test_fixture import Fixture

# TEST_PATTERN_YAML_PATH = "test/test_patterns.yaml"

class TestPatternReader(unittest.TestCase):
    """ Test for PatternReader class. """

    def setUp(self):
        self.pattern = PatternReader(Fixture.TEST_PATTERN_PATH)

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

    def test_get_all_file_types(self):
        """ Test for get_all_file_types() method. """
        expected_file_types = ["log", "txt"]
        self.assertEqual(expected_file_types, self.pattern.get_all_file_types())

    def test_get_keys_for_type(self):
        """ Test for get_keys_for_type() method. """
        expected_keys = ["foo", "bar", "foobar", "dgx"]
        self.assertEqual(expected_keys, self.pattern.get_keys_for_type("log"))
