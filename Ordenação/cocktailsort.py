
"""
Autor:  David Ferreira de Almeida

Implementacao do algoritmo Cocktail Sort
Complexidade: O(n^2)

Baseado no bubble sort; bubble sort bidirecional
"""


def cocktailsort(array):
    size = len(array)

    for i in range(len(array)):
        j = 0

        while j < size - 2:
            if array[size - 1 - j] < array[size - 2 - j]:
                array[size - 1 - j], array[size - 2 - j] = array[size - 2 - j], array[size - 1 - j]
            
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            
            j += 1


if __name__ == '__main__':
    from random import randint

    lista = [randint(1, 100) for x in range(1, 10)]
    print(f'Lista original: {lista}')

    cocktailsort(lista)
    
    print(f'Lista Ordenada: {lista}')
  