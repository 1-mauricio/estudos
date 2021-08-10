lista = [0]*1000
dig2 = []
num = int(input("Digite um número inteiro positivo ou 0(número negativo para encerrar): "))
c=0

while num>=0 and c<1000:
    lista[c] = num
    if num>=10 and num<100:
        dig2.append(num)
    num = int(input("Digite um número inteiro positivo ou 0(número negativo para encerrar): "))
    c += 1

dig2.reverse()
print(dig2)





