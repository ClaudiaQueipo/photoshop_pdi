import typing
import tkinter as tk
import customtkinter as ctk
from customtkinter import filedialog

from PIL import Image, ImageTk

from meta.singleton_meta import SingletonMeta
from photoshop import Photoshop

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")



class MainApp(ctk.CTk, metaclass=SingletonMeta):
    def __init__(self, title: str, geometry: str):
        super().__init__()

        self.image = None
        self.image_path = None
        self.image_modified = None
        self.image_ar = 0
        self.title(title)
        self.geometry(geometry)
        self.build_ui()
        self.photoshop= Photoshop()
        

    def build_ui(self):
        """Builds the user interface for the image processing application.
        Args:
            self: The instance of the ImageProcessingApp class to which this function belongs.

        Returns:
            None.
        """
        
        self.top_menu = ctk.CTkFrame(self, height=40)
        self.bottom_menu = ctk.CTkFrame(self, height=40)

        top_menu_buttons: list[tuple[str, typing.Callable]] = [
            ("Abrir", self.open_image),
            ("Guardar", self.save_image),
            ("Quitar", self.close_image),
            ("Salir", self.exit),
        ]

        for label, callback in top_menu_buttons[:-1]:
            button = ctk.CTkButton(
                self.top_menu, width=90, text=label, command=callback,
                fg_color="#653780", hover_color="#772AB8"
            )
            button.pack(pady=8, padx=8, side=tk.LEFT, anchor=tk.CENTER)

        button = ctk.CTkButton(
            self.top_menu,
            width=90,
            text=top_menu_buttons[-1][0],
            command=top_menu_buttons[-1][1],
            fg_color="#A52A2A",
            hover_color="#800020",
        )
        button.pack(pady=8, padx=8, side=tk.RIGHT, anchor=tk.CENTER)

        self.left_panel = ctk.CTkFrame(self)
        self.image_panel = ctk.CTkFrame(self, width=400, height=400)

        buttons: list[tuple[str, tuple(typing.Any, ...), typing.Callable]] = [
            ("Brightness", ("button", None), self.brightness_callback),
            ("Contrast", ("button", None), self.contrast_callback),
            ("Flip", ("button", None), self.flip_callback),
            ("Mirror", ("button", None), self.mirror_callback),
            ("Rotate", ("button", None), self.rotate_callback),
            ("Blur", ("button", None), self.blur_callback),
            ("Sumar", ("button", None), self.sum_callback),
            ("Restar", ("button", None), self.subtract_callback),
            ("Op Lógicas", ("popup_button", ["AND", "OR", "XOR", "NOT"]), 
                {"AND": self.and_callback, 
                 "OR": self.or_callback, 
                 "XOR": self.xor_callback, 
                 "NOT": self.not_callback}),
            ("Deshacer", ("button", None), self.revert),
        ]

        def popup_callback_wrapper(option):
            """Esta función se encarga de llamar a la función de llamada 
            de retorno correspondiente para una opción de menú emergente seleccionada."""
            if option in callback_map:
                callback_map[option]()

        for label, type, callback in buttons:
            if type[0] == "popup_button":
                callback_map = callback
                button = ctk.CTkOptionMenu(
                    self.left_panel, width=90, command=popup_callback_wrapper, values=[label]+type[1],
                    fg_color="#653780", dropdown_fg_color="#653780", 
                    button_color="#3F1651", button_hover_color="#653780"
                )
                button.pack(pady=8, padx=18, side=tk.TOP, anchor=tk.CENTER)
                continue

            button = ctk.CTkButton(
                self.left_panel, width=90, text=label, command=callback, fg_color="#653780", hover_color="#772AB8"  
            )
            button.pack(pady=8, padx=18, side=tk.TOP, anchor=tk.CENTER)

        self.slider = ctk.CTkSlider(master=self.bottom_menu, from_=-100, to=100, command=self.update_slider_value,
                               fg_color="#653780", button_color="#9C3587", button_hover_color="#E53F71")
        self.slider.set(0)
        self.slider.pack(side=tk.BOTTOM, anchor=tk.CENTER)
            
        self.slider_var = tk.StringVar()
        self.slider_var.set("0")    
        
        self.slider_label = ctk.CTkLabel(self.bottom_menu, textvariable=self.slider_var,corner_radius=8)
        self.slider_label.pack(side=tk.BOTTOM, anchor=tk.CENTER)
                  
        self.top_menu.pack(side=tk.TOP, fill=tk.X)
        self.bottom_menu.pack(side=tk.BOTTOM, fill=tk.X)
        self.left_panel.pack(side=tk.LEFT, anchor=tk.CENTER)
        self.image_panel.pack(
            padx=40, pady=40, side=tk.RIGHT, fill=tk.BOTH, expand=True
        )
    
    def open_image(self):
        """Opens a dialog window to select an image and displays it in the
            graphical user interface.
           The selected image is resized to fit the size of the image panel
            and stored as a copy in the image_modified variable.
        """
        
        file_types = (("Imágenes", "*.png *.jpg *.jpeg *.gif *.bmp"),)

        image_path = filedialog.askopenfilename(
            title="Abrir imagen", filetypes=file_types
        )
        image = Image.open(image_path)
        w, h = self.image_panel.winfo_width(), self.image_panel.winfo_height()
        image.thumbnail((w, h), Image.LANCZOS)
        
        self.image_modified=image.copy()
        
        image_tk = ImageTk.PhotoImage(image)

        if self.image:
            self.image.pack_forget()

        self.image_path=image_path
        self.image = tk.Label(self.image_panel, image=image_tk)
        self.image.image = image_tk
        self.image.pack(padx=8, pady=8, side=tk.TOP, expand=True)
    
    def save_image(self):
        """Resizes the modified image to the dimensions of the original 
            image and saves the modified image to a file.
           Opens a dialog window to select the output file path and name.
        """
        reference_image = Image.open(self.image_path)
        ref_width, ref_height = reference_image.size

        self.image_modified = self.image_modified.resize((ref_width, ref_height), Image.LANCZOS)

        savefile = filedialog.asksaveasfile(defaultextension=".jpg")
        self.image_modified.save(savefile)
    
    def put_image(self, image):
        """
         Updates the image displayed in the GUI with the given image. Resizes the image to fit the dimensions of the image panel. 
        """
        
        
        w, h = self.image_panel.winfo_width(), self.image_panel.winfo_height()
        image.thumbnail((w, h), Image.LANCZOS)
        
        image_tk = ImageTk.PhotoImage(image)

        
        self.image.image=image_tk
        self.image.configure(image=image_tk)

    def close_image(self):
        """
            Removes the currently displayed image from the GUI. 
        """
        if self.image:
            self.image.pack_forget()
            self.image = None

    def exit(self):
        self.destroy()

    def revert(self):
        self.image_modified = Image.open(self.image_path)
        
        self.put_image(self.image_modified)

 
    def reset_slider(self):
        self.slider.set(0)
        self.slider_var.set("0")
    
    def update_slider_value(self, value):
        self.slider_var.set(int(value))
    
    def brightness_callback(self):
        bright = int(self.slider_var.get())
        
        image = None
        
        image = self.photoshop.adjust_brightness(self.image_modified, bright)
                   
        
        self.image_modified = image.copy()

        self.reset_slider()
        self.put_image(self.image_modified)

    def contrast_callback(self):
        con = int(self.slider_var.get())
        
        image = self.photoshop.adjust_contrast(self.image_modified, con)
        self.image_modified=image.copy()

        self.reset_slider()
        self.put_image(image)
    
    def flip_callback(self):
        
        image = self.photoshop.image_flip(self.image_modified)
        self.image_modified=image

        self.put_image(image)
    
    def mirror_callback(self):
        
        image = self.photoshop.image_mirror(self.image_modified)
        self.image_modified=image

        self.put_image(image)
    
    def rotate_callback(self):
        
        image = self.photoshop.image_rotate(self.image_modified)
        self.image_modified=image

        self.put_image(image)
    
    def blur_callback(self):
        
        image = self.photoshop.median_blur(self.image_modified)
        self.image_modified=image

        self.put_image(image)
    
    def sum_callback(self):
        filename = filedialog.askopenfilename(initialdir='/', title='Seleccionar imagen', filetypes=(
        ('Archivos de imagen', '*.png *.jpg *.jpeg *.gif *.bmp'), ('Todos los archivos', '*.*')))

        image = Image.open(filename)
        w_modified, h_modified = self.image_modified.size

        image = image.resize((w_modified, h_modified), Image.LANCZOS)
        
        image = self.photoshop.sum(self.image_modified, image)
        self.image_modified=image

        self.put_image(image)
    
    def subtract_callback(self):
        filename = filedialog.askopenfilename(initialdir='/', title='Seleccionar imagen', filetypes=(
        ('Archivos de imagen', '*.png *.jpg *.jpeg *.gif *.bmp'), ('Todos los archivos', '*.*')))

        image = Image.open(filename)
        w_modified, h_modified = self.image_modified.size

        image = image.resize((w_modified, h_modified), Image.LANCZOS)
        
        image = self.photoshop.subtract(self.image_modified, image)
        self.image_modified=image

        self.put_image(image)
    
        
    def not_callback(self):
        image = self.photoshop.lo_not(self.image_modified)
        self.image_modified=image

        self.put_image(image)
    

    def and_callback(self):
        filename = filedialog.askopenfilename(initialdir='/', title='Seleccionar imagen', filetypes=(
        ('Archivos de imagen', '*.png *.jpg *.jpeg *.gif *.bmp'), ('Todos los archivos', '*.*')))

        image = Image.open(filename)

        w_modified, h_modified = self.image_modified.size

        image = image.resize((w_modified, h_modified), Image.LANCZOS)

        image = self.photoshop.lo_and(self.image_modified, image)

        self.image_modified = image

        self.put_image(image)

    
    def or_callback(self):
        filename = filedialog.askopenfilename(initialdir='/', title='Seleccionar imagen', filetypes=(
        ('Archivos de imagen', '*.png *.jpg *.jpeg *.gif *.bmp'), ('Todos los archivos', '*.*')))

        image = Image.open(filename)
        w_modified, h_modified = self.image_modified.size

        image = image.resize((w_modified, h_modified), Image.LANCZOS)
        image = self.photoshop.lo_or(self.image_modified,image)
        
        self.image_modified=image
        
        self.put_image(image)

    
    def xor_callback(self):
        filename = filedialog.askopenfilename(initialdir='/', title='Seleccionar imagen', filetypes=(
        ('Archivos de imagen', '*.png *.jpg *.jpeg *.gif *.bmp'), ('Todos los archivos', '*.*')))

        image = Image.open(filename)
        w_modified, h_modified = self.image_modified.size

        image = image.resize((w_modified, h_modified), Image.LANCZOS)

        image = self.photoshop.lo_xor(self.image_modified,image)
        
        self.image_modified=image

        self.put_image(image)
