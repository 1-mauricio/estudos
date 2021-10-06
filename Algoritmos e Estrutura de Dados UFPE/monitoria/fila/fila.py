class Node:
    def __init__(self, value=0, next=None) -> None:
        self.value = value
        self.next = None

class Queue:
    def __init__(self, listNext=None) -> None:
        self.first = None
        self.last = None

    def enqueue(self, node):
        newNode = node

        if self.first == None:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode

    def dequeue(self):
        if self.first == None:
            print("tá vazia doidão")
        else:
            aux = self.first
            self.first = aux.next
            print("elemento removido: ", aux.value)

    def amostracao(self):
        temp = self.first
        while temp != None:
            print(temp.value)
            temp = temp.next

q = Queue()
q2 = Queue()
q.enqueue(Node(1))
q.enqueue(Node(2))
q.enqueue(Node(3))
q.enqueue(Node(4))
q.enqueue(Node(5))
q2.enqueue(Node(6))

print("q1: ")
q.amostracao()
print("q2: ")
q2.amostracao()
q.enqueue(q2.first)
q2.dequeue()
