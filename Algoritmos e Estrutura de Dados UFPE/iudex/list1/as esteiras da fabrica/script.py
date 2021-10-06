import sys

class NoProduto:
    def __init__(self, produto) -> None:
        self.produto = produto
        self.proximo = None
        
class NoEsteiras:
    def __init__(self, esteira, numero):
        self.esteira = esteira
        self.numero = numero
        self.proximo = None
        self.anterior = None

class Lista:
    def __init__(self) -> None:
        self.cabeca = None

    def insert(self, numero):
        novo_node = NoEsteiras(Esteira(), numero)
        if self.cabeca == None:
            self.cabeca = novo_node
        else:
            self.cabeca.anterior = novo_node
            novo_node.proximo = self.cabeca
            self.cabeca = novo_node

    def select(self, numero):
        comparador = self.cabeca
        while comparador != None:
            if comparador.numero == numero:
                return comparador.esteira
            comparador = comparador.proximo

class Esteira:
    def __init__(self) -> None:
        self.primeiro = None
        self.ultimo = None

    def insert(self, produto):
        novo_node = NoProduto(produto)
        if self.primeiro == None:
            self.primeiro = novo_node
            self.ultimo = novo_node
        else:
            self.ultimo.proximo = novo_node
            self.ultimo = novo_node

        print('O produto: ', produto, ' foi adicionado na esteira')

    def remove(self):
        if self.primeiro != None:
            produto = self.primeiro.produto
            self.primeiro = self.primeiro.proximo
            self.tamanho -= 1
            return produto
        else:
            print("Nao ha elementos para empacotar")

    def move(self, esteira_numero):
        if self.primeiro != None:
            produto = self.primeiro.produto
            lista = Lista()
            esteira = lista.select(esteira_numero)
            if esteira.primeiro == None:
                esteira.primeiro = produto
            else:
                esteira.ultimo.proximo = produto
                esteira.ultimo = produto
            print("O produto: ",produto," foi movido para a esteira ",esteira_numero,".")
        else:
            print("Erro ao mover produto.")

    def show(self):
        if self.primeiro != None:
            resultado = ""
            comparador = self.primeiro
            while comparador != None:
                resultado += str(comparador.produto) + " "
                comparador = comparador.proximo 
            print(resultado)
        else:
            print("fila vazia")

if __name__ == "__main__":
    lista = Lista()
    entrada = []
    qtd = 1
    while qtd <= 3:
        lista.insert(str(qtd))
        qtd += 1

    esteira1 = lista.select("1")
    esteira1.insert("Pipoca")
    esteira1.insert("Chocolate")
    esteira1.show()
    esteira1.move("2")
    
    
    '''fabrica[0].remove()
    fabrica[0].insert("Pipoca", 1)
    fabrica[0].insert("Chocolate", 1)
    fabrica[0].show()
    valor = fabrica[0].move()
    fabrica[1].insert(valor, 2)'''
