# Somar inteiros impares entre dois valores inteiros informados pelo usuário

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
soma = 0

if num1>num2:
    num1, num2 = num2, num1

if num1 % 2 == 0:
    num1 += 1 

while num1<=num2:
    soma += num1
    num1 += 2

print(f"a soma dos números ímpares é {soma}")