# Calcular o menor de uma série de números inteiros lidos. A leitura dos números  deve parar quando o número
# 0 for lido

n = int(input("Digite um número inteiro (zero irá encerrar o programa): "))
menor = n
while n != 0:
    n = int(input("Digite um número inteiro (zero irá encerrar o programa): "))
    if (n != 0) and (n < menor):
        menor = n
    
if menor == 0:
    print("Nenhum número válido foi digitado")
else:
    print(f"O menor número é: {menor}")