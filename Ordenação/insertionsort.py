
"""
Autor: David Ferreira de Almeida

Algoritmo de ordenação Insertion Sort
Complexidade: O(n²)
Categoria: Algoritmo Guloso (greedy)
"""


def insertion_sort(array):
	"""
	:param array: lista a ser ordenada
	:return: None
	"""
    
	for i in range(1, len(array)):
		area_ordenada = i

		while area_ordenada > 0 and array[area_ordenada] < array[area_ordenada - 1]:
			array[area_ordenada - 1], array[area_ordenada] = array[area_ordenada], array[area_ordenada - 1]
    
			area_ordenada -= 1


