num1 = int(input("Digite o primeiro número(Deve ser positivo): "))
while num1<1:
    num1 = int(input("Invalido. Digite o primeiro número novamente(Deve ser positivo): "))
num2 = int(input("Digite o segundo número(Deve ser positivo): "))
while num2<1:
    num2 = int(input("Invalido. Digite o segundo número novamente(Deve ser positivo): "))

maior = num1
if num1<num2:
    maior = num2
mmc = 0
qtd = maior

while mmc == 0:
    if (qtd%num1 == 0) and (qtd%num2 == 0):
        mmc = qtd
    else:
        qtd += 1

print(f"o MMC entre {num1} e {num2} é: {mmc}")