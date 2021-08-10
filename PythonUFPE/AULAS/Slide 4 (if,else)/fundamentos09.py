x = float(input("Digite o número 1:"))
y = float(input("Digite o número 2:"))
z = float(input("Digite o número 3:"))


min = x
if y < min:
    min = y
if z < min:
    min = z

print("o menor número é:", min)