# Ler uma lista de N números (N é informado pelo
# usuário antes), e depois criar duas outras listas
# com os números pares e ímpares separados. No
# final imprimir as 3 listas

N = int(input("Digite a quantidade de números: "))
lista = [0]*N
pares = [0]*N
impares = [0]*N
tampar = 0
tamimp = 0


for i in range(N):
    valor = int(input(f"Digite o elemento {i+1} do lista: "))
    lista[i] = valor
    if valor % 2 == 0:
        pares[tampar] = valor
        tampar += 1
    else:
        impares[tamimp] = valor
        tamimp += 1

pares = pares[:tampar]
impares = impares[:tamimp]

print(f"Lista total: {lista}")
print(f"Lista dos números pares: {pares}")
print(f"Lista dos números ímpares: {impares}")