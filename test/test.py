import unittest
import subprocess
import os
from src.setting import logger

TEST_MAIN_PY_PATH = "src/log_parser.py"
TEST_DIR = "test"
TEST_OUTPUT_DIR = f"{TEST_DIR}/data"
TEST_LOG_FILE_PATH = f"{TEST_DIR}/data/sample.log"
TEST_TXT_FILE_PATH = f"{TEST_DIR}/data/sample2.txt"


class MainTests(unittest.TestCase):
    """ Test main file with arguments via unittest """

    def setUp(self) -> None:
        logger.info("MainTests.setUp() is called.")

    def tearDown(self) -> None:
        """ Clear up generated files """
        logger.info("MainTests.tearDown() is called.")

        # Remove file if exists
        if os.path.exists(f"{TEST_OUTPUT_DIR}/foo.log"):
            os.remove(f"{TEST_OUTPUT_DIR}/foo.log")
        if os.path.exists(f"{TEST_OUTPUT_DIR}/bar.log"):
            os.remove(f"{TEST_OUTPUT_DIR}/bar.log")
        if os.path.exists(f"{TEST_OUTPUT_DIR}/foobar.log"):
            os.remove(f"{TEST_OUTPUT_DIR}/foobar.log")
        if os.path.exists(f"{TEST_OUTPUT_DIR}/dgx.log"):
            os.remove(f"{TEST_OUTPUT_DIR}/dgx.log")
        if os.path.exists(f"{TEST_OUTPUT_DIR}/kizero.txt"):
            os.remove(f"{TEST_OUTPUT_DIR}/kizero.txt")

    def test_run_main_py_in_terminal_log(self):
        # Run main program with arguments. Parse "*.log" file.
        result = subprocess.run(['python3', TEST_MAIN_PY_PATH, '--file', TEST_LOG_FILE_PATH, '--out', TEST_OUTPUT_DIR, '--verbose'], stdout=subprocess.PIPE)

        # Check if there is no error
        self.assertEqual(result.returncode, 0)

        # Check if output files are generated
        self.assertTrue(os.path.exists(f"{TEST_OUTPUT_DIR}/foo.log"))
        self.assertTrue(os.path.exists(f"{TEST_OUTPUT_DIR}/bar.log"))
        self.assertTrue(os.path.exists(f"{TEST_OUTPUT_DIR}/foobar.log"))
        self.assertTrue(os.path.exists(f"{TEST_OUTPUT_DIR}/dgx.log"))

    def test_run_main_py_in_terminal_txt(self):
        # Run main program with arguments. Parse "*.txt" file.
        result = subprocess.run(['python3', TEST_MAIN_PY_PATH, '--file', TEST_TXT_FILE_PATH, '--out', TEST_OUTPUT_DIR, '--verbose'], stdout=subprocess.PIPE)

        # Check if there is no error
        self.assertEqual(result.returncode, 0)

        # Check if output files are generated
        self.assertTrue(os.path.exists(f"{TEST_OUTPUT_DIR}/kizero.txt"))
