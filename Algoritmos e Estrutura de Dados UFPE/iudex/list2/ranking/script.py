class Pessoa:
    def __init__(self, nome, pontuacao) -> None:
        self.nome = nome
        self.pontuacao = pontuacao
        self.predecessor = None
        self.sucessor = None

class Ranking:
    def __init__(self) -> None:
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    def add(self, nome, pontuacao):
        pessoa = Pessoa(nome, pontuacao)
        if self.primeiro == None:
            self.primeiro = pessoa
            self.ultimo = pessoa
            self.tamanho += 1
            return print("{} inserido com sucesso!" .format(nome))
        else:
            aux = self.primeiro
            for i in range(self.tamanho+1):
                if aux.pontuacao < pontuacao:
                    if aux == self.primeiro:
                        aux.sucessor = pessoa
                        self.primeiro = pessoa
                    else:
                        sucessor = aux.sucessor
                        sucessor.predecessor = pessoa
                        pessoa.sucessor = aux.sucessor
                        aux.sucessor = pessoa
                    pessoa.predecessor = aux
                    self.tamanho += 1
                    return print("{} inserido com sucesso!" .format(nome))
                
                elif aux.nome == nome:
                    return print("{} ja esta no sistema." .format(nome))

                elif aux.predecessor == None:
                    aux.predecessor = pessoa
                    pessoa.sucessor = aux
                    self.tamanho += 1

                else:    
                    aux = aux.predecessor
                    
    def show(self):
        aux = self.primeiro
        for i in range(self.tamanho):
            print(aux.nome, aux.pontuacao)
            aux = aux.predecessor

    def prox(self, pontuacao):
        aux = self.primeiro
        for i in range(self.tamanho):
            if aux.pontuacao == pontuacao:
                if self.tamanho == 1:
                    return print("Apenas {} existe no sistema..." .format(self.primeiro.nome))

                elif aux == self.primeiro:
                    return print("{} e o maior! e logo atras vem {}" .format(aux.nome, aux.predecessor.nome))

                elif aux.predecessor == None:
                    return print("{} e o menor! e logo apos vem {}" .format(aux.nome, aux.sucessor.nome))

                else:
                    return print("{} vem apos {} e antes de {}" .format(aux.nome, aux.predecessor.nome, aux.sucessor.nome))
            aux = aux.predecessor

if __name__ == '__main__':
    qtd = int(input())
    ranking = Ranking()

    for i in range(qtd):
        comando = input().split()
        if comando[0] == 'ADD':
            ranking.add(comando[1], int(comando[2]))
        else:
            ranking.prox(int(comando[1]))

    '''rank = Ranking()
    rank.add("ana", 2)
    rank.add("ana", 2)
    rank.add("bob", 3)
    rank.add("carlos", 6)
    rank.add("daniel", 4)
    rank.add("elisa", 5)
    rank.show()
    rank.prox(2)
    rank.prox(4)
    rank.prox(6)'''

     