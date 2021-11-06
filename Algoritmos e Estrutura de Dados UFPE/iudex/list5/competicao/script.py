class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

class Arvore:
    def __init__(self) -> None:
        self.raiz = None

    def inserir(self, no):
        novo = NodoArvore(no)
        if self.raiz == None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                anterior = atual
                if no <= atual.chave: 
                        atual = atual.esquerda
                        if atual == None:
                            anterior.esquerda = novo
                            return
                
                else: 
                        atual = atual.direita
                        if atual == None:
                                anterior.direita = novo
                                return

    def inOrder(self, atual):
         if atual != None:
              self.inOrder(atual.esquerda)
              print(atual.chave)
              self.inOrder(atual.direita)

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

def mergeSort(lista):
    if len(lista) > 1:
        meio = len(lista)//2
  
        L = lista[:meio]
  
        R = lista[meio:]
  
        mergeSort(L)
        mergeSort(R)
  
        i = j = k = 0
  
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1

if __name__ == '__main__':
    qtd_alunos = int(input())
    pontuacao = [0]*qtd_alunos

    for i in range(qtd_alunos):
        pontuacao[i] = int(input())

    mergeSort(pontuacao)
    
    '''output = Arvore()
    for i in range(0, qtd_alunos, 2):
        output.inserir((pontuacao[i+1] - pontuacao[i]))

    output.inOrder(output.raiz)'''

    output = []
    for i in range(0, qtd_alunos, 2):
        output.append((pontuacao[i+1] - pontuacao[i]))

    mergeSort(output)
    for i in range(len(output)):
        print(output[i])
