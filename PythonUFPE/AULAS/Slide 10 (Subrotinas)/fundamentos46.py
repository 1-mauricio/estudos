def leitura():
    codigo = int(input("Digite o código da profissão (positivo): "))
    while codigo <= 0:
        codigo = int(input("Código inválido. Digite o código da profissão (positivo): "))
    nome = input("Digite o nome da profissão: ")
    area = input("Digite a área da profissão: ")

    return codigo, nome, area

N = int(input("Digite a quantidade de profissões (maior que zero): "))
while N <= 0:
    N = int(input("Número inválido. Digite a quantidade de profissões (maior que zero): "))

prof = [(0,"", "")] * N
for i in range(N):
    prof[i] = leitura()

codigo = int(input("Digite um código (positivo) para ser pesquisado: "))
while codigo > 0:
    pos = 0
    while (pos < N) and (prof[pos][0] != codigo):
        pos += 1

    if pos == N:
        print("Profissão inexistente.")
    else:
        nome_profissao = prof[pos][1]
        area_profissao = prof[pos][2]
        print(f"Nome: {nome_profissao}\nÁrea: {area_profissao}")
    
    codigo = int(input("Digite um código (positivo) para ser pesquisado: "))
