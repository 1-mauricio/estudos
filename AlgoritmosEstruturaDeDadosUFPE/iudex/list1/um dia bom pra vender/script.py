class Node:
    def __init__(self, valor, anterior = None):
        self.valor = valor
        self.anterior = anterior

class Pilha:
    def __init__(self):
        self.topo = None

    def insert(self, valor):
        novo_node = Node(valor, self.topo)
        # novo_node.anterior = self.topo
        self.topo = novo_node

    def remove(self):
        assert self.topo
        self.topo = self.top.anterior

    def info(self):
        topo = self.topo
        comparador = self.topo
        contador = 0
        while comparador != None and topo.valor >= comparador.valor:
            contador += 1
            comparador = comparador.anterior

        print(f"o ultimo valor foi {topo.valor} e hoje e um bom dia para vender ações dos ultimos {contador} dias".upper())

    def __str__(self) -> str:
        output = []
        aux = self.topo
        while aux != None:
            output.append(str(aux.valor) + " ")
            aux = aux.anterior
        
        return output


if __name__ == "__main__":
    pilha = Pilha()
    pilha.insert(32)
    pilha.info()
    pilha.insert(34)
    pilha.info()
    pilha.insert(38)
    pilha.info()
    pilha.insert(15)
    pilha.info()
     