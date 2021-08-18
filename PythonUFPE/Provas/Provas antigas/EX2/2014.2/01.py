#A média ponderada de N números é a soma dos produtos de cada um deles multiplicados por
#seus respectivos pesos; o resultado da multiplicação é então dividido pela soma dos pesos. A
#média ponderada é utilizada em diversas disciplinas para calcular os resultados dos alunos
#considerando duas avaliações parciais com pesos variáveis. As regras para definição do resultado
#são as seguintes:
# Se a média do aluno for maior ou igual a sete, o aluno “está
#aprovado”.
# Se a média do aluno for menor que três, o aluno “está reprovado”.
# Se a média do aluno for menor que sete e maior ou igual a três, ele
#fará prova final”.
#Faça uma subrotina Python do tipo procedimento que leia as notas das duas avaliações parciais
#de um único aluno, calcule sua média, e imprima seu resultado na seguinte frase: "O aluno
#obteve média ____ e ___________." Os pesos a serem utilizados no procedimento são
#opcionalmente passados como parâmetros e, se não forem informados, seus valores devem ser 1.
#O seu programa inicialmente deve ler o nome da disciplina, os pesos a serem usados nos
#cálculos das médias e depois o número de alunos N. Em seguida, deve usar o procedimento
#acima para processar as notas dos N alunos.

def Media(N, peso1 = 1, peso2 = 1):
    if N 
    return



N = int(input("Quantidade de alunos: "))
peso1 = int(input('Digite o primeiro peso(0 para invalidar): '))
peso2 = int(input("Digite o segundo peso(0 para invalidar): "))
if (peso1 == 0 and) (peso2 == 0):
    media = Media(N)
    print(media)
else:
    media = Media(N, peso1, peso2)
    print(media)
    
    

