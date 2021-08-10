# S = 37*38/1 - 36*37/2 + 35*36/3 - 34*35/4 + ...
def serie_1(n, num = 37, den = 1, sin = 1):
    if n <= 1:
        res = sin * num * (num + 1) / den
    else:
        res = sin * num * (num + 1) / den + serie_1(n-1, num -1, den + 1, sin * -1)
    return res

n = int(input("Digite a quantidade de termos: "))
while n > 0:
    print(serie_1(n))
    n = int(input("Digite a quantidade de termos: "))