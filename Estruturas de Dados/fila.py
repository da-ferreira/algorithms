"""
Autor: David Ferreira de Almeida
Implemetação da estrutura de dados Fila
"""

class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0
    

    # Adiciona um novo elemento na fila
    def push(self, elemento):
        self.queue.append(elemento)
        self.size += 1
    

    # Remove o elemento do inicio da fila
    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.queue.pop(0)

        raise IndexError('A fila esta vazia')    


    # Observa o primeiro da fila
    def peek(self):
        if self.size > 0:
            return self.queue[0]

        raise IndexError('A fila esta vazia')    

    
    def __str__(self):
        return ' <- '.join(str(x) for x in self.queue)


if __name__ == '__main__':
    fila = Queue()

    for i in range(1, 11, 3):
        fila.push(i)

    print('Fila gerada:', fila)
    print('Removendo um elemento do inicio:', fila.pop())    
    
    fila.push('casa')
    print('Adiconado "casa" no fim da fila:', fila)

    print('Elemento que está no começo da fila:', fila.peek())
  
