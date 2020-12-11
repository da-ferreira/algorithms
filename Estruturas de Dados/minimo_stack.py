"""
Implementação de Mínimo Stack
autor: David Ferreira de Almeida

O objeto do algoritmo é modificar a estrutura de dados
stack (pilha) de modo que o menor elemento possa ser acessado
em O(1). O elementos são adicionados em pares: o elemento
e o menor elemento da pilha.
"""

class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0


    def min(self):
        if self.size == 0:
            return None  # caso a lista esteja vazia

        return self.stack[-1][1]

    
    def push(self, element):
        temp = self.min()

        if temp is None:
            temp = element
        
        # Adiciona o elemento e o menor entre o novo elemento
        # e o menor elemento da pilha
        self.stack.append([element, min(element, temp)])
        self.size += 1

    
    def pop(self):
        if self.size == 0:
            return None  # caso a lista esteja vazia

        removido = self.stack[-1][0]
        self.stack.pop()
        self.size -= 1

        return removido
    

    def peek(self):
        if self.size == 0:
            raise IndexError('list index out of range')
        
        return self.stack[-1][0]

    
if __name__ == '__main__':
    lista = Stack()

    lista.push(0)
    lista.push(1)
    lista.push(15)
    lista.push(3)
    lista.push(-2)

    print(lista.min())  # -> -2
    lista.pop()  # removendo o -2
    print(lista.min())  # -> 0
    