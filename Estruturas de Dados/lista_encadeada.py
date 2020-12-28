"""
Autor: David Ferreira de Almeida
Implementação de Lista Encadeada

head -> 2 -> 'string' -> True -> 7 -> None
"""

class Node:
    def __init__(self, element):
        self.current = element  # valor do nó
        self.next = None  # valor do próximo nó


class LinkedList:
    def __init__(self):
        self.head = None  
        self._size = 0 
    

    def append(self, element):
        """ Insere um elemento no final da lista """

        if self.head is not None:
            pointer = self.head

            while pointer.next is not None:
                pointer = pointer.next
            
            pointer.next = Node(element)
        else:
            self.head = Node(element)  # primeiro elemento inserido na lista

        self._size += 1
    

    def insert(self, index, element):
        """ Insere um elemento em qualquer posição da lista """
        node = Node(element)

        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index - 1)

            # Antes de inserir o elemento, é necessário fazer a ligação
            # com o elemento inserido e com o restante da lista
            node.next = pointer.next
            pointer.next = node

        self._size += 1
    

    def remove(self, element):
        """ Remove a primeira referencia do elemento na lista """

        if self.head is None:
            raise ValueError(f'{element} is not in list')

        elif self.head.current == element:
            self.head = self.head.next
            self._size -= 1
            
            return None  # elemento encontrado
        else:
            predecessor = self.head
            pointer = self.head.next  # começa a partir do segundo elemento

            while pointer is not None:
                if pointer.current == element:
                    # fazendo a ligação do elemento anterior do removido
                    # ao proximo elemento do removido
                    predecessor.next = pointer.next
                    pointer.next = None

                    self._size -= 1
                    return None  # elemento encontrado

                pointer = pointer.next
                predecessor = predecessor.next

        # caso o elemento não esteja na lista
        raise ValueError(f'{element} is not in list')


    def index(self, element):
        """ Retorna o índice do elemento passado """
        pointer = self.head
        i = 0

        while pointer is not None:
            if pointer.current == element:
                return i
            
            pointer = pointer.next
            i += 1

        raise ValueError(f'{element} is not in list')


    def _getnode(self, index):
        """ Retorna o i-esimo nó indicado pelo index """

        pointer = self.head

        for i in range(index):
            if pointer is not None:
                pointer = pointer.next
            else:
                raise IndexError('list index out of range')
        
        return pointer


    def __getitem__(self, index):
        """ Retorna o valor de index na lista
            ex: temp = lista[5]
        """
        pointer = self._getnode(index)
            
        if pointer is not None:
            return pointer.current
        
        raise IndexError('list index out of range')
        
        
    def __setitem__(self, index, element):
        """ Modifica o valor do indice "index" na lista
            ex: lista[4] = 15
        """

        pointer = self._getnode(index)

        if pointer is not None:
            pointer.current = element
        else:
            raise IndexError('list index out of range')
        

    def __len__(self):
        """ Retorna o tamanho da lista """
        return self._size


    # Usado quando é chamada a função print
    def __str__(self):
        representation = ''
        pointer = self.head

        while pointer is not None:
            if pointer.next is not None:
                representation += str(pointer.current) + ' -> '
            else:
                representation += str(pointer.current)

            pointer = pointer.next

        return representation


    # Usado sem a função print
    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    lista = LinkedList()

    lista.append(15)
    lista.append('casa')
    lista.append(12222)
    lista.append(1.7)
    lista.append('string')

    print(lista[3])
    lista.insert(3, 3.14159)
    print(lista[3])

    lista.remove(15)
    print(lista[0])

    print(lista)
    
