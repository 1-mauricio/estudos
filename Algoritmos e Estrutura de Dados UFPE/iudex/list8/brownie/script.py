if __name__ == '__main__':
    precos = input().split()
    gramas = int(input())
    maximo = 0

    for i in range(len(precos)):
        pedaco = (i+1)*100
        valor = precos[i].replace(",", '.')
        total = (gramas/pedaco) * float(valor)
        if total > maximo:
            maximo = total

    maximo = "R$ {:,.2f}".format(maximo)
    maximo = maximo.replace(',', '.')
    maximo = maximo[:len(maximo)-3] + ',' + maximo[-2:]
    
    print("{}" .format(maximo), end="")