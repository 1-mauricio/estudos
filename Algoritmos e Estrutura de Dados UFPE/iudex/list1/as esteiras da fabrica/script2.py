class NoProduto:
    def __init__(self, produto) -> None:
        self.produto = produto
        self.proximo = None
        
class Esteira:
    def __init__(self) -> None:
        self.primeiro = None
        self.ultimo = None

    def insert(self, produto, test):
        novo_node = NoProduto(produto)
        if self.primeiro == None:
            self.primeiro = novo_node
            self.ultimo = novo_node
        else:
            self.ultimo.proximo = novo_node
            self.ultimo = novo_node

        if test == 'move':
            novo_node.proximo = None

    def remove(self):
        if self.primeiro != None:
            aux = self.primeiro
            self.primeiro = aux.proximo
            aux.proximo = None
            if self.primeiro == None:
                return 1, aux.produto
            return aux.produto
        else:
            return 0

    def show(self):
        if self.primeiro != None:
            resultado = ""
            aux = self.primeiro
            while aux != None:
                resultado += str(aux.produto) + " "
                aux = aux.proximo 
            print(resultado.strip())
        else:
            print()

if __name__ == "__main__":
    fabrica = []
    i = 0
    
    while True:
        if i == 0:
            qtd = int(input())
            for i in range(qtd, 0, -1):
                fabrica.append(Esteira())  
            i = 1
        else:
            entrada = input()
            if "INS" in entrada:
                entrada = entrada.split()
                numero = int(entrada[1])
                esteira = fabrica[numero-1]
                produto = entrada[2]
                esteira.insert(produto, 0)
                print('O produto: "{produto}" foi adicionado na esteira {numero}.'.format(produto = produto, numero = numero))

            elif "RMV" in entrada:
                entrada = entrada.split()
                numero = int(entrada[1])
                esteira = fabrica[numero-1]
                produto = esteira.remove()
                if produto == 0:
                    print("Nao ha produtos para empacotar na esteira {numero}!" .format(numero = entrada[1]))
                elif produto[0] == 1:
                    print('O produto: "{produto}" foi empacotado com sucesso!' .format(produto = produto[-1]))
                    print("A esteira {numero} ficou vazia..." .format(numero = entrada[1]))
                else:
                    print('O produto: "{produto}" foi empacotado com sucesso!' .format(produto = produto))

            elif "MOV" in entrada:
                entrada = entrada.split()
                numero_esteira_rem = int(entrada[1])
                numero_esteira_add = int(entrada[2])
                esteira_rem = fabrica[numero_esteira_rem-1]
                esteira_add = fabrica[numero_esteira_add-1]
                if esteira_rem.primeiro != None:
                    aux = esteira_rem.primeiro.produto
            
                    esteira_add.insert(aux, 'move')
                    esteira_rem.remove()
                    print('O produto: "{produto}" foi movido para a esteira {numero}.' .format(produto = aux, numero = numero_esteira_add))
                else:
                    print("Erro ao mover produto.")
                
            elif "SHW" in entrada:
                entrada = entrada.split()
                esteira = fabrica[int(entrada[1])-1]
                print("Esteira {numero}:" .format(numero=entrada[1]))
                esteira.show()

            elif entrada == "END":
                exit()

    '''i = 0
    for line in sys.stdin:
        if i == 0:
            qtd = int(line)
            while qtd >= 1:
                fabrica.append(Esteira())  
                qtd -= 1  
            i = 1
        else:
            entrada = line.split()
            if entrada[0] == "INS":
                esteira = fabrica[int(entrada[1])-1]
                produto = entrada[2]
                esteira.insert(produto, entrada[1])
            elif entrada[0] == "RMV":
                esteira = fabrica[int(entrada[1])-1]
                esteira.remove()
            elif entrada[0] == "MOV":
                pass
            elif entrada[0] == "SHW":
                esteira = fabrica[int(entrada[1])-1]
                esteira.show()
            elif entrada[0] == "END":
                exit()'''
    
    '''fabrica[0].remove()
    fabrica[0].insert("Pipoca", "1")
    fabrica[0].insert("Chocolate", "1")
    fabrica[0].insert("Comida", "1")
    fabrica[0].show()

    fabrica[0].remove()
    fabrica[1].insert("Pipoca", "2")
    fabrica[0].show()
    fabrica[1].show()'''