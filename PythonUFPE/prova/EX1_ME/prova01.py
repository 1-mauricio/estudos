N = int(input("Digite a quantidade de termos(Deve ser positivo): "))
while N<1:
    N = int(input("Inválido. Digite a quantidade de termos(Deve ser positivo): "))

numi = 2
nump = 7
deni = 1
denp = 5
soma = 0


for i in range(1, N+1):
    if i % 2 == 0:
        soma -= nump/ denp
        nump += 6
        denp += 4 
    else:
        soma += numi/deni
        numi *= 4
        deni *= 3
    

print(f'O valor da série com {N} termos é: {soma:.4f}')