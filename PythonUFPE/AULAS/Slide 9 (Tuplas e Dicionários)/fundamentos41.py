tab = {}
n = 0
cod = int(input("Digite o código do curso(0 para parar): "))
while cod < 1:
    cod = int(input("Inválido. Digite o código do curso(0 para parar): "))

while cod != 0 :
    nome = input("Digite o nome do Curso: ")
    codCen = int(input("Digite o código centro: "))
    while codCen < 1:
        codCen = int(input("Inválido. Digite o código do centro(deve ser positivo): "))

    tab[cod] = (nome,codCen)
    n += 1

    cod = int(input("\nDigite o código do curso(0 para parar): "))
    while (cod < 0) or (cod in tab):
        cod = int(input("Inválido. Digite o código do curso(0 para parar): "))

print(f'\nTabela com {n} cursos lida corretamente:\n')

codCen = int(input("Digite o centro que deseja procurar(0 para parar): "))
while codCen < 0:
        codCen = int(input("Inválido. Digite o código do centro novamente(deve ser positivo): "))

while codCen > 0:
    qtd = 0
    print(f"Cursos do centro {codCen}:")
    for ch in tab:
        if codCen == tab[ch][1]:
            qtd += 1
            print(f'   Código: {ch}; Nome: {tab[ch][0]}')
    if qtd == 0:
        print("   Nenhum curso encontrado")
            

    codCen = int(input("Digite o centro que deseja procurar: "))

print("Fim do programa")