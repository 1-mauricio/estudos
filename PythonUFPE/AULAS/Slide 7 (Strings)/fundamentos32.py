# Ler o nome do usuário e imprimi-lo em formato de
# escala, ou seja, só a primeira letra na primeira linha,
# as duas primeiras letras na segunda linha, e assim por diante.

name = input("Digite seu nome: ")

for c in range(0, len(name)):
    if name[c] != " ":
        print(name[0:c+1])