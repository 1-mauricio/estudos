# USANDO LISTA
n = int(input("Digite o tamanho da tabela de profissões: "))

while n<1 :
    n = int(input('Tamanho de ser inteiro e positivo. Tente novamente: '))

tab = [None]*n

for i in range(n):
    codP = int(input('Digite o código de uma profissão: '))
    while codP < 1 :
        codP = int(input("Código deve ser inteiro e positivo. Tente novamente: "))
    nomeP = input(f'Digite o nome da profissão {codP}: ')
    areaP = input(f'Digite a área da profissão {codP}: ')
    tab[i] = (codP, nomeP, areaP)

codP = int(input("Digite um código de profissão para buscar(<=0 para parar): "))

while codP > 0:
    i = 0
    while (i<n) and (codP != tab[i] [0]):
        i += 1
    if i < n:
        nomeP,areaP = tab[i] [1:]
        print(f"Profissão {codP} é {nomeP} e sua área é {areaP}")
    else:
        print(f"Profissão {codP} não existe na tabela")
    codP = int(input("Digite outro código para buscar(<=0 para parar): "))

print('Fim do Programa')