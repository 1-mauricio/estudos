# Fazer um programa para achar todos os números
# palíndromos entre 100 e 5000.
# – Um número é palíndromo se ele tiver o mesmo valor
# quando escrito da direita para a esquerda. Ex: 17371.
# – Escreva e utilize uma subrotina cujo resultado é o valor
# recebido no parâmetro (int) escrito ao contrário.
# • Pode ser interessante utilizar a subrotina da questão
# anterior para desmembramento dos números.

def quebra_numero(num):
    algarismos = [-1] * 4
    pos = 0
    while num != 0:
        algarismos[pos] = num % 10
        num //= 10
        pos += 1

    return algarismos


def palindromo(num):
    nq = quebra_numero(num)
    num_reverso = 0
    pos = 0
    while (pos < 4) and (nq[pos] != -1):
        num_reverso = num_reverso * 10 + nq[pos]
        pos += 1

    if num == num_reverso:
        return True
    else:
        return False


for i in range(100, 5001):
    if palindromo(i):
        print(i)