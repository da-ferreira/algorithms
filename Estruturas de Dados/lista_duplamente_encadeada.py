"""
Autor: David Ferreira de Almeida
Implementação de Lista Duplamente Encadeada

Cabeça da lista (primeiro nó)
Rabo da lista (último nó)

HEAD <-> 2 <-> 'string' <-> True <-> 7 <-> TAIL
"""

class Node:
    def __init__(self, element):
        self.data = element
        self.previous = None  # 'aponta' para o nó anterior
        self.next = None  # 'aponta' para o próximo nó
    

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    

    def append(self, element):
        """ Insere um elemento no final da lista """

        if self.head is None:  # primeiro elemento inserido na lista.
            self.head = Node(element)
            self.tail = Node(element)
            
        else:
            # cria um novo nó
            new_node = Node(element)
            
            if self._size == 1:
                # apontando o próximo elemento da cabeca para o novo elemento.
                # colocando o novo elemento como rabo da lista.
                # apontando o elemento anterior do rabo da lista para a cabeca.
                self.head.next = new_node 
                self.tail = new_node  
                self.tail.previous = self.head  
            else:
                # aponta o 'proximo' do rabo da lista para o novo nó
                # e aponta o 'anterior' do novo elemento para o atual rabo da lista
                # em seguida, coloca o novo nó como rabo da lista
                self.tail.next = new_node
                new_node.previous = self.tail
                self.tail = new_node

        self._size += 1


    def prepend(self, element):
        """ Insere um elemento no inicio da lista """
        
        if self.head is None:  # primeiro elemento inserido na lista.
            self.head = Node(element)
            self.tail = Node(element)
        else:
            # cria um novo nó
            new_node = Node(element)

            # aponta o elemento anterior da atual cabeça da lista para o novo elemento.
            # aponta o elemento próximo do novo elemento para a atual cabeça da lista.
            # coloca como cabeça da lista o novo elemento.

            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node

        self._size += 1
    
    
    def remove(self, element):
        """ Remove um elemento da lista (se ele existir) """
        
        # verifica se o rabo da lista é o elemento (remoção em O(1))
        if self.tail.data == element: 
            # colocando o elemento anterior ao rabo como rabo da lista.
            self.tail = self.tail.previous  
            self.tail.next = None

            self._size -= 1
            return None

        # verifica se a cabeça da lista é o elemento (remoção em O(1))
        elif self.head.data == element:
            # colocando o segundo elemento como a cabeça da lista.
            self.head = self.head.next
            self.head.previous = None
            self._size -= 1

            return None

        else:
            pointer = self.head.next  # começa a partir do segundo elemento

            while pointer is not None:
                if pointer.data == element:
                    # Ligando o nó anterior ao elemento com o nó posterior ao elemento
                    pointer.previous.next = pointer.next
                    pointer.next.previous = pointer.previous

                    pointer = None
                    self._size -= 1
                    return pointer  # retornando None

                pointer = pointer.next
            
        # caso o elemento não esteja na lista
        raise ValueError(f'{element} is not in list')

    
    def __len__(self):
        """ Retorna o tamanho da lista """
        return self._size
    

    # Usado quando é chamada a função print
    def __str__(self):
        representation = ''
        pointer = self.head

        while pointer is not None:
            if pointer.next is not None:
                representation += str(pointer.data) + ' <-> '
            else:
                representation += str(pointer.data)

            pointer = pointer.next

        return representation


    # Usado sem a função print
    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    lista = DoublyLinkedList()

    lista.append(15)
    lista.append('jorge')
    lista.append(True)
    lista.append(3.14159)

    lista.prepend('maradona')
    lista.prepend(False)

    print(len(lista))
    print(lista)  # False <-> 'maradona' <-> 15 <-> 'jorge' <-> True <-> 3.14159
     
  
