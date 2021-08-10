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
def leitura(profissional):
    codigo = int(input("Digite um código (número positivo): "))
    while codigo <= 0:
        codigo = int(input("O número deve ser positivo. Digite um código: "))
    nome = input("Digite o nome da profissão: ")
    area = input("Digite a área da profissão: ")
    profissional[codigo] = (nome, area)


N = int(input("Digite um valor para N maior que zero: "))
while N <= 0:
    N = int(input("O valor de N deve ser maior que zero. Digite um valor para N: "))

prof = {}
for i in range(N):
    leitura(prof)

codigo = int(input("Digite um código para ser pesquisado: "))
while codigo > 0:
    if codigo in prof:
        print(f"Código encontrado.\nNome: {prof[codigo][0]}\nÁrea: {prof[codigo][1]}")
    else:
        print("Código inexistente.")

    codigo = int(input("Digite um código para ser pesquisado: "))