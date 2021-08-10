#Ler as notas de N alunos (N é informado pelo
#usuário antes), calcular e imprimir a média das
#notas e depois imprimir as notas que sejam
#maiores do que a média calculada.

N = int(input('Digite a quantidade de alunos: '))
notas_alunos = [0]*N
media = 0.0


for i in range(N):
    nota = int(input(f'Digite a {i+1} nota:'))
    media += nota
    notas_alunos[i] = nota
    
media = media/N
print(f"A média das {N} notas é: {media}")

for c in range(N):
    if notas_alunos[c]>=media:
        print(notas_alunos[c])

    




