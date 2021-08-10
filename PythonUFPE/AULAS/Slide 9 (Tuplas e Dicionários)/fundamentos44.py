linhas = int(input("Digite o número de linhas da matriz: "))
while linhas < 1 or linhas > 4:
    linhas = int(input("Digite o número de linhas da matriz: "))

colunas = int(input("Digite o número de colunas da matriz: "))
while colunas < 1 or colunas > 8:
    colunas = int(input("Digite o número de colunas da matriz: "))

M = []
res = [0]*(linhas*colunas)
m6 = 0

for i in range (linhas):
    M.append([0]*colunas)
    for c in range(colunas):
        M[i][c] = int (input(f"Digite [{i+1}][{c+1}]: "))
        
for c in range(colunas):
    for i in range(linhas):            
        if M[i][c] % 6 == 0:
            res[m6] = M[i][c]
            m6 += 1
res=res[:m6]

for i in range (linhas):
    for c in range(colunas):
        print('%5d    ' % (M[i][c]), end ='')
    print()

for i in range(linhas):
    print(M[i])
print(f'Os números multiplos de 6 são: {res}')
