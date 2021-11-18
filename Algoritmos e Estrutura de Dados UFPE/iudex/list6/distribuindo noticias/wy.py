class Grafo:
    def __init__(self, aresta, vertice):
        self.aresta = aresta
        self.vertice = vertice

    def dfs(self, origem):
        pilha = [origem]
        caminho = [] 
        while pilha:
            vertice = pilha.pop()
            if vertice in caminho:
                continue
            caminho.append(vertice)
            for i in self.aresta[vertice]:
                pilha.append(i)
        return caminho

def main():
    n, m = input().split()
    m = int(m) #numero de conexoes
    n = int(n) #numero de usuarios
    a = []
    vert = []

    for c in range(n+1):
        aresta = []
        a.append(aresta)

    for i in range(1, n+1):
        vert.append(i)

    for j in range(0, m):
        u, v = input().split()
        a[int(v)].append(int(u))
        a[int(u)].append(int(v))

    grafo = Grafo(a, vert)   
    result = ""

    for y in range(1, n+1):
        result = result + str(len(grafo.dfs(y))) + " "
    print(result.strip())
          
if __name__ == '__main__':
    main()