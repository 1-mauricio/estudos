# Faça um programa Python para calcular a soma dos N primeiros termos da
# série abaixo. O valor de N deve ser lido no início e deve ser positivo. Imprimir o resultado
# da seguinte forma: “O valor da série com ... termos é ...”.
# S = 150 / 20 – 156 / 30 + 162 / 50 – 170 / 80 + 174 / 120 – 184 / 170 + ...

N = int(input("Digite a quantidade de termos(Deve ser positivo): "))
while N<1:
    N = int(input("Inválido. Digite a quantidade de termos(Deve ser positivo): "))

numi = 150
nump = 156
den = 20
incr = 10
soma = 0
cont = 1


for i in range(1, N+1):
    if i % 2 == 0 :
        soma -= nump/ den
        numi + 12
    else:
        soma += numi/den
        nump += 14
    den += incr
    incr += 10
        

