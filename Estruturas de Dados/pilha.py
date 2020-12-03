"""
Autor: David Ferreira de Almeida
Implemetação da estrutura de dados Pilha
"""

class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0


    # Adiciona um elemento no topo da pilha
    def push(self, elemento):
        self.stack.append(elemento)
        self.size += 1


    # Remove o elemento do topo da pilha
    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.stack.pop()
            
        raise IndexError('A pilha esta vazia')


    # Observa que esta no topo da pilha
    def peek(self):
        if self.size > 0:
            return self.stack[-1]

        raise IndexError('A pilha esta vazia')


    def __str__(self):
        return ' -> '.join(str(x) for x in self.stack)


if __name__ == "__main__":
    pilha = Stack()

    pilha.push(15)
    pilha.push(100)
    pilha.push('Casa')
    pilha.push(7.5)

    print(pilha)

    print(pilha.pop())
    print(pilha.pop())

    print(pilha.peek())

    print(pilha)
  
