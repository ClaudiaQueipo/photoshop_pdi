import cv2
import numpy as np
from PIL import Image, ImageTk

class Photoshop():
    
    def adjust_brightness(self, image: np.ndarray, value: int) -> np.ndarray:
        """Adjusts the brightness of an input image by a given value."""
        
        final_output = cv2.convertScaleAbs(image, alpha=1, beta=value)
        return final_output
    
    
    def adjust_contrast(self, image: np.ndarray, value: int) -> np.ndarray:
        """ Adjusts the contrast of an input image by a given value  """  
            
        alpha = (value + 100) / 100
        final_output = cv2.convertScaleAbs(image, alpha=alpha, beta=0)
        
        
        
        return final_output


    def image_flip(self, image: np.ndarray) -> np.ndarray:
        """Flips an input image vertically."""
        img_flipped = np.flip(image, axis=0)
        return img_flipped

    
    def image_mirror(self, image: np.ndarray) -> np.ndarray:
        """Mirrors an input image horizontally."""
        img_mirrored = np.flip(image, axis=1)
        return img_mirrored

  
    def image_rotate(self, image: np.ndarray) -> np.ndarray:
        """ Rotates an input image by 90 degrees counter-clockwise. """
        img_rotate = np.rot90(image)
        return img_rotate
    
    

    
    
    
    
    
    
    
    
    
    


        
        
        