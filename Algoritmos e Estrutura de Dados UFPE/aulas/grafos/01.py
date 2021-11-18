class Grafo:
    def __init__(self, vertices, arestas):
        self.V = vertices
        self.A = arestas
    def adj(self, v):
        return self.A[v]
    def qtd_vertices(self):
        return len(self.V)
    def verifica_conexao(self, x, y):
        return y in self.adj(x)

    # busca em profundidade

    def busca_profundidade(self):
        visitado = len(self.V) * [False]
        antecessor = len(self.V) * [-1]
        for v in range(0, len(self.V)):
            if not visitado[v]:
                self.dfs(v,antecessor, visitado)
        
        for i in range(0, len(self.V)):
            print(antecessor[i])

        del visitado
        del antecessor

    def dfs(self, v, antecessor, visitado):
        visitado[v] = True
        for u in self.adj(v):
            if not visitado[u]:
                antecessor[u] = v
                self.dfs(u, antecessor, visitado)


    # busca em largura

    def bfs(self):
        visitado = len(self.V)*[False]
        antecessor =len(self.V)*[-1]
        vertices = []
        for i in range(0,len(self.V)):
            if not visitado[i]:
                vertices.append(i)
                visitado[i] = True
                while len(vertices) >0:
                    v = vertices.pop(0)
                    for u in self.adj(v):
                        if not visitado[u]:
                            visitado[u] = True
                            antecessor[u] = v
                            vertices.append(u)
        for i in range(0,len(self.V)): 
            print(antecessor[i])
        del visitado
        del antecessor

vertices = [ 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
arestas = {0: [2,4,7], 1: [2,5], 2: [3], 3: [6,10], 4: [8], 5:[9], 6:[9,10], 7: [8,14], 8: [], 9: [], 10: [13],11: [12,14], 12:[13,16],13:[16],14:[],15:[16],16:[17],17:[]}
g = Grafo(vertices, arestas)

g.busca_profundidade()

g.dfs()
