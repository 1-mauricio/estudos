# Fazer um programa para:
# – Ler uma tabela com N profissões, onde
# • O valor de N é informado antes pelo usuário.
# • Cada profissão é formada por um código (número positivo),
# um nome (String) e uma área (String).
# • Leitura da tabela deve ser feita em subrotina.
# – Depois o usuário fornecerá uma lista de códigos para
# que o programa informe o nome de cada profissão.
# – Se o código da profissão não existir na tabela, mostrar
# a mensagem “Profissão Inexistente” e continuar.
# – O programa pára com a digitação de um código
# inválido (negativo ou zero).

def leitura():
    codigo = int(input("Digite o código (número positivo): "))
    while codigo <= 0:
        codigo = int(input("Número deve ser positivo. Digite o código: "))
    nome = input("Digite o nome da profissão: ")
    area = input("Digite a área da profissão: ")

    return codigo, nome, area


N = int(input("Digite um valor para N maior que zero: "))
while N <= 0:
    N = int(input("Código inválido. Digite um valor para N maior que zero: "))

prof = [(0, "", "")] * N
for i in range(N):
    prof[i] = leitura()

codigo = int(input("Digite o código positivo para ser pesquisado (negativo ou zero p/ encerrar): "))
while codigo > 0:
    pos = 0
    while (pos < N) and (prof[pos][0] != codigo):
        pos += 1

    if pos == N:
        print("Profissão inexistente. ")
    else:
        print(f"Profissão encontrada.\nNome: {prof[pos][1]}\nÁrea: {prof[pos][2]}")

    codigo = int(input("Digite o código positivo para ser pesquisado (negativo ou zero p/ encerrar): "))