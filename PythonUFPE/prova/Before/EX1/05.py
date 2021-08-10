quantidade = -1

while quantidade < 0:
    quantidade = int(input("Digite a quantidade de termos: ")) 

result = 0
valor_par = 100
valor_impar = -13

for i in range(quantidade):
    fatorial = 1
    for j in range(i+1, 1, -1):
        if i ==0: pass
        else: fatorial *= j
    if i%2 == 0:
        result += valor_par/fatorial
        valor_par -= 5
    else:
        result += valor_impar/fatorial
        valor_impar -= 11


print(result)