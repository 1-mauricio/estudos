# S = 3 + 5 / 2! + 15 / 3! + 30 / 4! + 75 / 5! + 180 / 6! + ...
def fatorial (num):
    if num < 2:
        den = 1
    else:
        den = num*fatorial(num-1)
    return den

def serie(n, num1 = 3, num2 = 5, den = 1, termo = 1, fat = 1):
    if termo == 1:
        res = num1/den
    else:
        res = num2/den
    if n > 1:
        if termo == 1:
            fat += 1
            res = res + serie(n-1, num1*5, num2, fatorial(fat), 2, fat)
        else:
            fat += 1
            res = res + serie(n-1, num1, num2*6, fatorial(fat), 1, fat)
    return res
    
num = int(input("Digite a quantidade de termos da série: "))
while num > 0:
    print(serie(num))
    num = int(input("Digite a quantidade de termos da série: "))

