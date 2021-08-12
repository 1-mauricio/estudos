fim = False
while not fim:
    try:
        valor = int(input("Digite um valor positivo e inteiro: "))
        while valor <= 0:
            valor = int(input("Valor inválido. Digite um valor positivo e inteiro: "))
    except ValueError:
        print("Erro. O valor digitado deve ser um número inteiro.")
    else:
        fim = True