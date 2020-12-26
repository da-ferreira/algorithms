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
            # cria um novo nó e aponta seu 'anterior' para o atual rabo da lista.
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
        pass
