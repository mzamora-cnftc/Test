from tkinter import Tk
from ui.ventana_principal import VentanaPrincipal

def main():
    root = Tk()
    root.title("Mi Aplicación Tkinter")
    app = VentanaPrincipal(root)
    root.mainloop()

if __name__ == "__main__":
    main()