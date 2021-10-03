import sys

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
        self.topo = self.topo.anterior

    def info(self):
        topo = self.topo
        comparador = self.topo
        contador = 0
        while comparador != None and topo.valor >= comparador.valor:
            contador += 1
            comparador = comparador.anterior

        print(f"o ultimo valor foi {topo.valor} e hoje e um bom dia para vender acoes dos ultimos {contador} dias".upper())

    def __str__(self) -> str:
        output = []
        aux = self.topo
        while aux != None:
            output.append(str(aux.valor) + " ")
            aux = aux.anterior
        
        return output

if __name__ == "__main__":
    lista = []
    pilha = Pilha()
    try:
        for line in sys.stdin:
            lista.append(line)
    except:
        pass

    qtd_comandos = int(lista[0])
    i = 1
    while i <= qtd_comandos:
        line = lista[i].split()
        comando = line[0]
        qtd = line[-1]
        if comando == "ATUALIZA":
            pilha.insert(int(qtd))
        else:
            pilha.info()
        i += 1
     