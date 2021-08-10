# power(base,expoente)
def power(base,expoente):
    if expoente == 1:
        return base
    
    res = base * power(base, expoente-1)
    return res

base = float(input("Digite o valor da base: "))
expo = int(input("Digite o valor do expoente(>0): "))
while expo <= 0:
    expo = int(input("Expoente inválido. Digite o valor do expoente(>0): "))

print(power(base, expo))