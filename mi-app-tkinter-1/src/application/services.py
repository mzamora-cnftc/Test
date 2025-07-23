from domain.entities import Cliente, Pedido

class ClienteService:
    def __init__(self, repo):
        self.repo = repo

    def registrar(self, nombre, email):
        cliente = Cliente(None, nombre, email)
        self.repo.add(cliente)

    def modificar(self, id, nombre, email):
        cliente = Cliente(id, nombre, email)
        self.repo.update(cliente)

    def eliminar(self, id):
        self.repo.delete(id)

    def listar(self):
        return self.repo.list()

class PedidoService:
    def __init__(self, repo):
        self.repo = repo

    def registrar(self, cliente_id, producto, cantidad):
        pedido = Pedido(None, cliente_id, producto, cantidad)
        self.repo.add(pedido)

    def modificar(self, id, cliente_id, producto, cantidad):
        pedido = Pedido(id, cliente_id, producto, cantidad)
        self.repo.update(pedido)

    def eliminar(self, id):
        self.repo.delete(id)

    def listar(self):
        return self.repo.list()