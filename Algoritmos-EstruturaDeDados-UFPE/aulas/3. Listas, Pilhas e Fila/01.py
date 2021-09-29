class Pessoa:
    def __init__(self, initNome, initIdade, initEndereco):
        self.nome = initNome
        self.idade = initIdade
        self.endereco = initEndereco

    def imprimeDados(self):
        print(self.nome, self.idade, self.endereco)
    
    def fazAniversario(self):
        self.idade += 1

    def atualizaEndereco(self, novoEndereco):
        self.endereco = novoEndereco

    def retornaAnoNascimento(self):
        return 2021-self.idade

    def getNome(self):
        return self.nome
    
    def setNome(self, novoNome):
        self.nome = novoNome

def moraMesmoEndereco(pessoa1, pessoa2):
    if(pessoa1.endereco == pessoa2.endereco):
        return True
    else:
        return False

p1 = Pessoa("João Pedro da Silva", 20, "Rua Sem Nome")
p2 = Pessoa("Maria Xuxa", 47, "Rua da Nave Espacial")

p1.proximo = p2 #o ponteiro de p1 aponta para p2
p2.proximo = None #o ponteiro de p2 aponta para NULL

print(p1.proximo.nome)