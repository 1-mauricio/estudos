def busca_binaria(A, elemento):
    if elemento > int(A[-1]):
        return 0
    esquerda, direita = 0, len(A) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if int(A[meio]) > elemento:
            direita = meio - 1
        elif int(A[meio]) < elemento:
            esquerda = meio + 1
        else:
            return elemento
    
    return 0

if __name__ == '__main__':
    A = input().split()
    Q = input().split()
    result = ""
    for elemento in Q:
        elemento = int(elemento)
        result += str(busca_binaria(A, elemento))
    print(result)
