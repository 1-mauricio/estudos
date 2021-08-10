cod = int(input("Digite o código do curso(0 para parar): "))
tab = {}

while cod>=1 :
    nome = input("Digite o nome do Curso: ")
    cen = int(input("Digite o código centro a que o Curso pertence: "))

    tab[cod] = (nome,cen)

    cod = int(input("Digite o código do curso(0 para parar): "))

x = int(input("Digite o código do centro: "))

for key in tab.items():
   for x in key:
       print("está")






