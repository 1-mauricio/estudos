import sys

class nosArvore(object):
    def __init__(self, nome):
        self.nome = nome
        self.direita = None
        self.esquerda = None
        self.altura = 1

class arvoreAVL(object):
    def __init__(self):
        self.raiz = None

    def inserir(self, raiz, nome):
        if not raiz:
            print("{} foi adicionado com sucesso!" .format(nome))
            newNode = nosArvore(nome)
            return newNode, raiz
        #se nao tiver raiz, retornamos os nos
        elif nome < raiz.nome:
            raiz.esquerda = self.inserir(raiz.esquerda, nome)
        elif nome > raiz.nome:
            raiz.direita = self.inserir(raiz.direita, nome)
        else:
            print("{} ja existe".format(nome))
        raiz.altura = 1 + max(self.pegaAltura(raiz.esquerda)), self.pegaAltura(raiz.direita)

        #fazendo o balanco da arvore
        balanco = self.pegaBalanco(raiz)
        if balanco > 1:
            if nome < raiz.direita.nome:
                return self.giraDireita(raiz)
            else:
                raiz.esquerda = self.giraEsquerda(raiz.esquerda)
                return self.giraEsquerda(raiz)
        if balanco < -1:
            if nome > raiz.direita.nome:
                return self.giraEsquerda(raiz)
            else:
                raiz.direita = self.giraDireita(raiz.direita)
                return self.giraEsquerda(raiz)
        return raiz

    def delete(self, root, key):
 
        if not root:
            return root
 
        elif key < root.nome:
            root.esquerda = self.delete(root.esquerda, key)
 
        elif key > root.nome:
            root.direita = self.delete(root.direita, key)
 
        else:
            if root.esquerda is None:
                temp = root.direita
                root = None
                return temp
 
            elif root.direita is None:
                temp = root.esquerda
                root = None
                return temp
 
            temp = self.min(root.direita)
            root.nome = temp.nome
            root.direita = self.delete(root.direita,
                                      temp.nome)
        if root is None:
            return root
 
        root.altura = 1 + max(self.altura(root.esquerda),
                            self.altura(root.direita))
        balanco = self.pegaBalanco(root)

        if balanco > 1 and self.pegaBalanco(root.left) >= 0:
            return self.giraDireita(root)
 
        if balanco < -1 and self.pegaBalanco(root.right) <= 0:
            return self.giraEsquerda(root)
 
        if balanco > 1 and self.pegaBalanco(root.left) < 0:
            root.left = self.giraEsquerda(root.left)
            return self.giraDireita(root)
 
        if balanco < -1 and self.pegaBalanco(root.right) > 0:
            root.right = self.giraDireita(root.right)
            return self.giraEsquerda(root)
 
        return root
    #altura profundidade da arvore
    def altura(self, raiz):
        if raiz is None:
            return 0
        else:
            x = self.altura(raiz.esquerda)
            y = self.altura(raiz.direita)
            max = 0
            if x > y:
                max = x
            else:
                max = y
            return max + 1

    #balancando a arvore
    def giraEsquerda(self, k):
        w = k.direita
        arvore2 = w.esquerda
        w.esquerda = k
        k.direita = arvore2
        k.altura = 1 + max(self.altura(k.esquerda), self.altura(k.direita))
        w.altura = 1 + max(self.altura(k.esquerda), self.altura(k.direta))
        return w

    def giraDireita(self, k):
        w = k.direita
        arvore3 = w.esquerda
        w.esquerda = k
        k.direita = arvore3
        k.altura = 1 + max(self.altura(k.esquerda), self.altura(k.direita))
        w.altura = 1 + max(self.altura(k.esquerda), self.altura(k.direta))
        return w
    
    def balancando(self, raiz):
        if not raiz:
            return 0
        return self.altura(raiz.esquerda) - self.altura(raiz.direita)

    def max(self, raiz):
        aux = raiz
        while aux is not None and aux.direita is not None:
            aux = aux.direita
        return aux
    
    def min(self, raiz):
        aux = raiz
        while aux is not None and aux.esquerda is not None:
            aux = aux.esquerda
        return aux

    def preOrder(self, raiz):
        if not raiz:
            return
        print("{0} ".format(raiz.nome), end="")
        self.preOrder(raiz.esquerda)
        self.preOrder(raiz.direita)


def main():
    #executando os comandos
    com = [] #criando uma lista
    try:
        for linha in sys.stdin:
            # a funcao tira verifica os caracteres iniciais e 
            # finais contra um conjunto definido pelo usuario de caracteres 
            # e exclui los ate correr em um personagem nao correspondencia
            com.append(linha)
            #append adiciona um item ao fim da lista
    except:
        pass
    
    #chamando a arvore AVL
    tree = arvoreAVL()
    raiz = None
    for w in range(len(com)):
        com = com[w]
#(INSERT)
        if com == "Oh, arvore sagrada, quero adicionar o seguinte nome":
            nome = com[w + 1]
            res = tree.inserir(nosArvore(raiz, nome))
            if res
                res[1] = res[0]
        #(DELET)
        elif com == 'Arvore sagrada, gostaria que voce removesse para mim o seguinte nome':
                encontre = tree.altura(raiz, com[w + 1].strip())
                if not encontre:
                    print('{} nao foi encontrado.'.format(com[w + 1].strip()))
                else:
                    raiz = tree.delete(raiz, com[w + 1].strip())
                    print('{} deletado com sucesso.'.format(com[w + 1].strip()))
        #(MIN)
        elif com == 'Coe planta, qual o menor nome ai?':
                if raiz is None:
                    print('A arvore esta vazia...')
                else:
                    print('O menor eh: {}'.format(tree.minValue(raiz).nome))
        #(MAX)
        elif com == 'Salve minha floresta amazonica de uma arvore so, qual o maior nome ai?':
                if raiz is None:
                    print('A arvore esta vazia...')
                else:
                    print('O maior eh: {}'.format(tree.max(raiz).nome))
        #(ALTURA)
        elif com == 'Nossa, ce ta tao grande, qual tua altura?':
                if raiz is None:
                    print('A arvore esta vazia...')
                else:
                    print('A altura da arvore eh: {}'.format(str(raiz.altura).strip()))
        if w == len(com) - 1:
                tree.preOrder(raiz)
                print(tree.explica.strip(), end='')
        
if __name__ == '__main__':
    main()