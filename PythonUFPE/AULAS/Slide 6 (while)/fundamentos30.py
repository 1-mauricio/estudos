# Ler um número inteiro e dizer se ele é perfeito ou não.
# Obs: um número é perfeito se ele é igual à soma de
# todos os seus divisores (exceto ele mesmo).

n = int(input("Digite um valor maior que zero:"))
while n <= 0:
    n = int(input("Digite um valor maior que zero:"))

soma = 1
for i in range(2, n):
    if n % i == 0:
        soma += i
    

if soma == n:
    print(f"O número {n} é perfeito.")
else:
    print(f"O número {n} não é perfeito.")