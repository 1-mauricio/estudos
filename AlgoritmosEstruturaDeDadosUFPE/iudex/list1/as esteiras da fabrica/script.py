class Node:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.proximo = None

class Fila:
    def __init__(self) -> None:
        self.primeiro = None
        self.ultimo = None

    def insert(self, valor):
        novo_node = Node(valor)
        if self.primeiro == None:
            self.primeiro = novo_node
            self.ultimo = novo_node
        else:
            self.ultimo.proximo = novo_node
            self.ultimo = novo_node

    def remove(self):
        if self.primeiro != None:
            self.primeiro = self.primeiro.proximo
            if self.primeiro == None:
                self.ultimo = None
        else:
            return f"Não há produtos para empacotar na esteira {}"
    def move(self):
        


if __name__ == "__main__":
    entrada = input()
    for linha in entrada:
        if "INS" in linha:
            lista = linha.split()
            esteira = lista[1]
            codigo = lista[2]
        elif "RMV"

        elif "ENF" in linha