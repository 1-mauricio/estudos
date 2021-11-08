def partition(lista, inicio, fim, pivo):
    i = (inicio-1)
  
    for j in range(inicio, fim):
        if lista[j] < pivo:

            i = i+1
            lista[i], lista[j] = lista[j], lista[i]
  
    lista[i+1], lista[fim] = lista[fim], lista[i+1]
    return (i+1)
  
def quickSort(lista, inicio, fim):
    if len(lista) == 1:
        return lista
    if inicio < fim:
  
        pi = partition(lista, inicio, fim)
        

if __name__ == '__main__':
    k = int(input())
    for i in range(k):
        chaves = input().split()
        cadeados = input().split()
        partition(cadeados, 0, len(cadeados)-1, chaves[1])
        print(cadeados)