#seleção direta
class Ordenador:
    def selecao_direta(self, lista):

        fim = len(lista)

        for i in range(fim - 1):
            #inicialmente o menor elemento já visto é o i-ésimo
            posicao_do_minimo = i

            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j

            #coloca o menor elemento encontrado no inicio da sub-lista
            #para isso, troca de lugar os elementos nas posições i e posicao do minimo
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
        
        return lista
        

    

lista = [10,3,8,-10,200,17,32]
o = Ordenador()
print(o.selecao_direta(lista))