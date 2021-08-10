numerador = 0
denominador = 500
divisao = 0
soma = 0

qtd = int(input('Informe um número entre 1 e 50: '))


if qtd <= 0 or qtd >= 50:
    print("O número precisa estar entre 1 e 50")

else:
    for numerador in range(qtd):
        if qtd%2 == 0:
            numerador = -5
        else:
            numerador = 2

    for denominador in range(500, qtd):
        denominador -= 10
    
        

