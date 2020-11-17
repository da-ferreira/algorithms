
"""
Autor: David Ferreira de Almeida

Algoritmo Merge Sort

Categoria: Divisão e conquista
Complexidade: O(n.log(n))
"""


def mergesort(lista, inicio=0, fim=''):
    if fim == '':
        fim = len(lista)

    if (fim - inicio) > 1:
        meio = (inicio + fim) // 2

        # Dividindo a lista
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)

        # Unindo as divisões (merge)
        merge(lista, inicio, meio, fim)


# Fazendo as junções das duas metades da lista
def merge(lista, inicio, meio, fim):
    esquerda = lista[inicio:meio]
    direita = lista[meio:fim]

    topo_esquerda = topo_direita = 0

    for i in range(inicio, fim):
        if topo_esquerda >= len(esquerda):
            lista[i] = direita[topo_direita]
            topo_direita += 1

        elif topo_direita >= len(direita):
            lista[i] = esquerda[topo_esquerda]
            topo_esquerda += 1

        elif esquerda[topo_esquerda] < direita[topo_direita]:
            lista[i] = esquerda[topo_esquerda]
            topo_esquerda += 1
        else:
            lista[i] = direita[topo_direita]
            topo_direita += 1


