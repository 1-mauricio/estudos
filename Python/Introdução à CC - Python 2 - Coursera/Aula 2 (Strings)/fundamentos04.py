#função que recebe uma lista de strings e devolve o nome mais curto. A função deve ignorar espaços antes e depois do nome e deve devolver o nome "capitalizado, i.e ignorar espaços, apenas com a 1a letra maiuscula"
def mais_curto(lista_de_nomes):
    mais_curto = lista_de_nomes[0].strip()
    for i in range(1, len(lista_de_nomes)-1):
        if len(lista_de_nomes[i].strip())<len(mais_curto):
            mais_curto = lista_de_nomes[i]
    return mais_curto.capitalize().strip()

nomes = []
nome = input("Digite o nome(digite 'parar' para encerrar): ")
while nome != "parar":
    nomes.append(nome)
    nome = input("Digite o nome(digite 'parar' para encerrar): ")
print(f"O nome mais curto é: {mais_curto(nomes)}")
