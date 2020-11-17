"""
Autor: David Ferreira de Almeida

Algoritmo de ordenação Counting Sort

Complexidade: O(n + k), onde k: maior elemento da lista.

Usado com mais frequencia para ordenacao de numeros,
mas ha versoes dele para outros elementos.
"""


def countingsort(array):
    """
    :param array: Lista a ser ordenada
    :return: A lista ordenada
    """

    maior = max(array) + 1

    auxiliar = [0] * maior  # preenchendo o vetor com 0's.

    for i in range(len(array)):  # incrementando quantos elementos pertencem a seu indice.
        auxiliar[array[i]] += 1

    k = 0
    for i in range(maior):  # ordenando a lista.
        for j in range(auxiliar[i]):
            array[k] = i
            k += 1

    return array 
    
