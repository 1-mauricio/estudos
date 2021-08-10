# S = 37*38/1 - 36*37/2 + 35*36/3 - 34*35/4 + ...
def serie2(n, num1 = 37, num2 = 38, den = 1):
    res = num1*num2/den
    if n > 1:
        if den%2 == 1:
            res = res + serie2(n-1, num1-1, num2-1, den+1)
        else:
            res = res - serie2(n-1, num1-1, num2-1, den+1)
    return res

def series1(n, num1 = 37, den = 1, sinal = 1):
    res = sinal * num1 * (num1 + 1) / den
    if n > 1 :
        res = sinal * res + series1(n - 1, num1 - 1, den + 1, - sinal)
    return res

n = int(input("Digite a quantidade de itens: "))
while n>0:
    print(serie2(n))
    print(series1(n))
    n = int(input("Digite a quantidade de itens: "))


