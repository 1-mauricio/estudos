# S = 2/500 - 5/490 + 2/480 - 5/470
def serie(n, num = 2, den = 500):
    res = num/den
    if n > 1:
        if num == 2:
            res = res +serie(n-1, -5, den-10)
        else:
            res = res + serie(n-1, 2, den-10)
    return res

n = int(input("Digite a quantidade de termos: "))
while n>0 and n<51:
    print(serie(n))
    n = int(input("Digite a quantidade de termos: "))
