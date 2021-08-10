#FATORIAL COM RECURSAO
def fatorial (num):
    if num < 2:
        res = 1
    else:
        res = num*fatorial(num-1)
    return res

num = int(input("Digite um número para descobrir o fatorial dele: "))
while num > 0:
    print(fatorial(num))
    num = int(input("Digite um número para descobrir o fatorial dele: "))
