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

p2.fazAniversario()
p2.imprimeDados()

p1.atualizaEndereco("Rua com Nome")
p1.imprimeDados()

print(p2.retornaAnoNascimento())
print(moraMesmoEndereco(p1, p2))