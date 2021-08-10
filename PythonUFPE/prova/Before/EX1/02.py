# ler uma sequencia de números inteiros negativos - parar com um número não negativo
# usuário só pode digitar 300 numeros
# imprimir nessa ordem: numeros lidos cujos valores são negativos e múltiplos de 5

lista = [0]*300
mult_5 = []
mult_11= []
num = int(input("Digite um número inteiro negativo(número positivo ou 0 para encerrar): "))
c=0

while num<0 and c<300:
    lista[c] = num
    if num % 5 == 0:
        mult_5.append(num)
    if num % 11 == 0:
        mult_11.append(num)
    num = int(input("Digite um número inteiro negativo(número positivo ou 0 para encerrar): "))
    c += 1

lista = lista[:c]

mult_5.reverse()
maior = max(mult_11)
print(f"Os números lidos que são multiplos de 5: {mult_5} \nO maior número lido múltiplo de 11: {maior}")
