i = num = soma = 0
qtd = int(input("Digite a quantidade de números: "))

for i in range(qtd):
    num = int(input("Digite um número:"))
    soma = soma + num
print("A soma dos", qtd, "números digitados é", soma)