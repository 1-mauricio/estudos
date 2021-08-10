# Calcular o valor de S com N termos, onde N é informado pelo usuário e S é:
# S = 37*38/1 + 36*37/2 + 35*36/3  ...

N = int(input("informe a quantidade de termos(o número deve ser maior que zero): "))
numerador1 = 37
numerador2 = 38
denominador = 1
S = 0
while N<=0:
    N = int(input("informe a quantidade de termos(o número deve ser maior que zero): "))
while N>0:
    S += (numerador1*numerador2/denominador)
    numerador1 -= 1
    numerador2 -= 1
    denominador += 1
    N -= 1
    
print(f"A soma é igual a {S}")

