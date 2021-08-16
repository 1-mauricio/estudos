def MutiplicaDigitos(Num):
    if Num < 1:
        return -1
    elif Num > 999999:
        return -2
    else:
        mult = 1
        while Num > 0:
            if Num % 10 != 0:
                mult = mult * (Num % 10)
            Num = Num // 10
        return mult
        

erro = True
while erro:
    try:
        Num = int(input("Digite um número: "))
        erro = False
    except ValueError:
        print("Erro.")
