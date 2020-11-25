"""
Algoritmo de busca linear com recursao
"""


def linear_search(array, item, index=0):
    if len(array) == 0 or index >= len(array):
        return -1  # Retorna -1 caso o elemento nao esteja na lista, ou a lista estiver vazia.

    elif array[index] == item:
        return index
    
    return linear_search(array, item, index + 1)


if __name__ == '__main__':
    lista = [15, 4, 3, 2, 8, 9, 14, 7]

    for i in lista:
        print(f'O valor {i} na lista, esta na posicao: {linear_search(lista, i, 0)}')

    # Testando com um valor fora da lista
    print(f'O valor "5" esta na posicao: {linear_search(lista, 5, 0)}')
