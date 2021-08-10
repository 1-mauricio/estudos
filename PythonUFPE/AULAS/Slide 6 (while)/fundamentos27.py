# Calcular a média aritmética de vários números reais
# fornecidos pelo usuário. A leitura dos números deve
# parar quando um número negativo for lido.

n = float(input("Digite um número maior ou igual a zero (número negativo para encerrar):" ))
soma = n
total = 1.0
while n >= 0:
    n = float(input("Digite um número maior ou igual a zero (número negativo para encerrar):" ))
    if n >=0:
        soma += n
        total += 1.0

if soma < 0:
    print("Nenhum número válido foi digitado.")
else:
    print(f"A média dos números digitados é: {soma/total}")