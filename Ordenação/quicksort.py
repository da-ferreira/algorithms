"""
Autor: David Ferreira de Almeida

Algoritmo de ordenação Quick Sort
Complexidade: O(n.log(n))
Categoria: Divisão e conquista
"""


def quick_sort(lista, inicio=0, fim=''):
    if fim == '':
        fim = len(lista) - 1  # O ultimo indice da lista é o pivô de separação.

    if inicio < fim:  # Condicao de parada
        pivo = partition(lista, inicio, fim)  # Função de partição
        
        quick_sort(lista, inicio, pivo - 1)  # Acaba antes da posicao do pivo, lista da esquerda
        quick_sort(lista, pivo + 1, fim)  # lista da direita (maiores que o pivo)

 
def partition(lista, inicio, fim):
    pivo2 = lista[fim]

    menor_que_pivo = inicio  # elementos menores que o pivo 

    for j in range(inicio, fim):
        if lista[j] <= pivo2:
            lista[j], lista[menor_que_pivo] = lista[menor_que_pivo], lista[j]  # trocando os elementos menores que o pivo
            menor_que_pivo += 1  # avançando os elementos menores que o pivo

    lista[menor_que_pivo], lista[fim] = lista[fim], lista[menor_que_pivo]  # trocando o pivo de lugar para o "meio"

    return menor_que_pivo  # retornando a posicao do pivo

 
