"""
Autor: David Ferreira de Almeida

Implemetação da estrutura de dados Pilha
"""

def stack():
    """ Cria a pilha """
    return []


def push(stack, item):
    """ Adiciona o elemento "item" no topo da pilha """
    stack.append(item)


def pop(stack):
    """ Remove o elemento que esta no topo da pilha """

    if len(stack) > 0:
        return stack.pop()
    
    raise IndexError('A pilha esta vazia')


def peek(stack):
    """ Mostra elemento o elemento que esta no topo da pilha """

    if len(stack) > 0:
        return stack[-1]
    
    raise IndexError('A pilha esta vazia')


# Demostracao basica do funcionamento da pilha
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
