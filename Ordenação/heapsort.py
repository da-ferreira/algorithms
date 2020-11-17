
"""
Autor: David Ferreira de Almeida

Algoritmo Heap Sort (min_heap, arvore binaria)

O algoritmo tem uma complexidade de n.log2(n)
para uma lista com n elementos, equivalente a
complexidade do algoritmo Quick Sort.

A base do algoritmo eh fazer n (log(n)) insercoes heap e depois n (log(n)) extracoes.

Categoria: Programacao Dinamica
"""


def filho_esquerdo_heap(posicao):
    """
    :param posicao: Posicao do pai.
    :return: Retorna a posicao do filho esquerdo. 
    """

    return 2 * posicao + 1


def filho_direito_heap(posicao):    
    """
    :param posicao: Posicao do pai.
    :return: Retorna a posicao do filho direito. 
    """

    return 2 * posicao + 2


def pai_heap(posicao):
    """
    :param posicao: Posicao de um dos filhos (esquerdo ou direito).
    :return: Retorna a posicao do pai. 
    """

    return (posicao - 1) // 2


def heap_up(arvore, posicao):
    """
    Um elemento inserido no heap eh colocado na última posicao,
    enquanto o pai for maior do que o filho (min-heap) ambos trocam de posicao.

    :param arvore: A lista da arvore binaria.
    :param posicao: Posicao do elemento inserido. 
    :return: Retorna a posicao do pai. 
    """

    pai = pai_heap(posicao)

    while (posicao != 0) and (arvore[pai] > arvore[posicao]):    
        arvore[pai], arvore[posicao] = arvore[posicao], arvore[pai]

        posicao = pai
        pai = pai_heap(posicao)

    

def inserir_heap(arvore, item):
    """
    Insere um elemento no heap e organiza ele na arvore.

    :param arvore: A lista da arvore binaria.
    :param item: Item a ser inserido.
    :return: None
    """
    
    arvore.append(item)
    heap_up(arvore, len(arvore) - 1)


def heap_down(arvore):
    """
    Removendo o menor elemento do min-heap (elemento 0), ocorre um processo
    de heap down. Enquanto o pai nao for o menor do que os dois filhos, ele troca
    de posicao com o menor filho.
   
    :param arvore: A lista da arvore binaria.
    :return: None 
    """
    
    filho = filho_esquerdo_heap(0)
    pai = 0

    while filho < len(arvore) and arvore[pai] > arvore[filho] or \
        filho + 1 < len(arvore) and arvore[pai] > arvore[filho + 1]:

        if filho + 1 < len(arvore) and arvore[filho] > arvore[filho + 1]:
            arvore[pai], arvore[filho + 1] = arvore[filho + 1], arvore[pai]

            pai = filho + 1
        else:
            arvore[pai], arvore[filho] = arvore[filho], arvore[pai]

            pai = filho
        
        filho = filho_esquerdo_heap(pai)


def retirar_heap(arvore):
    """
    Retira o menor elemento do heap e traz o ultimo elemento
    para a posicao do primeiro e organiza a arvore.

    :param arvore: A lista da arvore binaria.
    :return: O elemento retirado
    """
    
    apagado = arvore[0]

    if len(arvore) > 1:
        arvore[0] = arvore.pop()
        heap_down(arvore)

    return apagado


def transforma_em_min_heap(lista):
    """
    Transforma uma lista em arvore binaria heap (insercoes)

    :param lista: A lista a ser transformada.
    :return: A lista transformada em arvore binaria.
    """

    heap = []

    tamanho_lista = len(lista)
    i = 0

    while i < tamanho_lista:
        inserir_heap(heap, lista.pop(0))
        i += 1

    return heap


def heap_sort(lista):
    """
    Ordena uma lista com o metodo heap sort (extracoes)

    :param lista: A lista a ser ordenada.
    :return: A lista ordenada
    """

    lista = transforma_em_min_heap(lista)
    ordenada = []

    tamanho_lista = len(lista)
    i = 0
    
    while i < tamanho_lista:
        temp = retirar_heap(lista)
        ordenada.append(temp)
        
        i += 1

    return ordenada


if __name__ == '__main__':
    lista = [55, 99, 33, 22, 77, 66, 11, 88, 44]

    print(f'Ordenando a lista: {lista}')
    lista = heap_sort(lista)

    print(f'Lista ordenada: {lista}')
