pessoas = []
qtd = 0
continuar = False

cod = input("Digite o código(5 caracteres). Digite 'FIM' para encerrar: ")
while len(cod) != 5:
    cod = input("Digite o código(5 caracteres). Digite 'FIM' para encerrar: ")

while not continuar and qtd<501:
    qtd += 1
    
    nome = input("Digite o nome: ")
    carg = int(input("Digite a carga horária(positivo): "))
    while carg < 1:
        carg = int(input("Inválido. Digite a carga horária(positivo): "))
    num = int(input("Digite o número de créditos(positivo): "))
    while num < 1:
        num = int(input("Inválido. Digite o número de créditos(positivo): "))

    pessoas[cod] = (nome, carg, num)

    cod = input("Digite o código(5 caracteres). Digite 'FIM' para encerrar: ")
    if 'FIM' in cod:
        continuar = True
        


pref = input("Digite o prefixo do codigo, com menos de 5 carac: ")
soma = 0
qtd = 0

for pessoa in pessoas.items():
    if pref == pessoas[pessoa][0]:
        print(pessoa['cod'], pessoa['nome'], pessoa['carg'], pessoa[num])
        soma += cod
        qtd += 1

media = soma / qtd

print(f"A média das cargas horárias é: {media}")
