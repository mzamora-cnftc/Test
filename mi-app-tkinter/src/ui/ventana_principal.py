class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("Mi Aplicación Tkinter")
        self.master.geometry("400x300")
        self.configurar_widgets()

    def configurar_widgets(self):
        self.label = Label(self.master, text="¡Bienvenido a Mi Aplicación!")
        self.label.pack(pady=20)

        self.boton_salir = Button(self.master, text="Salir", command=self.master.quit)
        self.boton_salir.pack(pady=10)

    def manejar_evento(self, evento):
        # Aquí puedes manejar eventos adicionales
        pass