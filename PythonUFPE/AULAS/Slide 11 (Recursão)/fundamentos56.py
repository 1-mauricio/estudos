# SEQUENCIA FIBONACCI RECURSIVA
def Fibonacci(qtd, num1 = 0, num2 = 1, soma=0):
    if qtd==1:
        soma += num1
    elif qtd==2:
        soma += num2
    else:
        soma = num1 + num2
    
    if qtd>1:
        Fibonacci(qtd-1, num2, soma)    

    return soma

###### PROFESSOR 1
def fibR(n):
    if n == 1:
        res = 0
    else:
        if n == 2:
            res = 1
        else:
            res = fibR(n-1) + fibR(n-2)
    return res
#####

##### PROFESSOR 2
def fibR2(n, t1 = 1, res = 0):
    if n > 1:
        res = fibR2 (n-1, res, t1 + res)
    return res
#####


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