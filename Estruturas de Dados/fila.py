"""
Autor: David Ferreira de Almeida

Implemetação da estrutura de dados Fila
"""


def queue():
    """ Cria a fila """
    return []


def push(queue, item):
    """ Adiciona o elemento "item" no topo da fila """
    queue.append(item)


def pop(queue):
    """ Remove o elemento que esta no inicio da fila """

    if len(queue) > 0:
        return queue.pop(0)
    
    raise IndexError('A fila esta vazia')


def peek(queue):
    """ Mostra elemento o elemento que esta no inicio da fila """

    if len(queue) > 0:
        return queue[0]
    
    raise IndexError('A fila esta vazia')


if __name__ == '__main__':
    fila = queue()

    for i in range(1, 11, 3):
        push(fila, i)

    print('Fila gerada:', fila)
    print('Removendo um elemento do inicio:', pop(fila))    
    
    push(fila, 'casa')
    print('Adiconado "casa" no fim da fila:', fila)

    print('Elemento que está no começo da fila:', peek(fila))
    print(pop(fila))
    print(pop(fila))

    print('Removido dois elementos do inicio da fila:', fila)
