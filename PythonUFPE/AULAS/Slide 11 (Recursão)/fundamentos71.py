#Revisão
# 37*38/1 - 36*37/2 + 35*36/3 - 36*37/4 
def serie (n) :
    return serieR (n, 37, 1)

def serieR (n, num, den):
    if n == 1:
        if num % 2 == 1:
            res = num * (num + 1) / den
        else:
            res = - num * (num + 1) / den
    else:
        if num % 2 == 1:
            res = num * (num + 1) / den + serieR (n - 1, num - 1, den + 1)
        else:
            res = - num * (num + 1) / den + serieR (n - 1, num - 1, den + 1)
    return res

termos = int(input("Número de termos: "))
while termos < 1:
    termos = int(input("Número de termos: "))
r = serie (termos)
print(f"Resultado com {termos} termos é {r}")