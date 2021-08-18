# S_3 = - 1/5 + 2/10 - 6/20 + 24/35 - 120/55 + ...
def serie_3(N, num = -1, den = 5, num_incr = -2, den_incr = 5):
    if N == 1:
        res = num/den
    else:
        res = num/den + serie_3(N - 1, num * num_incr, den + den_incr, num_incr - 1, den_incr + 5)
    return res

n = int(input("Digite a quantidade de termos: "))
while n > 0:
    resultado = serie_3(n)
    print(f"O resultado para {n} termos é : {resultado}")
    n = int(input("Digite a quantidade de termos: "))