"""
Implemetação da estrutura de dados DEQUE

DEQUE: Double Ended Queue (fila duplamente terminada)
"""

class Deque:
    def __init__(self):
        self.deque = []
        self._size = 0


    def add_first(self, element):
        """ Adiciona um elemento no inicio da fila """
        self.deque.insert(0, element)
        self._size += 1
    

    def add_end(self, element):
        """ Adiciona um elemento no final da fila """
        self.deque.append(element)
        self._size += 1


    def pop_first(self):
        """ Remove um elemento no inicio da fila """

        if self._size > 0:
            self._size -= 1
            return self.deque.pop(0)
        
        raise IndexError('empty list')  # a lista esta vazia

    
    def pop_end(self):
        """ Remove um elemento no inicio da fila """

        if self._size > 0:
            self._size -= 1
            return self.deque.pop()
        
        raise IndexError('empty list')  # a lista esta vazia


    def peek_first(self):
        """ Retorna o elemento que esta no inicio da fila """
        
        if self._size > 0:
            return self.deque[0]
        
        raise IndexError('empty list')

    
    def peek_end(self):
        """ Retorna o elemento que esta no final da fila """

        if self._size > 0:
            return self.deque[self._size - 1]
        
        raise IndexError('empty list')


    # Retorna o tamanho da lista quando chamado o len()
    def __len__(self):
        return self._size 


if __name__ == '__main__':
    deque = Deque()

    deque.add_first(15)
    deque.add_first('deque')

    deque.add_end(3.14159)
    deque.add_end(2.71828)

    print(deque.peek_end())  # -> 2.71828
    print(deque.peek_first())  # -> 'deque'
    
    deque.pop_first()

    print(len(deque))  # -> 3
    