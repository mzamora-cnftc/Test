from application.services import ClienteService, PedidoService
from infrastructure.sqlite_repository import SqliteClienteRepository, SqlitePedidoRepository
from openpyxl import Workbook
import tkinter as tk
from tkinter import ttk, messagebox

class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        master.title("Ventana Principal")
        master.geometry("400x300")
        self.cliente_service = ClienteService(SqliteClienteRepository())
        self.pedido_service = PedidoService(SqlitePedidoRepository())
        self.crear_widgets()

    def crear_widgets(self):
        # Frame Clientes
        frame_c = tk.LabelFrame(self.master, text="Clientes")
        frame_c.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        tk.Label(frame_c, text="Nombre:").grid(row=0, column=0)
        tk.Label(frame_c, text="Email:").grid(row=1, column=0)
        self.nombre = tk.Entry(frame_c)
        self.email = tk.Entry(frame_c)
        self.nombre.grid(row=0, column=1)
        self.email.grid(row=1, column=1)
        tk.Button(frame_c, text="Registrar", command=self.registrar_cliente).grid(row=2, column=0)
        tk.Button(frame_c, text="Modificar", command=self.modificar_cliente).grid(row=2, column=1)
        tk.Button(frame_c, text="Eliminar", command=self.eliminar_cliente).grid(row=2, column=2)
        self.tree_clientes = ttk.Treeview(frame_c, columns=("id", "nombre", "email"), show="headings")
        for col in ("id", "nombre", "email"):
            self.tree_clientes.heading(col, text=col)
        self.tree_clientes.grid(row=3, column=0, columnspan=3)
        self.tree_clientes.bind("<<TreeviewSelect>>", self.seleccionar_cliente)

        # Frame Pedidos
        frame_p = tk.LabelFrame(self.master, text="Pedidos")
        frame_p.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        tk.Label(frame_p, text="Cliente ID:").grid(row=0, column=0)
        tk.Label(frame_p, text="Producto:").grid(row=1, column=0)
        tk.Label(frame_p, text="Cantidad:").grid(row=2, column=0)
        self.cliente_id = tk.Entry(frame_p)
        self.producto = tk.Entry(frame_p)
        self.cantidad = tk.Entry(frame_p)
        self.cliente_id.grid(row=0, column=1)
        self.producto.grid(row=1, column=1)
        self.cantidad.grid(row=2, column=1)
        tk.Button(frame_p, text="Registrar", command=self.registrar_pedido).grid(row=3, column=0)
        tk.Button(frame_p, text="Modificar", command=self.modificar_pedido).grid(row=3, column=1)
        tk.Button(frame_p, text="Eliminar", command=self.eliminar_pedido).grid(row=3, column=2)
        self.tree_pedidos = ttk.Treeview(frame_p, columns=("id", "cliente_id", "producto", "cantidad"), show="headings")
        for col in ("id", "cliente_id", "producto", "cantidad"):
            self.tree_pedidos.heading(col, text=col)
        self.tree_pedidos.grid(row=4, column=0, columnspan=3)
        self.tree_pedidos.bind("<<TreeviewSelect>>", self.seleccionar_pedido)
        # Botón reporte
        tk.Button(self.master, text="Generar reporte Excel", command=self.generar_reporte).grid(row=2, column=0, pady=10)
        self.listar_clientes()
        self.listar_pedidos()

    # CLIENTES
    def registrar_cliente(self):
        nombre = self.nombre.get()
        email = self.email.get()
        if not nombre or not email:
            messagebox.showerror("Error", "Campos obligatorios")
            return
        self.cliente_service.registrar(nombre, email)
        self.listar_clientes()
        self.nombre.delete(0, tk.END)
        self.email.delete(0, tk.END)

    def modificar_cliente(self):
        selected = self.tree_clientes.selection()
        if not selected:
            messagebox.showerror("Error", "Seleccione un cliente")
            return
        cliente_id = self.tree_clientes.item(selected[0])["values"][0]
        nombre = self.nombre.get()
        email = self.email.get()
        if not nombre or not email:
            messagebox.showerror("Error", "Campos obligatorios")
            return
        self.cliente_service.modificar(cliente_id, nombre, email)
        self.listar_clientes()
        self.nombre.delete(0, tk.END)
        self.email.delete(0, tk.END)

    def eliminar_cliente(self):
        selected = self.tree_clientes.selection()
        if not selected:
            messagebox.showerror("Error", "Seleccione un cliente")
            return
        cliente_id = self.tree_clientes.item(selected[0])["values"][0]
        self.cliente_service.eliminar(cliente_id)
        self.listar_clientes()

    def listar_clientes(self):
        for i in self.tree_clientes.get_children():
            self.tree_clientes.delete(i)
        for cliente in self.cliente_service.listar():
            self.tree_clientes.insert("", tk.END, values=(cliente.id, cliente.nombre, cliente.email))

    def seleccionar_cliente(self, event):
        selected = self.tree_clientes.selection()
        if selected:
            values = self.tree_clientes.item(selected[0])["values"]
            self.nombre.delete(0, tk.END)
            self.email.delete(0, tk.END)
            self.nombre.insert(0, values[1])
            self.email.insert(0, values[2])
            self.cliente_id.delete(0, tk.END)
            self.cliente_id.insert(0, values[0])

    # PEDIDOS
    def registrar_pedido(self):
        cliente_id = self.cliente_id.get()
        producto = self.producto.get()
        cantidad = self.cantidad.get()
        if not cliente_id or not producto or not cantidad:
            messagebox.showerror("Error", "Campos obligatorios")
            return
        self.pedido_service.registrar(cliente_id, producto, cantidad)
        self.listar_pedidos()
        self.producto.delete(0, tk.END)
        self.cantidad.delete(0, tk.END)

    def modificar_pedido(self):
        selected = self.tree_pedidos.selection()
        if not selected:
            messagebox.showerror("Error", "Seleccione un pedido")
            return
        pedido_id = self.tree_pedidos.item(selected[0])["values"][0]
        cliente_id = self.cliente_id.get()
        producto = self.producto.get()
        cantidad = self.cantidad.get()
        self.pedido_service.modificar(pedido_id, cliente_id, producto, cantidad)
        self.listar_pedidos()

    def eliminar_pedido(self):
        selected = self.tree_pedidos.selection()
        if not selected:
            messagebox.showerror("Error", "Seleccione un pedido")
            return
        pedido_id = self.tree_pedidos.item(selected[0])["values"][0]
        self.pedido_service.eliminar(pedido_id)
        self.listar_pedidos()

    def listar_pedidos(self):
        for i in self.tree_pedidos.get_children():
            self.tree_pedidos.delete(i)
        for pedido in self.pedido_service.listar():
            self.tree_pedidos.insert("", tk.END, values=(pedido.id, pedido.cliente_id, pedido.producto, pedido.cantidad))

    def seleccionar_pedido(self, event):
        selected = self.tree_pedidos.selection()
        if selected:
            values = self.tree_pedidos.item(selected[0])["values"]
            self.cliente_id.delete(0, tk.END)
            self.producto.delete(0, tk.END)
            self.cantidad.delete(0, tk.END)
            self.cliente_id.insert(0, values[1])
            self.producto.insert(0, values[2])
            self.cantidad.insert(0, values[3])

    # REPORTE
    def generar_reporte(self):
        # Usar los servicios para obtener los datos relacionados
        clientes = {c.id: c for c in self.cliente_service.listar()}
        pedidos = self.pedido_service.listar()
        wb = Workbook()
        ws = wb.active
        ws.append(["Nombre Cliente", "Email", "Producto", "Cantidad"])
        for pedido in pedidos:
            cliente = clientes.get(pedido.cliente_id)
            if cliente:
                ws.append([cliente.nombre, cliente.email, pedido.producto, pedido.cantidad])
        wb.save("reporte_clientes_pedidos.xlsx")
        messagebox.showinfo("Reporte", "Reporte generado como reporte_clientes_pedidos.xlsx")