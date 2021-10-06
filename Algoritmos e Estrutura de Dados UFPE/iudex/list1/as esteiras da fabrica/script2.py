import sys

class NoProduto:
    def __init__(self, produto) -> None:
        self.produto = produto
        self.proximo = None
        
class Esteira:
    def __init__(self) -> None:
        self.primeiro = None
        self.ultimo = None

    def insert(self, produto):
        novo_node = NoProduto(produto)
        if self.primeiro == None:
            self.primeiro = novo_node
            self.ultimo = novo_node
        else:
            self.ultimo.proximo = novo_node
            self.ultimo = novo_node

        return novo_node.produto

    def remove(self):
        if self.primeiro != None:
            aux = self.primeiro
            self.primeiro = aux.proximo
            return aux.produto
        else:
            print("Nao ha produtos para empacotar na esteira I!")

    def show(self):
        if self.primeiro != None:
            resultado = ""
            aux = self.primeiro
            while aux != None:
                resultado += str(aux.produto) + " "
                aux = aux.proximo 
            print(resultado)
        else:
            print("fila vazia")

if __name__ == "__main__":
    fabrica = []
    i = 0
    
    while True:
        if i == 0:
            qtd = int(input())
            while int(qtd) >= 1:
                fabrica.append(Esteira())  
                qtd -= 1  
            i = 1
        else:
            entrada = input()
            if "INS" in entrada:
                entrada = entrada.split()
                numero = int(entrada[1])
                esteira = fabrica[numero-1]
                produto = entrada[2]
                esteira.insert(produto)
                print('O produto: "{produto}" foi adicionado na esteira {numero}'.format(produto = produto, numero = numero))
            elif "RMV" in entrada:
                entrada = entrada.split()
                numero = int(entrada[1])
                esteira = fabrica[numero-1]
                produto = esteira.remove()
                print("O produto: ", produto," foi empacotado com sucesso!")
            elif "MOV" in entrada:
                entrada = entrada.split()
                numero1 = int(entrada[1])
                numero2 = int(entrada[2])
                esteira1 = fabrica[numero1-1]
                esteira2 = fabrica[numero2-1]
                esteira2.insert(esteira1.primeiro)
                produto = esteira1.remove()
                print('O produto: "{produto}" foi movido para a esteira {numero2}' .format(produto = produto, numero2 = numero2))
                
            elif "SHW" in entrada:
                entrada = entrada.split()
                esteira = fabrica[int(entrada[1])-1]
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