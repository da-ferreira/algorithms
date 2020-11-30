"""
Autor: David Ferreira de Almeida

Implementacao da formula da area de Gauss

A formula eh utilizada quando deseja-se saber a area
de um poligono qualquer (regular ou irregular) pelas
coordenadas de seus vertices.
"""

def gauss(vertices):
    """
    :param vertices: Uma matriz com 2 colunas e x linhas, onde cada linha representa
    uma coordenada de um vertice (x, y).

    :return: A area do poligono
    """

    soma1 = 0
    soma2 = 0

    for i in range(len(vertices) - 1):
        soma1 += vertices[i][0] * vertices[i + 1][1]
        soma2 += vertices[i][1] * vertices[i + 1][0]
    
    soma1 += vertices[-1][0] * vertices[0][1]
    soma2 += vertices[-1][1] * vertices[0][0]

    area = abs(soma1 - soma2)
    area = area / 2

    return area


if __name__ == '__main__':
    quadrado = [
        [0, 0],
        [0, 4],
        [4, 4],
        [4, 0]
    ]

    print(f'A area do quadrado eh: {gauss(quadrado)}')  # -> 16.0
