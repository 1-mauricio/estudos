pessoas = []
qtd = 0

cpf = float(input("Digite o cpf(número não positivo para parar): "))
while cpf>0 and qtd < 300:
    pessoa_atual = {}
    pessoa_atual['cpf'] = cpf
    pessoa_atual['nome'] = input("Digite o nome: ")
    pessoa_atual['salario'] = float(input("Digite o salário: "))
    pessoas.append(pessoa_atual)
    qtd += 1
    cpf = float(input("Digite o cpf(número não positivo para parar): "))

limite_inferior = 0
limite_superior = 0
is_correct = False

while not is_correct:
    limite_inferior = float(input("Digite o limite inferior: "))
    limite_superior = float(input("Digite o limite supérior: "))
    if limite_superior < 1 or limite_inferior < 0:
        print("Os limites devem ser positivos!")
    elif limite_superior < limite_inferior:
        print("O limite superior precisa ser maior que o inferior!")
    else:
        is_correct = True


maior_salario = 0
soma_salarios = 0
quantidade_pessoas = 0
aux_cont = 0

print("Se encontram neste intervalo: ")
for pessoa in pessoas:
    if pessoa['salario'] >= limite_inferior and pessoa['salario'] <= limite_superior:
        print(pessoa['nome'], pessoa['cpf'], pessoa['salario'])
        soma_salarios += pessoa['salario']
        quantidade_pessoas += 1
        if pessoa['salario'] > maior_salario:
            maior_salario = pessoa['salario']
    
    if pessoa['salario'] > limite_superior:
        aux_cont += 1

if quantidade_pessoas == 0:
    print('Nenhuma pessoa se encontra nesse intervalo')
    print(f"{aux_cont} pessoas recebem mais do que o limite superior.")
else:
    print(f"{aux_cont} pessoas recebem mais do que o limite superior.")
    print(f"o maior salario vale R$: {maior_salario}")
    print(f"a média dos salários é de R$: {soma_salarios/quantidade_pessoas}")



