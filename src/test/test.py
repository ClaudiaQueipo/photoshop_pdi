import unittest
import numpy as np
import cv2
from photoshop import Photoshop

class TestImageProcessor(unittest.TestCase):
    
    def setUp(self):
        self.photoshop = Photoshop()
        self.test_image = np.array("src\test\300px-ISPJAM7.jpg")
        
    
    def test_adjust_brightness(self):
        result = self.photoshop.adjust_brightness(self.test_image, 50)
        expected = cv2.convertScaleAbs(self.test_image, alpha=1, beta=50)
        self.assertEqual(result.dtype, expected.dtype)
        self.assertEqual(result.shape, expected.shape)
        self.assertTrue(np.allclose(result, expected))
    
    def test_adjust_contrast(self):
        result = self.photoshop.adjust_contrast(self.test_image, 50)
        alpha = (50 + 100) / 100
        expected = cv2.convertScaleAbs(self.test_image, alpha=alpha, beta=-50*alpha)
        self.assertEqual(result.dtype, expected.dtype)
        self.assertEqual(result.shape, expected.shape)
        self.assertTrue(np.allclose(result, expected))
    
    def test_image_flip(self):
        result = self.photoshop.image_flip(self.test_image)
        expected = np.flip(self.test_image, axis=0)
        self.assertEqual(result.dtype, expected.dtype)
        self.assertEqual(result.shape, expected.shape)
        self.assertTrue(np.allclose(result, expected))
    
    def test_image_mirror(self):
        result = self.photoshop.image_mirror(self.test_image)
        expected = np.flip(self.test_image, axis=1)
        self.assertEqual(result.dtype, expected.dtype)
        self.assertEqual(result.shape, expected.shape)
        self.assertTrue(np.allclose(result, expected))
    
    def test_image_rotate(self):
        result = self.photoshop.image_rotate(self.test_image)
        expected = np.rot90(self.test_image, k=3)
        self.assertEqual(result.dtype, expected.dtype)
        self.assertEqual(result.shape, expected.shape)
        self.assertTrue(np.allclose(result, expected)))


if __name__ == '__main__':
    unittest.main()