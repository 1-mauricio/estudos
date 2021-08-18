# S_2 = 0 - 1/100 + 2 - 3/100 + 4 - 5/100 + 6 + ...
def serie(N, num = 0, den = 100, sin = 1):
    if N == 1:
        res = num/den
    else:
        res = num/den + serie(N - 1, num + 1, den -101 * sin, sin * -1) 
    return res

n = int(input("Digite a quantidade de termos: "))
while n > 0:
    resultado = serie(n)
    print(f"O resultado para {n} termos é : {resultado}")
    n = int(input("Digite a quantidade de termos: "))