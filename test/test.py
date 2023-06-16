import unittest
import subprocess
import os
from src.setting import logger
from test.test_fixture import Fixture


class MainTests(unittest.TestCase):
    """ Test main file with arguments via unittest """

    def setUp(self) -> None:
        logger.info("MainTests.setUp() is called.")

    def tearDown(self) -> None:
        """ Clear up generated files """
        logger.info("MainTests.tearDown() is called.")

        # Remove file if exists
        if os.path.exists(f"{Fixture.TEST_OUTPUT_DIR}/foo.log"):
            os.remove(f"{Fixture.TEST_OUTPUT_DIR}/foo.log")
        if os.path.exists(f"{Fixture.TEST_OUTPUT_DIR}/bar.log"):
            os.remove(f"{Fixture.TEST_OUTPUT_DIR}/bar.log")
        if os.path.exists(f"{Fixture.TEST_OUTPUT_DIR}/foobar.log"):
            os.remove(f"{Fixture.TEST_OUTPUT_DIR}/foobar.log")
        if os.path.exists(f"{Fixture.TEST_OUTPUT_DIR}/dgx.log"):
            os.remove(f"{Fixture.TEST_OUTPUT_DIR}/dgx.log")
        if os.path.exists(f"{Fixture.TEST_OUTPUT_DIR}/kizero.txt"):
            os.remove(f"{Fixture.TEST_OUTPUT_DIR}/kizero.txt")

    def test_run_main_py_in_terminal_log(self):
        """ Test main.py with arguments via unittest. Parse "*.log" file. """
        result = subprocess.run(['python3', Fixture.TEST_MAIN_PY_PATH,
                                 '--file', Fixture.TEST_LOG_FILE_PATH,
                                 '--out', Fixture.TEST_OUTPUT_DIR,
                                 '--pattern', Fixture.TEST_PATTERN_PATH,
                                 '--verbose'],
                                check=False,
                                stdout=subprocess.PIPE)

        # Check if there is no error
        self.assertEqual(result.returncode, 0)

        # Check if output files are generated
        self.assertTrue(os.path.exists(f"{Fixture.TEST_OUTPUT_DIR}/foo.log"))
        self.assertTrue(os.path.exists(f"{Fixture.TEST_OUTPUT_DIR}/bar.log"))
        self.assertTrue(os.path.exists(
            f"{Fixture.TEST_OUTPUT_DIR}/foobar.log"))
        self.assertTrue(os.path.exists(f"{Fixture.TEST_OUTPUT_DIR}/dgx.log"))

    def test_run_main_py_in_terminal_txt(self):
        """ Test main.py with arguments via unittest. Parse "*.txt" file. """
        result = subprocess.run(['python3', Fixture.TEST_MAIN_PY_PATH,
                                 '--file', Fixture.TEST_TXT_FILE_PATH,
                                 '--out', Fixture.TEST_OUTPUT_DIR,
                                 '--pattern', Fixture.TEST_PATTERN_PATH,
                                 '--verbose'],
                                check=False,
                                stdout=subprocess.PIPE)

        # Check if there is no error
        self.assertEqual(result.returncode, 0)

        # Check if output files are generated
        self.assertTrue(os.path.exists(
            f"{Fixture.TEST_OUTPUT_DIR}/kizero.txt"))
