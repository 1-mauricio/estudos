menor = a
if b < menor :
    menor = b
if c < menor:
    menor = c

n = int(input("Digite um balor inteiro positivo para n: "))
while n == 0:
    n = int(input("Primeiro valor não pode ser zero. Tente novamente: "))
while n != 0:
    if n < menor