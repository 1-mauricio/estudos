class Pessoa:
    #"""Classe pessoa possui nome, endereço e idade"""
    def __init__(self): #construtor dá a possibilidade de configurar ooss atributos com valores iniciais
        #self é defiinniddo para faao próprio objeto recém criado
        ##"""Cria uma nova pessoa com nome, endereco e idade"""
        self.nome = ""
        self.idade = 0
        self.endereco = ""

p1 = Pessoa() #inicialização de um objeto do tipo Pessoa
p2 = Pessoa() #inicialização de outro objeto do tipo Pessoa

print(p1 is p2) #false

p1.nome = "Joao da Silva"
p2.nome = "Maria Meneguel"