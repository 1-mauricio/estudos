def partition(lista, inicio, fim):
    i = (inicio-1)      
    pivo = lista[fim][1]     
  
    for j in range(inicio, fim):
        if lista[j][1] <= pivo:

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

if __name__ == '__main__':
    destino, agua = input().split()
    destino = int(destino)
    agua = int(agua) 
    n = int(input())

    lista = [0]*n

    for i in range(n):
        pos, cap = input().split()
        lista[i] = [int(pos),int(cap)]

    print(lista)
    quickSort(lista, 0, len(lista)-1)
    lista.reverse()
    
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