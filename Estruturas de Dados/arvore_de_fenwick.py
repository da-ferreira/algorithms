
# Implementação da estrutura de dados Árvore de Fenwick (ou árvore de indexação binária)
# autor: David Ferreira de Almeida
#
# Exemplo de utilização:
# Num problema em que se tem uma lista de números com tamanho N,
# e que é possivel fazer 2 operações:
# 1. Atualizar um indice k da lista para um determinado valor v.
# 2. Pegar a soma de um intervalo [i até j] dentro da lista.
#
# A operação 1 pode ser feita em O(1), mas a operação 2 será feita em O(n);
# quando o valor de N for grande, fazer operações do tipo 2 se torna muito lento,
# dependendo do intervalo. 
# Com a Árvore de Fenwick ambas operações podem ser feitas em O(log n).


def update(tree, index, value):
    """ Atualiza o valor de um determinado indice. 
    :param index: indice do elemento que se deseja atualizar.
    :param value: valor que se deseja colocar no indice.
    :param tree: arvore de fenwick, lista/vetor aonde estão os elementos.
    """

    while index < len(tree):
        tree[index] += value
        index += (index & -index)


def range_sum_query(tree, index=None):
    """ Retorna a soma entre um intervalo
    :param tree: estrutura aonde está guardado os dados
    :param index=None: indice para realizar a soma do indice até o indece 1.
    """

    if index is None:
        index = len(tree) - 1

    soma = 0

    while index > 0:
        soma += tree[index]
        index -= (index & -index)

    return soma


if __name__ == '__main__':
    lista = [0, 1, 3, 2, 4, 1, 2, 5, 3, 6, 4, 7, 1, 9, 6, 5]
    fenwick = [0] * len(lista)
    
    # A árvore de fenwick começa a partir da posição 1, o indice 0 é descartado;
    for i in range(1, len(lista)):
        update(fenwick, i, lista[i])
    
    print(range_sum_query(fenwick, 8))  # Soma do itervalo[1:8]

    # Trocar o elemento da posicao 5 para 8.
    # 1 -> 8, soma-se 7 em todas as posições, com o bit menos significativo.
    update(fenwick, 5, 8 - lista[5])
    # depois atualiza o valor na lista.
    lista[5] = 8

    print(lista)
    print(fenwick)

    # Se a soma é acumulada, é possivel achar a soma entre intervalos[a -> b].
    # A soma entre a até b é: 
    # a soma de b até 1 - a soma de a - 1 até 1.

    # Soma do intervalo[4:8]
    print(range_sum_query(fenwick, 8) - range_sum_query(fenwick, 3)) 
    
    # Usando a estrutura para saber quando elementos são menores que X.

    lista = [0, 1, 3, 2, 4, 1, 2, 5, 3, 6, 4, 7, 1, 9, 6, 5]
    fenwick = [0] * len(lista)

    for i in range(1, len(lista)):
        update(fenwick, lista[i], 1)   # incrementa 1 para o valor
    
    print(fenwick)
    print(range_sum_query(fenwick, 2))  # <- Quantos elementos são menores que 3?
                 
