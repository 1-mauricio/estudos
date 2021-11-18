class Grafo:
    def __init__(self, vertices, arestas):
        self.V = vertices
        self.A = arestas

    def adj(self, v):
        return self.A[v]

    def dfs(self, origem):
        lista = [origem]
        visitado = []
        while lista:
            vertice = lista.pop()
            if vertice in visitado:
                continue
            visitado.append(vertice)
            for v in self.A[vertice]:
                lista.append(v)
        return len(visitado)

    def bfs(self, origem):
        aux = 1
        visitado = [False] * len(self.V)
        antecessor = [-1] * len(self.V)
        fila = []

        visitado[origem-1] = True
        fila.append(origem)

        while fila:
            v = fila.pop()
            
            for i in g.adj(v):
                if visitado[i-1] == False:
                    visitado[i-1] = True
                    fila.append(i)
                    antecessor[i-1] = v
                    aux += 1
        
        return aux

if __name__ == "__main__":
    entrada = input().split()
    qtd_usuario = int(entrada[0]) 
    qtd_conexoes = int(entrada[1]) 
    vertices = []
    arestas = [[] for _ in range(qtd_usuario+1)]

    for i in range(1, qtd_usuario+1):
        vertices.append(i)

    for i in range(qtd_conexoes):
        conex1, conex2 = input().split()
        conex1 = int(conex1)
        conex2 = int(conex2)
        arestas[conex1].append(conex2)
        arestas[conex2].append(conex1)

    g = Grafo(vertices, arestas)
    outuput = ""
    for i in range(1, qtd_usuario+1):
        outuput += str(g.dfs(i)) + " "

    print(outuput.strip())