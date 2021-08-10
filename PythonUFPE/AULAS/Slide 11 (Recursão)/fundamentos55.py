# SEQUENCIA FIBONACCI NÃO RECURSIVA
def Fibonacci(Num):
    num1 = 0
    num2 = 1
    soma = 0
    if Num==1:
        soma = num1
    elif Num==2:
        soma = num2
    else:    
        for i in range(3,Num+1):
            soma = num1 + num2
            num1 = num2
            num2 = soma
    return soma

###### PROFESSOR
def fib(n):
    t1 = -1
    t2 = 1
    for i in range(1, n + 1):
        res = t1 + t2
        t1 = t2
        t2 = res
    return res
#######

Num = int(input("Digite um termo: "))
qtd = -1
seq = []
while Num>0:
    qtd += 1
    seq.append(Num)
    Num = int(input("Digite um termo: "))

seq.reverse()
while qtd>-1:
    num = seq[qtd]
    fib = Fibonacci(num)
    qtd -=1
    print(f"O {num} número equivale a {fib} na sequência de Fibonacci.")
