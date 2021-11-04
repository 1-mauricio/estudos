import sys

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
    entrada = []
    try:
        for line in sys.stdin:
            entrada.append(line)

    except:
        pass

    destino, agua_inicial = entrada[0].split()
    n = int(entrada[1])

    ordem_inicial = []

    for i in range(2, n+2):
        pos, cap = entrada[i].split()
        ent = [int(pos),int(cap)]
        ordem_inicial.append(ent)

    ordem = ordem_inicial.copy()
    quickSort(ordem, 0, len(ordem)-1)
    ordem.reverse()
    
    agua = int(agua_inicial)
    qtd = 0
    while agua < int(destino):
        agua += ordem[qtd][1]
        qtd += 1

    agua_atual = int(agua_inicial)
    qtd_real = 0

    print(ordem)

    for i in range(len(ordem_inicial)):
        pos, cap = ordem_inicial[i]
        
        if agua_atual >= int(destino):
            print("E preciso no minimo {} paradas para chegar no destino.".format(qtd_real))
            exit()

        elif cap >= ordem[qtd-1][1]:
            agua_atual += cap
            qtd_real += 1

        elif i+1 < len(ordem_inicial):
            if ordem_inicial[i+1][0] > agua_atual:
                agua_atual += cap
                qtd_real += 1
            
            if ordem_inicial[i+1][0] > agua_atual:
                print("Nao e possivel chegar no destino, RIP.")
                exit()

        
    print("E preciso no minimo {} paradas para chegar no destino.".format(qtd_real))
    