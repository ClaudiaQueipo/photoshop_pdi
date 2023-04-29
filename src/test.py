import unittest
import numpy as np
import cv2
from photoshop import Photoshop

class TestImageProcessor(unittest.TestCase):
    
    def setUp(self):
        self.photoshop = Photoshop()
        self.test_image = np.ones((100, 100, 3), dtype=np.uint8)
    
    def test_adjust_brightness(self):
        result = self.photoshop.adjust_brightness(self.test_image, 50)
        self.assertTrue(np.all(result == cv2.convertScaleAbs(self.test_image, alpha=1, beta=50)))
    
    def test_adjust_contrast(self):
        result = self.photoshop.adjust_contrast(self.test_image, 50)
        alpha = (50 + 100) / 100
        self.assertTrue(np.all(result == cv2.convertScaleAbs(self.test_image, alpha=alpha, beta=0)))
    
    def test_image_flip(self):
        result = self.photoshop.image_flip(self.test_image)
        self.assertTrue(np.all(result == np.flip(self.test_image, axis=0)))
    
    def test_image_mirror(self):
        result = self.photoshop.image_mirror(self.test_image)
        self.assertTrue(np.all(result == np.flip(self.test_image, axis=1)))
    
    def test_image_rotate(self):
        result = self.photoshop.image_rotate(self.test_image)
        self.assertTrue(np.all(result == np.rot90(self.test_image)))


if __name__ == '__main__':
    unittest.main()
