import random
import fundamentos15 as ordenador
import time

class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]
        return lista

    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista

    def compara (self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]

        o = ordenador.Ordenador()
        
        print("Comparando com listas aleatórias")
        antes = time.time()
        o.bubblesort(lista1)
        depois = time.time()
        print(f"Bubble sort demorou {depois - antes}")

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print(f"Seleção Direta demorou {depois - antes}")

        print("\nComparando com listas quase ordenadas")
        antes = time.time()
        o.bubble_curta(lista1)
        depois = time.time()
        print(f"Bubble curta demorou {depois - antes}")

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print(f"Seleção Direta demorou {depois - antes}")

c = ContaTempos()
c.compara(1000)
