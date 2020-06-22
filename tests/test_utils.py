import os
import unittest
from face_rec_api import utils


class TestUtils(unittest.TestCase):
    def test_ensure_directory_existing(self):
        utils.ensure_directory("tests/")
        pass

    def test_ensure_directory_new(self):
        utils.ensure_directory("new_directory_test/")
        self.assertTrue(os.path.exists("new_directory_test"))

    @classmethod
    def tearDownClass(self):
        import os

        os.rmdir("new_directory_test")


if __name__ == "__main__":
    unittest.main()
