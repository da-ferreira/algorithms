
"""
Autor: David Ferreira de Almeida

Algoritmo de ordenacao Comb Sort
complexidade melhor caso: O(n.log(n))
complexidade pior caso: O(n^2)

O algoritmo é uma melhora do bubble sort.
Usa um salto para comparar elementos, e esse
salto diminui a cada iteracao sobre a lista, ate que chegue em 1 (equivalente ao bubble sort).
Segundo os autores, o melhor valor de diminuicao e dividir por 1.3
"""


def combsort(array):
    gap = len(array)

    while gap > 1:
        gap = int(gap / 1.3)

        for i in range(len(array) - gap):
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]


if __name__ == '__main__':
    from random import randint
    quantidade = randint(1, 10)

    lista = [randint(1, 99) for x in range(quantidade)]

    print(f'Lista gerada: {lista}')
    combsort(lista)
    print(f'Lista ordenada: {lista}')
   