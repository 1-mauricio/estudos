num1 = int(input("Digite o primeiro número(Deve ser positivo): "))
while num1<0:
    num1 = int(input("Invalido. Digite o primeiro número(Deve ser positivo): "))
num2 = int(input("Digite o segundo número(DEve ser positivo): "))
while num2<0:
    num2 = int(input("Invalido. Digite o segundo número(Deve ser positivo): "))

menor = num1
if num1>num2:
    menor = num2
mdc = 1
qtd = 1

while menor>qtd:
    if (num1%qtd == 0) and (num2%qtd == 0):
        mdc = qtd
    qtd += 1

print(f"o MDC entre {num1} e {num2} é: {mdc}")
