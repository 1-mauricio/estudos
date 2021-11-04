import sys

def partition(lista, inicio, fim):
    i = (inicio-1)         
    pivo = lista[fim][0]     
  
    for j in range(inicio, fim):
        if lista[j][0] <= pivo:

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
    entrada = []
    try: 
        for line in sys.stdin:
            entrada.append(line)
    except:
        pass

    inicio = entrada[0].split()
    t = int(inicio[0])
    n = int(inicio[1])
    combo = []

    for i in range(1, t+1):
        produto = [int(entrada[i]), i-1]
        combo.append(produto)

    quickSort(combo, 0, len(combo)-1)
    combo.reverse()

    result = ""
    preco = 0
    for i in range(n):
        produto = combo[i][0]
        posicao = combo[i][1]
        result += str(posicao) + " "
        preco += produto - 1
         
    result = result.strip()

    print("O combo vai custar {} reais, e os produtos escolhidos foram: {}".format(preco, result))