from face_rec_api import image_processing
import cv2
import unittest

sample_frame = cv2.imread('tests/reference/sample_frame.webp')
unknown_face = cv2.imread('tests/reference/ai_face.webp')
known_face = cv2.imread('tests/reference/maddie.webp')
blurry_image = cv2.imread('tests/reference/blurry_image.webp')


class TestImageProcessing(unittest.TestCase):

    def test_get_faces(self):
        faces = image_processing.get_faces(sample_frame)
        print(faces[0])
        self.assertEqual(faces[0], (126, 100, 272, 355))

    def test_crop_frame(self):
        cropped_frame = image_processing.crop_frame(sample_frame, (127, 96, 272, 361))
        self.assertEqual(cropped_frame.shape, (361, 272, 3))

    def test_identify_unknown_person(self):
        face_id, confidence = image_processing.identify_person(unknown_face)
        self.assertLess(confidence, 90)

    def test_identify_known_person(self):
        face_id, confidence = image_processing.identify_person(known_face)
        self.assertEqual(face_id, "Maddie")

    def test_blur_detection_blurry(self):
        is_blurry = image_processing.frame_has_blur(blurry_image)
        self.assertTrue(is_blurry)

    def test_blur_detection_clear(self):
        is_blurry = image_processing.frame_has_blur(sample_frame)
        self.assertFalse(is_blurry)

    def test_base64_conversion(self):
        base64_encoded = image_processing.numpy_array_to_base64(known_face)
        converted_image = image_processing.base64_to_numpy_array(base64_encoded)
        base64_converted = image_processing.numpy_array_to_base64(converted_image)
        # np.testing.assert_array_equal(base64_encoded, base64_converted)
        self.assertEqual(base64_encoded, base64_converted)

    def test_save_image(self):
        image_processing.save_image(known_face, 'test', 'pytest.webp')
        saved_image = cv2.imread('datasets/test/pytest.webp')
        self.assertEqual(bytes(known_face), bytes(saved_image))

    @classmethod
    def tearDownClass(self):
        import os
        os.remove('datasets/test/pytest.webp')
        os.rmdir('datasets/test')


if __name__ == '__main__':
    unittest.main()
