n_mult_7 = []
mult_5 = []
num = int(input("Digite um número inteiro negativo(0 para encerrar): "))
while num > 0:
    num = int(input("Inválido, o número deve ser positivo. Digite um número inteiro negativo(0 para encerrar): "))
cont = 0

while num < 0 and cont < 151:
    cont += 1
    if num % 5 == 0 and num <= -10 and num> -100:
        mult_5.append(num)
    if num % 7 != 0:
        n_mult_7.append(num)
    num = int(input("Digite um número inteiro negativo(0 para encerrar): "))
    

if cont>0:
    mult_5.reverse()
    maior = max(n_mult_7)
    print(f"Os números lidos que são múltiplos de 5 e têm 2 digitos significativos são: {mult_5}")
    print(f"O maior número lido não múltiplo de 7 é: {maior}")