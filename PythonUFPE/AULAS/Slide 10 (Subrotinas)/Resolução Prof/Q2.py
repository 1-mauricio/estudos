# – Ler números inteiros positivos de até 5 dígitos (consistir)
# e imprimir quantas vezes o dígito 9 ocorre em cada um.
# – A leitura pára com número negativo ou zero.
# – Escrever subrotina que deve desmembrar o valor do
# número em seus 5 dígitos, retornando o resultado em
# uma lista de tamanho 5.
# – Escrever outra subrotina que usa a anterior e que:
# • Recebe como parâmetros um número positivo até 99999
# e um algarismo inteiro (0 a 9), nesta ordem.
# • Retorne como resultado a quantidade vezes que o
# algarismo aparece no número.

def quebra_numero(num):
    algarismos = [-1] * 5
    pos = 0
    while num != 0:
        algarismos[pos] = num % 10
        num //= 10
        pos += 1

    return algarismos


def procura_numero(num, num_desejado):
    qn = quebra_numero(num)
    contador = 0
    pos = 0
    while (pos < 5) and (qn[pos] != -1):
        if qn[pos] == num_desejado:
            contador += 1
        pos += 1

    return contador


numero = int(input("Digite um número inteiro de até 5 dígitos (zero p/ encerrar): "))
while numero > 99999:
    numero = int(input("Número deve ter até 5 dígitos e deve ser positivo. Tente novamente: "))

while numero > 0:
    alg = int(input("Digite um algarismo de 0 a 9: "))
    while (alg < 0) or (alg > 9):
        alg = int(input("O número deve ser de 0 a 9. Tente novamente: "))
    qtd = procura_numero(numero, alg)
    print(f"O número {alg} aparece {qtd} vez(es) em {numero}.")

    numero = int(input("Digite um número inteiro de até 5 dígitos (zero p/ encerrar): "))
    while numero > 99999:
        numero = int(input("Número deve ter até 5 dígitos e deve ser positivo. Tente novamente: "))