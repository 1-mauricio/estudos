class Node:
    def __init__(self, nome, valor) -> None:
        self.nome = nome
        self.valor = valor
        self.direita = None
        self.esquerda = None
        self.pai = None

class Arvore:
    def __init__(self) -> None:
        self.raiz = None

    def busca(self, y):
        x = self.raiz
        while x != None and y != x.valor:
            if y < x.valor:
                x = x.esquerda
            else:
                x = x.direita
        return x

    def min_valor(self, x):
        while x.esquerda != None:
            x = x.esquerda
        return x
    
    def max_valor(self, x):
        while x.direita != None:
            x = x.direita
        return x

    def sucessor(self, x):
        if x.direita != None:
            return self.min_valor(x.direita)
        y = x.pai
        while y != None and x == y.direita:
            x = y
            y = y.pai

        return y
        
    def antecessor(self, x):
        if x.esquerda != None:
            return self.max_valor(x.esquerda)
        y = x.pai
        while y != None and x == y.esquerda:
            x = y
            y = y.pai

        return y

    def inserir(self, nome, valor):
        z = Node(nome, valor)
        y = None
        x = self.raiz
        while x != None:
            y = x
            if z.valor < x.valor:
                x = x.esquerda
            elif z.valor > x.valor:
                x = x.direita
            else:
                return 0

        z.pai = y
        if y == None:
            self.raiz = z
        elif z.valor < y.valor:
            y.esquerda = z
        else:
            y.direita = z

if __name__ == "__main__":
    qtd = int(input())
    arvore = Arvore()

    for i in range(qtd):
        comando = input().split()
        if comando[0] == 'ADD':
            check = arvore.inserir(comando[1], int(comando[2]))
            if check != 0:
                print("{} inserido com sucesso!" .format(comando[1]))
            else:
                print("{} ja esta no sistema." .format(comando[1]))
        else:
            x = arvore.busca(int(comando[1]))
            antecessor = arvore.antecessor(x)
            sucessor = arvore.sucessor(x)
            if antecessor == None and sucessor == None: 
                print("Apenas {} existe no sistema..." .format(x.nome))

            elif sucessor == None:
                print("{} e o maior! e logo atras vem {}" .format(x.nome, antecessor.nome))

            elif antecessor == None:
                print("{} e o menor! e logo apos vem {}" .format(x.nome, sucessor.nome))

            else:
                print("{} vem apos {} e antes de {}" .format(x.nome, antecessor.nome, sucessor.nome))