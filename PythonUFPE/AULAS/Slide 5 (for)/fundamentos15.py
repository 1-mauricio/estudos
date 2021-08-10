#programa qu elê "n" números e mostra o menor deles

qtd = int(input("Digite a quantidade de números: "))
menor = numero = 0

if qtd <= 0:
    print("A quantidade deve ser maior que zero.")
else:
    numero = int(input("Digite o 1° número: "))
    menor = numero
    for i in range(qtd-1):
        numero = int(input(f'Digite o {i+2}° número: '))
        if numero < menor:
            menor = numero
    
    print(f"O menor número digitado foi: {menor}")
