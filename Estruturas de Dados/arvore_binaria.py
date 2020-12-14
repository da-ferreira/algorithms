"""
Autor: David Ferreira de Almeida
Implementacao de uma arvore binaria
"""

# o nó permite ligar os elementos esparsos da árvore
class Node:
    def __init__(self, element):  # atributos da classe
        self.data = element
        self.left = None
        self.right = None
    
    
    def __str__(self):
        return f'{self.data}'


class BinaryTree:
    def __init__(self, element=None):

        # Raiz da arvore; a partir dela é possivel fazer as demais operacoes
        if element is not None:
            self.root = Node(element)
        else:
            self.root = None

    
    # Percurso em ordem simétrica a partir do nó passado como parâmetro.
    #      '+'
    #    /     \
    #  'a'      '*'
    #          /   \
    #        'b'    '-'
    #              /    \
    #            '/'    'e' 
    #           /   \
    #         'c'   'd'
    #
    # A ordem visitada no exemplo acima sera:
    # (a+(b*((c/d)-e)))

    def simetric_route(self, node=None):
        if node is None:
            node = self.root
        
        # Chamando recursivamente e mostrando os elementos

        if node.left is not None:
            # O print com o "(" não é necessário em percurso em ordem simétrica,
            # mas, é possivel geral uma expressão matemática com eles como no exemplo acima.  

            print('(', end='')
            self.simetric_route(node.left)
        
        print(node, end='')  # mostrando o elemento do nó

        if node.right is not None:
            self.simetric_route(node.right)
            print(')', end='')


    # Percurso em pós ordem: exibi os filhos da esquerda e direita antes de mostrar a sí mesmo,
    # visitando recursivamente sua sub-árvore da esquerda, e depois sua sub-árvore da direta.
    #           A
    #          / \
    #         /   \
    #        /     \
    #       B       C
    #      / \     /
    #     D   E   F 
    #        / \   \
    #       G   H   I
    #            \
    #             J
    #
    # A ordem visitada no exemplo acima sera: 
    # D, G, J, H, E, B, I, F, C, A

    def post_order_route(self, node=None):
        if node is None:  # Começa o percurso pela raíz da árvore
            node = self.root

        if node.left is not None:
            self.post_order_route(node.left)
        
        if node.right is not None:
            self.post_order_route(node.right)
        
        print(node)  # mostrando o elemento do nó
    

    # Altura da árvore: raíz ate sua folha mais profunda.
    # O objetivo é olhar a altura das sub-arvores da esquerda e direita,
    # utilizando o percurso em pós ordem, e pegar a maior altura e incrementar 1.
    def height(self, node=None):
        if node is None:
            node = self.root  # altura da arvore completa

        height_left = 0  # altura da sub-árvore esquerda
        height_right = 0  # altura da sub-árvore direita

        if node.left is not None:
            height_left = self.height(node.left)
        
        if node.right is not None:
            height_right = self.height(node.right)


        if height_left > height_right:
            return height_left + 1
            
        return height_right + 1


def ordem_simetrica_exemplo():
    tree = BinaryTree()  # para o percurso em ordem simetrica
    n1 = Node('a')
    n2 = Node('+')
    n3 = Node('*')
    n4 = Node('b')
    n5 = Node('-')
    n6 = Node('/')
    n7 = Node('c')
    n8 = Node('d')
    n9 = Node('e')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3
    
    tree.root = n2

    return tree


def pos_ordem_exemplo():
    tree = BinaryTree()  # para o percurso em pós ordem
    n0 = Node('A')
    n1 = Node('B')
    n2 = Node('C')
    n3 = Node('D')
    n4 = Node('E')
    n5 = Node('F')
    n6 = Node('G')
    n7 = Node('H')
    n8 = Node('I')
    n9 = Node('J')
    
    n0.left = n1
    n0.right = n2
    n1.left = n3
    n1.right = n4
    n4.left = n6
    n4.right = n7
    n7.right = n9
    n2.left = n5
    n5.right = n8

    tree.root = n0

    return tree


if __name__ == '__main__':
    tree = pos_ordem_exemplo()
    print('Percurso em pós ordem:')
    tree.post_order_route()

    print(f'\nA altura da árvore: {tree.height()}')   

    #tree2 = ordem_simetrica_exemplo()
    #print('Percurso em ordem simétrica:')
    #tree2.simetric_route()

    