def fibonacci(n):
    if n == 1 or n == 2:
        return 0
    else:
        return 2 + fibonacci(n-1) + fibonacci(n-2)


n = int(input("Digite um valor maior que zero p/ n: "))
while n <= 0:
    n = int(input("Valor inválido. Digite um valor maior que zero p/ n: "))

print(f"Para encontrar o {n}º termo da sequência de "
      f"Fibonacci serão necessárias {fibonacci(n)} "
      "chamadas recursivas.")