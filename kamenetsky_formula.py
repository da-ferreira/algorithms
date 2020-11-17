"""
Autor: David Ferreira de Almeida

Formula de Kamenetsky 

Complexidade: O(1)

A formula de kamenetsky permite saber quantos
digitos tem o fatorial de um numero qualquer > 0
sem precisar calcular seu fatorial.
"""


def kamenetsky(number):
    """
    :param number: O numero do fatorial
    :return: Quantidade de digitos do fatorial de number.
    """
    
    import math

    if number < 0:  # nao existe
        return 0
    
    elif number <= 1:
        return 1
    
    digits = (number * math.log10(number / math.e)) + (math.log10(2 * math.pi * number) / 2)
   
    return math.floor(digits) + 1
