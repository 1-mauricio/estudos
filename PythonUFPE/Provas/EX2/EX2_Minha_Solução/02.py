def serieR(n, num1 = 105, num2 = 130, den = 25, sinal = 1):
    if n<=1:
        if sinal>0:
            res = sinal * (num1 / den)
        else:
            res = sinal * (num2 / den)
    else:
        if sinal>0:
            res = num1/den + serieR(n-1, num1 + 35, num2, den + 10, sinal * -1)
        else:
            res = num2/den - serieR(n-1, num1, num2 + 30, den + 10, sinal * -1)

    return res


n = int(input("Digite a quantidade de itens: "))
while n>0:
    print(serieR(n))
    n = int(input("Digite a quantidade de itens: "))
