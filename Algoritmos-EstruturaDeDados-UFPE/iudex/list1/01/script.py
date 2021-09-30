class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Pilha:
    def __init__(self):
        self.top = None

    def insert(self, valor):
        new_node = Node(valor)
        new_node.next = self.top
        self.top = new_node

    def info(self):
        return f"o ultimo valor foi {preco} e hoje e um bom dia para vender acoes dos ultimos {dia} dias"


if __name__ == "__main__":
    pass