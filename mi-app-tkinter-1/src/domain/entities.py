class Cliente:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

class Pedido:
    def __init__(self, id, cliente_id, producto, cantidad):
        self.id = id
        self.cliente_id = cliente_id
        self.producto = producto
        self.cantidad = cantidad