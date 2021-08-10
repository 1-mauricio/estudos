# S = 2 - 7/5 + 8/3 - 13/9 + 32/9 - 19/13 + 128/27 ...

def Serie(n, num1 = 2, den1 = 1, num2 = -7, den2 = 5, termo = 1):
    if termo == 1:
        res = num1 / den1
    else:
        res = num2 / den2
    if n > 1:
        if termo == 1:
            res = res + Serie(n - 1, num1 * 4, den1 * 3, num2, den2, 2)
        else:
            res = res + Serie(n - 1, num1, den1, num2 - 6, den2 + 4, 1)
    return res


n = int(input("Digite a quantidade de termos: "))
while n < 1:
    n = int(input("Digite a quantidade de termos: "))

s = Serie(n)
print(s)