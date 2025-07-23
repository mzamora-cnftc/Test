import tkinter as tk
from ui.ventana_principal import VentanaPrincipal

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gestión de Clientes y Pedidos")
    app = VentanaPrincipal(root)
    root.mainloop()