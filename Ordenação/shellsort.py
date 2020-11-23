
"""
Algoritmo de Ordenação Shell Sort
Complexidade media: O(n.log(n))
"""

def shellsort(array):
    interval = len(array) // 2

    while interval > 0:
        for i in range(interval, len(array)):
            temp = array[i]
            j = i

            # fazendo as trocas
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


if __name__ == '__main__':
    from random import randint

    lista = [randint(1, 99) for x in range(10)]

    print(f'Lista gerada: {lista}')
    shellsort(lista)
    print(f'Lista ordenada: {lista}')

    