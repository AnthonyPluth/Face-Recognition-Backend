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

    def test_list_images(self):
        image_list = sorted(list(utils.list_images("tests/reference/")))
        print(image_list)
        self.assertEqual(
            image_list,
            [
                "tests/reference/ai_face.webp",
                "tests/reference/blurry_image.webp",
                "tests/reference/maddie.webp",
                "tests/reference/sample_frame.webp",
            ],
        )

    @classmethod
    def tearDownClass(self):
        import os

        os.rmdir("new_directory_test")


if __name__ == "__main__":
    unittest.main()
