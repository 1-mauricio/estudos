#busca binária

class Buscador:
    def busca_binaria(self, lista, x):
        primeiro = 0
        ultimo = len(lista)-1

        while primeiro <= ultimo:
            meio = (primeiro + ultimo) // 2
            if lista[meio] == x:
                return meio
            else:
                if x < lista[meio]:
                    ultimo = meio - 1
                else:
                    primeiro = meio + 1

        return -1

lista = [-100, 0, 20, 30, 50, 100, 3000, 5000]
o = Buscador()
print(o.busca_binaria(lista, 100))