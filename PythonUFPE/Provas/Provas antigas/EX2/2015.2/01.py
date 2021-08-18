# O Mínimo Múltiplo Comum (MMC) de 2 números inteiros é o menor número inteiro que é
#múltiplo de ambos. Escreva uma função em Python que receba 2 números inteiros como
#parâmetros e devolva como resultado o MMC destes números (também inteiro).
#Obs1: A função deve supor que os dois números recebidos como parâmetros serão sempre
#informados corretamente, i.e., não é necessário validá-los na função.
#Obs2: Não utilizar nenhuma fórmula matemática para calcular o MMC.
#Esta função deve fazer parte de um programa Python que calcula e imprime o MMC de todos
#os pares de números inteiros positivos M e N informados pelo usuário. A quantidade de pares
#será informada pelo usuário antes de começar a digitar os números. O seu programa só deve
#imprimir os resultados após o usuário digitar todos os pares de números.
#Obs3: Caso o usuário digite algum número incorreto, o seu programa deve pedir para o
#usuário digitá-lo novamente.

def MMC(num1, num2):
    if num2 > num1:
        num1, num2 = num2, num1
    cont = num1
    while (cont%num1 != 0) or (cont%num2 != 0):
        cont += 1

    return cont


num1 = int(input('Digite um numero inteiro positivo: '))
while num1 <= 0:
    num1 = int(input('Numero invalido. Digite um numero inteiro positivo: '))
    
num2 = int(input('Digite um numero inteiro positivo: '))
while num2 <= 0:
    num2 = int(input('Numero invalido. Digite um numero inteiro positivo: '))

mmc = MMC(num1, num2)
print(f"O mmc entre {num1} e {num2} é: {mmc}")
