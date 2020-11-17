"""
Autor: David Ferreira de Almeida

Implemetação da estrutura de dados Pilha
"""

def stack():
    """
    Cria a pilha
    """
    return []


def push(stack, item):
    """
    Adiciona "item" no topo da pilha

    :param stack: Pilha que vai receber o novo elemento
    :param item: Elemento a ser adicionado ao topo
    :return: None
    """
    stack.append(item)


def pop(stack):
    """
    Remove o elemento do topo da pilha
    
    :param stack: Pilha que vai ter seu topo removido 
    :return: O elemento removido
    """

    if len(stack) > 0:
        return stack.pop()
    
    raise IndexError('A pilha esta vazia')


def peek(stack):
    """
    Mostra elemento do topo da pilha

    :param stack: Pilha
    :return: O elemento do topo da pilha
    """

    if len(stack) > 0:
        return stack[-1]
    
    raise IndexError('A pilha esta vazia')


if __name__ == '__main__':
    pilha = stack()

    for i in range(1, 11, 3):
        push(pilha, i)

    print(pilha)
    print(pop(pilha))    
    
    push(pilha, 'casa')
    print(pilha)

    print(peek(pilha))
    print(pop(pilha))
    print(pop(pilha))

