
"""
Implementacao da distancia euclidiana de dois pontos em um plano.
"""


def euclidian_distance(x1, y1, x2, y2):
    from math import sqrt

    distancia = (abs(x2 - x1) ** 2) + (abs(y2 - y1) ** 2)
    distancia = sqrt(distancia)

    return distancia
   
