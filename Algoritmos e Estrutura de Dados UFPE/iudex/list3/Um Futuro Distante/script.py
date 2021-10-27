class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.esquerda = None
        self.direita = None
        self.altura = 1

    def profundidade(self):
        prof_esq = 0
        if self.esquerda:
            prof_esq = self.esquerda.profundidade()
        prof_dir = 0
        if self.direita:
            prof_dir = self.direita.profundidade()
        return 1 + max(prof_esq, prof_dir)