"""
Autor: David Ferreira de Almeida

Algoritmo de ordenação Bubble Sort
Complexidade: O(n^2) 
"""

def bubblesort(lista):
    for i in range(len(lista) - 1):
        tamanho = len(lista) - (i + 1)

        j = 0
        while j < tamanho:
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

            j += 1
    
    return lista


if __name__ == '__main__':
    from random import randint

    lista = [randint(1, 100) for x in range(1, 10)]
    print(f'Lista original: {lista}')

    lista = bubblesort(lista)
    
    print(f'Lista Ordenada: {lista}')
  