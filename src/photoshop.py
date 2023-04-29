import cv2
import numpy as np
from PIL import Image, ImageTk
from meta.singleton_meta import SingletonMeta


from functools import wraps
from typing import Callable

def pil_to_np(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Convierte la imagen de PIL a numpy antes de llamar a la función
        image = args[1]
        args = list(args)
        args[1] = np.array(image)
        return func(*args, **kwargs)
    return wrapper

def np_to_pil(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Convierte la imagen de numpy a PIL después de llamar a la función
        result = func(*args, **kwargs)
        return Image.fromarray(result)
    return wrapper

class Photoshop(metaclass=SingletonMeta):
    
    @pil_to_np
    @np_to_pil
    def adjust_brightness(self, image: np.ndarray, value: int) -> np.ndarray:
        value = value
        print(value)
        final_output = cv2.convertScaleAbs(image, alpha=1, beta=value)
        return final_output
    
    
    @pil_to_np
    @np_to_pil
    def adjust_contrast(self, image: np.ndarray, value: int) -> np.ndarray:
        value = value
        alpha = (value + 100) / 100
        final_output = cv2.convertScaleAbs(image, alpha=alpha, beta=0)
        
        
        
        return final_output

    @pil_to_np
    @np_to_pil
    def image_flip(self, image: np.ndarray) -> np.ndarray:
        img_flipped = np.flip(image, axis=0)
        return img_flipped

    @pil_to_np
    @np_to_pil
    def image_mirror(self, image: np.ndarray) -> np.ndarray:
        img_mirrored = np.flip(image, axis=1)
        return img_mirrored

    @pil_to_np
    @np_to_pil
    def image_rotate(self, image: np.ndarray) -> np.ndarray:
        img_rotate = np.rot90(image)
        return img_rotate
    
    @pil_to_np
    @np_to_pil
    def median_blur(self, image: np.ndarray) -> np.ndarray:
        median_blur = cv2.medianBlur(image, 3)
        return median_blur
    
    
    @pil_to_np
    @np_to_pil
    def sum(self, image: np.ndarray, image2) -> np.ndarray:
        image2 = np.array(image2)
        result  = cv2.add(image, image2)
        
        return result
    
    @pil_to_np
    @np_to_pil
    def subtract(self, image: np.ndarray, image2) -> np.ndarray:
        image2 = np.array(image2)
        result  = cv2.subtract(image, image2)
        
        return result
    
    # Logic Operations
    @pil_to_np
    @np_to_pil
    def lo_not(self, image: np.ndarray) -> np.ndarray:
        invert_image = cv2.bitwise_not(image)
        return invert_image
    
    @pil_to_np
    @np_to_pil
    def lo_and(self, image: np.ndarray, image2) -> np.ndarray:
        image2 = np.array(image2)
        and_image = cv2.bitwise_and(image, image2)
        return and_image
    
    @pil_to_np
    @np_to_pil
    def lo_or(self, image: np.ndarray, image2) -> np.ndarray:
        image2 = np.array(image2)
        or_image = cv2.bitwise_or(image, image2)
        return or_image
    
    @pil_to_np
    @np_to_pil
    def lo_xor(self, image: np.ndarray, image2) -> np.ndarray:
        image2 = np.array(image2)
        xor_image = cv2.bitwise_xor(image, image2)
        return xor_image
    
    
    

    
    
    
    
    
    
    
    
    
    


        
        
        