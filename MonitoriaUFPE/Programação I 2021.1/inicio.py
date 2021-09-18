dias_usuario = int(input("Digite a quantidade de dias: "))

anos = 0
meses = 0
dias = dias_usuario

while dias >= 365:
    anos += 1
    dias -= 365

while dias >= 30:
    meses += 1
    dias -= 30


print(f"{dias_usuario} dias equivalem a {anos} ano(s), {meses} mes(es) e {dias} dia(s)")