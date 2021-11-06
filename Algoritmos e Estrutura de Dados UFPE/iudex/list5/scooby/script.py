def partition(lista, inicio, fim):
    i = (inicio-1)         
    pivo = lista[fim]     
  
    for j in range(inicio, fim):
        if lista[j] <= pivo:

            i = i+1
            lista[i], lista[j] = lista[j], lista[i]
  
    lista[i+1], lista[fim] = lista[fim], lista[i+1]
    return (i+1)
  
def quickSort(lista, inicio, fim):
    if len(lista) == 1:
        return lista
    if inicio < fim:
  
        pi = partition(lista, inicio, fim)
  
        quickSort(lista, inicio, pi-1)
        quickSort(lista, pi+1, fim)

lista1 = "bjX mbj fIS".split()
lista2 = "mbj bjX fIS".split()

(lista1, lista2, len(lista1), len(lista2))


