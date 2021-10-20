class Node:
    def __init__(self, valor, anterior = None):
        self.valor = valor
        self.anterior = anterior

class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def insert(self, valor):
        novo_node = Node(valor, self.topo)
        self.topo = novo_node
        self.tamanho += 1

    def remove(self):
        if self.topo != None:
            self.topo = self.topo.anterior

    def info(self, max):
        comparador = self.topo
        if max == self.topo.valor:
            print("O ULTIMO VALOR FOI", self.topo.valor, "E HOJE E UM BOM DIA PARA VENDER ACOES DOS ULTIMOS", self.tamanho, "DIAS")
            return 0

        for i in range(0, self.tamanho):
            if comparador == None or self.topo.valor < comparador.valor:
                print("O ULTIMO VALOR FOI", self.topo.valor, "E HOJE E UM BOM DIA PARA VENDER ACOES DOS ULTIMOS", i, "DIAS")
                return 0
            comparador = comparador.anterior
        
        print("O ULTIMO VALOR FOI", self.topo.valor, "E HOJE E UM BOM DIA PARA VENDER ACOES DOS ULTIMOS", self.tamanho, "DIAS")
        
if __name__ == '__main__':
    pilha = Pilha()

    max = 0
    n = int(input())
    for i in range(n):
        entrada = input().split()
        if entrada[0] == 'ATUALIZA':
            p = int(entrada[-1])
            pilha.insert(p)
            if p > max:
                max = p
        else:
            pilha.info(max)