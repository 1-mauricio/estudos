def max_heapify(A,i):
    l = esquerda(i)
    r = direita(i)
    if l < len(A) and A[l] > A[i]:
        maior = l
    else:
        maior = i
    if r < len(A) and A[r] > A[maior]:
        maior = r
    if maior != i:
        A[i], A[maior] = A[maior], A[i]
        max_heapify(A, maior)

def esquerda(i):
    return 2 * i + 1

def direita(i):
    return 2 * i + 2

def build_max_heap(A):
    n = int((len(A)//2)-1)
    for i in range(n, -1, -1):
        max_heapify(A,i)

A = [1,2,3,4,5,6,7,8,9]
build_max_heap(A)
print(A)

#output = [9, 8, 7, 4, 5, 6, 3, 2, 1]