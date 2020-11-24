
"""
Algoritmo de ordenação Gnome Sort
Complexidade media: O(n^2)

Baseado no conceito de um Gnome de Jardim separando seus vasos de flores.
Um gnomo de jardim classifica os vasos de flores pelo seguinte metodo:
Ele olha para o vaso de flores proximo a ele e para o anterior;
se estiverem na ordem certa, ele avanca um pote; caso contrario,
ele os troca e recua um pote. Se não houver pote anterior (ele esta no inicio da linha do pote),
ele avanca; se nao houver um pote proximo a ele (ele esta no final da fila do pote), ele acabou.
"""

def gnomesort(array):
    size = len(array) - 1
    index = 0
    
    while index < size:
        if array[index] > array[index + 1]:
            array[index], array[index + 1] = array[index + 1], array[index]

            if index > 0:
                index -= 2
        
        index += 1


if __name__ == '__main__':
    from random import randint

    lista = [randint(1, 99) for x in range(10)]

    print(f'Lista gerada: {lista}')
    gnomesort(lista)
    print(f'Lista ordenada: {lista}')
     