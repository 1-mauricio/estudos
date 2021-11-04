def partition(lista, inicio, fim):
    i = (inicio-1)      
    pivo = lista[4]   
  
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
        print(lista)
  
        quickSort(lista, inicio, pi-1)
        quickSort(lista, pi+1, fim)


a = [90,40,20,30,10,2,3,6,100, 65, 12, 56, 13, 577, 1]
quickSort(a, 0, len(a)-1)
print(a)