
## Project Description

Our school project is a digital image processing application that utilizes OpenCV, Pillow, and NumPy libraries to process images. The application provides various image processing functionalities such as brightness and contrast adjustment, blur, flip, mirror, rotate, image addition, image subtraction, and logical operations such as AND, OR, NOT, and XOR. 

### Functionalities

- **Brightness and Contrast Adjustment:** Our application allows users to adjust the brightness and contrast of an image

- **Blur:** Our application provides a blur effect to images using OpenCV's cv2.

- **Flip:** Our application allows users to flip an image

- **Mirror:** Our application provides a mirror effect to images  

- **Rotate:** Our application allows users to rotate an image

- **Image Addition and Subtraction:** Our application allows users to add or subtract two images

- **Logical Operations:** Our application provides logical operations such as AND, OR, NOT, and XOR

Overall, our application provides a user-friendly interface for processing digital images with various functionalities using OpenCV, Pillow, and NumPy libraries.

## Requirements

````bash

pip install opencv-python pillow tkinter customtkinter 

````

## Run app

````bash
cd src
````

````bash
python main.py
````
## SOLID PRINCIPLES

The SOLID principle that was applied in this code is the Single Responsibility Principle (SRP) in Photoshop class. Each method has a single responsibility and is responsible for performing a specific task, which makes the code more maintainable and scalable.

## Design Patterns

The Singleton design pattern was applied. This is indicated by the use of the metaclass=SingletonMeta argument in the Photoshop class definition. The Singleton pattern ensures that only one instance of the Photoshop class can exist at any given time, providing global access to this instance throughout the codebase.

