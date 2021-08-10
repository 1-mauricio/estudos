N = int(input("Digite o tamanho dos vetores: "))
vetor1 = [0]*N
vetor2 = [0]*N
soma = [0]*N

for e in range(N):
    vetor1[e] = int(input(f"Digite o elemento {e+1} do vetor 1: "))

for e in range(N):
    vetor2[e] = int(input(f"Digite o elemento {e+1} do vetor 2: "))

for e in range(N):
    soma[e] = vetor1[e] + vetor2[e]

print(f'{vetor1} + {vetor2} = {soma}')