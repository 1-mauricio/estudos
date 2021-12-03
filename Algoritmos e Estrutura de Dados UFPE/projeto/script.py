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


if __name__ == '__main__':
    vertices = []
    nome = {}
    grafo = {}
    

    data = open('data\lesmis.txt', 'r')

    for line in data:
        if 'node' in line:
            id = next(data).split()
            label = next(data).split()
            vertices.append(int(id[1]))
            nome[int(id[1])] = label[1]
            grafo[int(id[1])] = {}

        elif 'edge' in line:
            source = next(data).split()
            target = next(data).split()
            value = next(data).split()

            grafo[int(source[1])][int(target[1])] = int(value[1])
            grafo[int(target[1])][source[1]] = int(value[1])


    print(grafo)
    g = Grafo(vertices, grafo)