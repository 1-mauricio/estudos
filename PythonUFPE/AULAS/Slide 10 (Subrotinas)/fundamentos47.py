def quebra_numero(num):
    # %10 retorna o último algarismo
    # N // 10 tira o ulimo algarismo 
    algs = [-1] * 5
    i = 0
    while num != 0:
            algs[i] = num % 10
            num //= 10
            i += 1

    return algs


def conta_numeros(num, numero_desejado):
    algs = quebra_numero(num)
    cont = 0
    i = 0
    while (i < 5) and (algs[i] != -1):
        if algs[i] == numero_desejado:
            cont += 1
        i += 1

    return cont


numero = int(input("Digite um número positivo de até 5 digitos: "))
while numero > 99999:
    numero = int(input("Inválido. Digite um número positivo de até 5 digitos: "))

alg = quebra_numero(numero)

while numero > 0:
    numero_unico = int(input("Digite um número entre 0 e 9: "))
    while (numero_unico < 0) or (numero_unico > 9):
        numero_unico = int(input("Inválido. Digite um número entre 0 e 9: "))
    quantidade = conta_numeros(numero, numero_unico)

    print(f"O número {numero_unico} aparece {quantidade} vez(es) em {numero}")