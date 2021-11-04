def max_heapify(A,i):
    l = esquerda(i)
    r = direita(i)
    if l < len(A) and A[l][1] > A[i][1]:
        maior = l
    else:
        maior = i
    if r < len(A) and A[r][1] > A[maior][1]:
        maior = r
    if maior != i:
        A[i][1], A[maior][1] = A[maior][1], A[i][1]
        max_heapify(A, maior)

def esquerda(i):
    return 2 * i + 1

def direita(i):
    return 2 * i + 2

def build_max_heap(A):
    n = int((len(A)//2)-1)
    for i in range(n, -1, -1):
        max_heapify(A,i)

if __name__ == '__main__':
    destino, agua = input().split()
    destino = int(destino)
    agua = int(agua) 
    n = int(input())

    lista = [0]*n

    for i in range(n):
        pos, cap = input().split()
        lista[i] = [int(pos),int(cap)]

    build_max_heap(lista)
    print(lista)
    
    qtd = 0
    conseguiu = False
    i = 0

    while True:
        if agua >= destino:
            print("E preciso no minimo {} paradas para chegar no destino.".format(qtd))
            conseguiu = True
            break
        elif i < len(lista):
            if lista[i][0] <= agua:
                agua += lista[i][1]
                qtd += 1
                del(lista[i])
                i = 0
            else:
                i += 1
        else:
            break
    if not conseguiu:
        print("Nao e possivel chegar no destino, RIP.")