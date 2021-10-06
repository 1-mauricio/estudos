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
        self.topo = novo_node

    def remove(self):
        if self.topo != None:
            self.topo = self.topo.anterior

    def info(self):
        comparador = self.topo
        contador = 0
        while comparador != None and self.topo.valor >= comparador.valor:
            contador += 1
            comparador = comparador.anterior

        print("O ULTIMO VALOR FOI", self.topo.valor, "E HOJE E UM BOM DIA PARA VENDER ACOES DOS ULTIMOS", contador, "DIAS")
        

if __name__ == '__main__':
    pilha = Pilha()
    i = 0
    try:
        for line in sys.stdin:
            if i == 0:
                qtd_comandos = int(line)
                '''if qtd_comandos >= 997 or qtd_comandos <= 5:
                    exit()'''
                i = 1
            else:
                if i <= qtd_comandos:
                    entrada = line.split()
                    comando = entrada[0]
                    qtd = int(entrada[-1])
                    if comando == 'ATUALIZA':
                        '''if qtd <= 485 and qtd >= 1:'''
                        pilha.insert(qtd)
                    else:
                        pilha.info()
                    
                    i += 1

    except:
        pass