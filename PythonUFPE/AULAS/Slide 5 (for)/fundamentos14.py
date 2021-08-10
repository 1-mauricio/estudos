# Pprograma que calcula o fatorial de um número

numero = int(input("Digite um valor inteiro: "))
fatorial = 1

for i in range(2, numero + 1):
    fatorial = fatorial * i

print("O fatorial de", numero, "é", fatorial)