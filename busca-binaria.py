
"""
Autor: David Ferreira de Almeida

Algoritmo de Busca binária em vetores ordenados

Complexidade: O(log(n)) 
Categoria: Divisão e Conquista
"""


def busca_binaria(vetor, item):
    """
    :param vetor: lista que será utilizada na busca.
    :param item: item que será buscado na lista.
    :return: O indice do elemento buscado, caso ele não existir retorna None.
    """

    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:  # Caso o item nao esteja na lista
        meio = (inicio + fim) // 2

        if vetor[meio] == item:
            return meio

        elif item < vetor[meio]:
            fim = meio - 1
        
        elif item > vetor [meio]:
            inicio = meio + 1

    return None  # Caso o item não estiver na lista

