import sqlite3
from domain.entities import Cliente, Pedido

DB = "app.db"

class SqliteClienteRepository:
    def add(self, cliente):
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("INSERT INTO clientes (nombre, email) VALUES (?, ?)", (cliente.nombre, cliente.email))
        conn.commit()
        conn.close()

    def update(self, cliente):
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("UPDATE clientes SET nombre=?, email=? WHERE id=?", (cliente.nombre, cliente.email, cliente.id))
        conn.commit()
        conn.close()

    def delete(self, cliente_id):
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("DELETE FROM clientes WHERE id=?", (cliente_id,))
        conn.commit()
        conn.close()

    def list(self):
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        clientes = []
        for row in c.execute("SELECT * FROM clientes"):
            clientes.append(Cliente(*row))
        conn.close()
        return clientes

class SqlitePedidoRepository:
    def add(self, pedido):
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("INSERT INTO pedidos (cliente_id, producto, cantidad) VALUES (?, ?, ?)", (pedido.cliente_id, pedido.producto, pedido.cantidad))
        conn.commit()
        conn.close()

    def update(self, pedido):
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("UPDATE pedidos SET cliente_id=?, producto=?, cantidad=? WHERE id=?", (pedido.cliente_id, pedido.producto, pedido.cantidad, pedido.id))
        conn.commit()
        conn.close()

    def delete(self, pedido_id):
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("DELETE FROM pedidos WHERE id=?", (pedido_id,))
        conn.commit()
        conn.close()

    def list(self):
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        pedidos = []
        for row in c.execute("SELECT * FROM pedidos"):
            pedidos.append(Pedido(*row))
        conn.close()
        return pedidos