
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
		
    def compDist(self, dist, total):
        
        for i in range(self.V):
            if dist[i] != float("Inf") and dist[i] != 0:
                if dist[i] < total[i][0]:
                    total[i][0] = dist[i]
            
        return total
	
    def BellmanFord(self, src, total):

        dist = [float("Inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        total = self.compDist(dist, total)
        return total


if __name__ == "__main__":
    entrada = input().split()
    m = int(entrada[0])
    n = int(entrada[1])
    g = Graph(m)

    for i in range(n):
        line = input().split()
        u = int(line[0])
        v = int(line[1])
        w = int(line[2])
        g.addEdge(u, v, w)

    total = [[100] for i in range(g.V)]
    for i in range(g.V):
        total = g.BellmanFord(i, total)

    res = 0
    for i in range(1, len(total)):
        res += total[i][0]

    print(res)