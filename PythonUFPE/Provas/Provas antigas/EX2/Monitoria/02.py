# S = 3 + 5 / 2! + 15 / 3! + 30 / 4! + 75 / 5! + 180 / 6! + ...
def Fatorial(n):
    if n <= 1:
        fat = 1
    else:
        fat = n* Fatorial(n - 1)
    return fat

def Soma(N, num_1 = 3, num_2 = 5/6, den = 1, sin = 1):
    if N <= 1:
        if sin > 0:
            res = num_1 / Fatorial(den)
        else:
            res = num_2 / Fatorial(den)
    else:
        if sin > 0:
            res = num_1 / Fatorial(den) + Soma(N - 1, num_1, num_2 * 6, den + 1, sin * -1)
        else:
            res = num_2 / Fatorial(den) + Soma(N - 1, num_1 * 5, num_2, den + 1, sin * -1)
    return res

erro = True
while erro:
    try:
        N = input("Digite um número inteiro: ")
        N = int(N)
        erro = False
    except:
        print("Erro.")

res = Soma(N)
print(res)


def serie(n, num1 = 3, num2 = 5/6, den = 1, sin = 1):
    if n <= 1:
        if sin > 0:
            res = num1 / den
        else:
            res = num2 / den
    else:
        if sin > 0:
            res = num1 / den + serie(n-1, num1, num2 * 6, den * (den+1), sin * -1)
        else:
            res = num2 / den + serie(n-1, num1 * 5, num2, den * (den+1), sin * -1)
    return res