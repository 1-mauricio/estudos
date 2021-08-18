num1 = 2
den1 = 1
num2 = 7
den2 = 5
soma = 0.0

n = int(input("digite o valor de n: "))
while n < 1 :
    n = int(input("n deve ser positivo. digite novamente: "))

for i in range (n) :
    if i % 2 == 0 :
        soma = soma + num1 / den1
        num1 = num1 * 4
        den1 = den1 * 3
    else:
        soma = soma - num2 / den2
        num2 = num2 + 6
        den2 = den2 + 4
        
print("O valor da série com %d termos é %.4f" % (n,soma))