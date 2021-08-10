num = soma = qtd = 0
num = int(input("Digite um número (zero para parar): "))
while num != 0:
    soma = soma + num
    qtd = qtd + 1
    num = int(input("Digite outro (zero para parar): "))
print(f"A soma dos {qtd} números digitados é {soma}")

