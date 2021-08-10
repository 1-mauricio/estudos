numerador = s = 0

n = int(input("Informe um número entre 1 e 50: "))
if n > 50:
    print("Valor inválido")
else:
  denominador = 500
  numerador = 2
  for i in range(n):
    if numerador == 2:
      s += numerador / denominador

      denominador -=10
      numerador = -5
    elif numerador == -5:
      s += numerador / denominador
      denominador -=10
      numerador = 2

print(s)