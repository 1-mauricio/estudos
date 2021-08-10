def MutiplicaDigitos(Num):
    if Num<1:
        return -1
    if Num>999999:
        return -2

    multiplicacao = 1
    
    while Num != 0:
        ultDig = Num % 10
        if ultDig>0:
            multiplicacao *= ultDig
        Num //= 10
    
    return multiplicacao

Num = int(input("Digite um número inteiro positivo de 6 digitos: "))
print(MutiplicaDigitos(Num))