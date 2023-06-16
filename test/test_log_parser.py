import unittest
from test.test_fixture import Fixture
from src.log_parser import LogParser
from src.pattern_reader import PatternReader


class TestLogParser(unittest.TestCase):
    """Test for LogParser class."""

    def setUp(self):
        self.pttrn_reader = PatternReader(Fixture.TEST_PATTERN_PATH)

    def test_get_file_type(self):
        """Test for get_file_type() method."""
        log_parser = LogParser(pttrn_reader=self.pttrn_reader,
                               log_file=Fixture.TEST_LOG_FILE_PATH,
                               out_dir=Fixture.TEST_OUTPUT_DIR)

        self.assertEqual("log", log_parser.get_file_type("foo.log"))
        self.assertEqual("txt", log_parser.get_file_type("bar.txt"))
        self.assertEqual("log", log_parser.get_file_type("foo.bar.log"))

    def test_get_file_type_force_type(self):
        """When file type is specified, it must be used."""
        log_parser = LogParser(pttrn_reader=self.pttrn_reader,
                               log_file=Fixture.TEST_LOG_FILE_PATH,
                               out_dir=Fixture.TEST_OUTPUT_DIR,
                               file_type="txt")

        self.assertEqual("txt", log_parser.get_file_type("foo.log"))

    def test_get_file_type_invalid_file_name(self):
        """Test for get_file_type() method. When file_type is not specified,
        target file must have extension."""
        log_parser = LogParser(pttrn_reader=self.pttrn_reader,
                               log_file=Fixture.TEST_LOG_FILE_PATH,
                               out_dir=Fixture.TEST_OUTPUT_DIR)

        self.assertRaises(ValueError, log_parser.get_file_type, "foobar")
