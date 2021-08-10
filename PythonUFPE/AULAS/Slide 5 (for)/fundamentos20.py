N = int(input("Digite um valor para N: "))
if N<=0:
    print('N deve ser maior que zero.')
else:
    for i in range(1, N+1):
        for j in range(0, i):
            print("#", end='')
        print()