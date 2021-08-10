# Calcular o valor de S com N termos, onde N é
# informado pelo usuário e S é:
# • S = 2/500 - 5/490 + 2/480 - 5/470 + ...

N = int(input("Informe um valor para N: "))
if N > 0:
    print("o valor deve ser maior que 0")
elif N > 50:  # Valores maiores que 50 terão divisão por zero
    print("O valor de N deve ser menor ou igual a 50")
else:
    S = 0
    numerador = 2
    denominador = 500
    for i in range(N):
        S += numerador/denominador

        denominador -= 10
        if numerador == 2:
            numerador = -5
        else:
            numerador = 2

    print(f"Para {N} termos, o valor de S ={S}")