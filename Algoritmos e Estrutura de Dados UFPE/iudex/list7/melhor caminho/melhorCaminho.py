class Graph:

    def __init__(self, vertices):
        self.V = vertices 
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
		
    def BellmanFord(self, src, dest):

        dist = [float("Inf")] * self.V
        dist[src] = 0
        path = [src]
        
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                path.append(v)
                if v == dest:
                    return path

        return "Nao e possivel chegar ao destino."

if __name__ == "__main__":
    entrada = input().split()
    n = int(entrada[0])
    m = int(entrada[1])
    s = int(entrada[2])
    t = int(entrada[3])

    g = Graph(n+1)
    for i in range(m):
        line = input().split()
        u = int(line[0])
        v = int(line[1])
        w = int(line[2])
        g.addEdge(u, v, w)

    out = g.BellmanFord(s, t)
    if type(out) == list:
        res = ""
        for i in out:
            res += str(i) + " "
        
        print(res.strip())
    else:
        print(out)

