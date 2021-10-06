class NoLista:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.proximo = None
        self.anterior = None

class Pokemon:
    def __init__(self):
        self.primeiro = None

    def insert(self, nome, idade):
        novo_node = Node(nome, idade)
        self.primeiro = novo_node


def InsereElemento(noInicio, nome, idade):
    no = NoLista(nome, idade)
    no.proximo = noInicio
    if noInicio != None:
        noInicio.anterior = no
    noInicio = no
    no.anterior = None

    return no

def ImprimeTodos(noInicio):
    x = noInicio
    print("Pokemons Cadastrados")
    while x != None:
        print(x.nome)
        x = x.proximo

    return x

def procurarElementos(noInicio, nome):
    x = noInicio
    while x != None and x.nome != nome:
        x = x.proximo

    return x

def removerElemento(noInicio, nome):
    elemento = procurarElementos(noInicio)
    if elemento.anterior != None:
        elemento.anterior.proximo = elemento.proximo
    else:
        noInicio = elemento.proximo
    if (elemento.proximo != None):
        elemento.proximo.anterior = elemento.anterior

    return noInicio

noInicio = None
while (True):
    entrada = int(input(""))