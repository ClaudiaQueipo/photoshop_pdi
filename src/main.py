from gui import MainApp

if __name__ == "__main__":
    app = MainApp("Photoshop", "800x600")
    app.eval("tk::PlaceWindow . center")
    app.iconbitmap("assets//icono.ico")
    
    app.mainloop()