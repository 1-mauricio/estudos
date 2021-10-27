import sys

class Node:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.altura = 1
        self.esquerda = None
        self.direita = None

class Arvore:
    def min_valor(self, node):
        if node is None or node.esquerda is None:
            return node
    
    def max_valor(self, node):
        while node.direita != None:
            node = node.direita
        return node.nome

    def inserir(self, node, nome):
        if node == None:
            print("{} foi adicionado com sucesso!" .format(nome))
            newNode = Node(nome)
            return newNode
        elif nome < node.nome:
            node.esquerda = self.inserir(node.esquerda, nome)
        elif nome > node.nome:
            node.direita = self.inserir(node.direita, nome)
        else:
            print("{} ja existe." .format(nome))
            return node

        node.altura = 1 + max(self.profundidade(node.esquerda),
                           self.profundidade(node.direita))
 
        balance = self.balanco(node)
 
        if balance > 1 and nome < node.esquerda.nome:
            return self.rotacao_direita(node)
 
        if balance < -1 and nome > node.direita.nome:
            return self.rotacao_esquerda(node)
 
        if balance > 1 and nome > node.esquerda.nome:
            node.esquerda = self.rotacao_esquerda(node.esquerda)
            return self.rotacao_direita(node)
 
        if balance < -1 and nome < node.direita.nome:
            node.direita = self.rotacao_direita(node.direita)
            return self.rotacao_esquerda(node)
 
        return node

    def deletar(self, node, nome):
        if not node:
            print('{} deletado com sucesso.' .format(nome))
            return node
 
        elif nome < node.nome:
            node.esquerda = self.deletar(node.esquerda, nome)
 
        elif nome > node.nome:
            node.direita = self.deletar(node.direita, nome)
 
        else:
            if node.esquerda is None:
                temp = node.direita
                node = None
                print('{} deletado com sucesso.' .format(nome))
                return temp
 
            elif node.direita is None:
                temp = node.esquerda
                node = None
                print('{} deletado com sucesso.' .format(nome))
                return temp
 
            temp = self.min_valor(node.direita)
            node.nome = temp.nome
            node.direita = self.deletar(node.direita,
                                      temp.nome)

            if node is None:
                print('{} nao foi encontrado.' .format(nome))
                return node

            node.altura = 1 + max(self.profundidade(node.esquerda),
                                self.profundidade(node.direita))
    
            balance = self.balanco(node)
    
            if balance > 1 and self.balanco(node.esquerda) >= 0:
                return self.rotacao_direita(node)
    
            if balance < -1 and self.balanco(node.direita) <= 0:
                return self.rotacao_esquerda(node)
    
            if balance > 1 and self.balanco(node.left) < 0:
                node.left = self.rotacao_esquerda(node.left)
                return self.rotacao_direita(node)
    
            if balance < -1 and self.balanco(node.direita) > 0:
                node.direita = self.rotacao_direita(node.direita)
                return self.rotacao_esquerda(node)
    
            return node

    def rotacao_esquerda(self, z):
 
        y = z.direita
        T2 = y.esquerda
 
        y.esquerda = z
        z.direita = T2
 
        z.altura = 1 + max(self.profundidade(z.esquerda),
                         self.profundidade(z.direita))
        y.altura = 1 + max(self.profundidade(y.esquerda),
                         self.profundidade(y.direita))
 
        return y
 
    def rotacao_direita(self, z):
 
        y = z.esquerda
        T3 = y.direita
 
        y.direita = z
        z.esquerda = T3
 
        z.altura = 1 + max(self.profundidade(z.esquerda),
                        self.profundidade(z.direita))
        y.altura = 1 + max(self.profundidade(y.esquerda),
                        self.profundidade(y.direita))
 
        return y
 
    def profundidade(self, node):
        if not node:
            return 0
 
        return node.altura
 
    def balanco(self, node):
        if not node:
            return 0
 
        return self.profundidade(node.esquerda) - self.profundidade(node.direita)

if __name__ == "__main__":
    entrada = []
    try:
        for line in sys.stdin:
            if line != '':
                line = line.strip()
                entrada.append(line)
    except:
        pass

    qtd_comandos = entrada[0]
    node = None
    arvore = Arvore()
    
    for i in range(1, len(entrada)):
        comando = entrada[i]
        if comando == 'Oh, arvore sagrada, quero adicionar o seguinte nome':
            nome = entrada[i+1]
            node = arvore.inserir(node, nome)

        elif comando == 'Arvore sagrada, gostaria que voce removesse para mim o seguinte nome':
            nome = entrada[i+1]
            node = arvore.deletar(node, nome)

        elif comando == 'Coe planta, qual o menor nome ai?':
            menor = arvore.min_valor(node)
            print('O menor eh: {}' .format(menor.nome))

        elif comando == 'Salve minha floresta amazonica de uma arvore so, qual o maior nome ai?':
            maior = arvore.max_valor(node)
            print('O maior eh: {}' .format(maior))

        elif comando == 'Nossa, ce ta tao grande, qual tua altura?':
            altura = node.altura
            print('A altura da arvore eh: {}' .format(altura))

    out = 'PRE-ORDER DA ARVORE:'
    def preOrder(node, out):
 
        if not node:
            return

        out += node.nome + " "
        preOrder(node.esquerda)
        preOrder(node.direita)

        return out

    
    preOrder(node, out)
    print(out, end="")
    