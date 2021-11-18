def caminho(matriz, altura, largura):
    altura, largura = altura, largura

    comeco = [0, 0]
    for i in range(altura):
        for j in range(largura):
            if matriz[i][j] == '2':
                comeco = [i, j]
                break
        else: 
            continue
        break
    else:
        return None

    fila = []
    fila.insert(0, [comeco[0], comeco[1], 0])
    direcoes = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visitado = [[False] * largura for _ in range(altura)]

    while len(fila) != 0:
        pos = fila.pop()
        visitado[pos[0]][pos[1]] = True

        if matriz[pos[0]][pos[1]] == "3":
            return pos[2]

        for dir in direcoes:
            h, w = pos[0]+dir[0], pos[1]+dir[1]
            if (h < 0 or h >= altura or w < 0 or w >= largura or matriz[h][w] == "1" or visitado[h][w]): continue
            fila.insert(0, [h, w, pos[2]+1])

if __name__ == '__main__':
    altura, largura = input().split()
    altura = int(altura)
    largura = int(largura)
    matriz = []

    for i in range(altura):
        line = input().split()
        matriz.append(line)
        
    result = caminho(matriz, altura, largura)

    if result == None:
        print('Labirinto Impossivel')
    else:
        print(result)



















'''class Grafo:
    def __init__(self, vertices, arestas):
        self.V = vertices
        self.A = arestas
        
    def adj(self, v):
        return self.A[v]

    def bfs(self, origem):
        visitado = [False] * len(self.V)
        antecessor = [-1] * len(self.V)
        fila = []


        visitado[origem] = True
        fila.append(origem)

        while fila:
            v = fila.pop()
            count = -1
            for i in self.adj(v):
                count += 1
                if visitado[count] == False and i != 'i':
                    visitado[count] = True
                    fila.append(count)
                    antecessor[count] = v
        
        return antecessor

def caminho(vetor, antecessor, origem=0):
    if vetor == origem:
        print(origem)
    elif vetor == -1:
        print('caminho impossivel')
    else:
        text = antecessor[vetor]
        r1 = caminho(text, antecessor, origem)'''



                
















''' inicio = ''
fim = ''
arestas ={}
chave = input()
comando = chave.split()
for i in range(int(comando[0])):
    key = input()
    comando = key.split()
    arestas[i] = comando

vertices = []
for i in arestas:
    vertices.append(i)'''
    



    