
# Autor: David Ferreira de Almeida
# Implementacao de uma Árvore Binária
#
# Exemplo de uma árvore binária que será usado durante o código
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

ROOT = 'root'  # valor constante que será usado como valor padrão em alguns casos no código.

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

    # Percurso em pré ordem.
    # O percurso mostra a raíz, depois o elemento à esquerda e o elemento à dereita.
    # A ordem visitada no exemplo visto acima sera:
    # A, B, D, E, G, H, J, C, F, I

    def pre_order_route(self, node=ROOT):
        if node == ROOT:
            node = self.root

        if node is not None:
            print(node, end=' ')

            self.pre_order_route(node.left)
            self.pre_order_route(node.right)

    
    # Percurso em ordem simétrica.
    # O percurso mostra primeiro o elemento da esquerda, depois a raíz, e
    # o elemento da direita, recursivamente. É possivel representar expressões
    # matemáticas com este percurso.
    # A ordem visitada no exemplo visto acima sera:
    # D, B, G, E, H, J, A, F, I, C

    def inorder_route(self, node=None):
        if node is None:
            node = self.root
        
        # Chamando recursivamente e mostrando os elementos

        if node.left is not None:
            self.inorder_route(node.left)

        print(node, end=' ')  # mostrando o elemento do nó

        if node.right is not None:
            self.inorder_route(node.right)


    # Percurso em pós ordem: exibi os filhos da esquerda e direita antes de mostrar a sí mesmo,
    # visitando recursivamente sua sub-árvore da esquerda, e depois sua sub-árvore da direta.
    # A ordem visitada no exemplo visto acima sera: 
    # D, G, J, H, E, B, I, F, C, A

    def post_order_route(self, node=None):
        if node is None:  # Começa o percurso pela raíz da árvore
            node = self.root

        if node.left is not None:
            self.post_order_route(node.left)
        
        if node.right is not None:
            self.post_order_route(node.right)
        
        print(node, end=' ')  # mostrando o elemento do nó
    

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
    

    # Percurso em Nível
    # O elementos visitados são os de cada nivel da árvore, da esquerda para a direita.
    # Para obter esse percurso é necessário usar uma Fila, seguindo a regra: primeiro a entrar,
    # primeiro a sair.
    # A ordem visitada no exemplo visto acima sera: 
    # A, B, C, D, E, F, G, H, I, J
    
    def route_at_level(self, node=ROOT):
        if node == ROOT:
            node = self.root
        
        queue = []
        queue.append(node)  # insere no final, e remove do inicio

        while len(queue) > 0:
            node = queue.pop(0)

            if node.left is not None:
                queue.append(node.left)
            
            if node.right is not None:
                queue.append(node.right)
            
            print(node, end=' ')



def tree_exemple():
    tree = BinaryTree()
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
    tree = tree_exemple()

    print('Percurso em Pré Ordem:')
    tree.pre_order_route()

    print('\n\nPercurso em ordem simétrica/em ordem:')
    tree.inorder_route()
    print()
    
    print('\n\nPercurso em pós ordem:')
    tree.post_order_route()
    
    print('\n\nPercurso em Nível:')
    tree.route_at_level()
    

    print(f'\n\nA altura da árvore: {tree.height()}')   
    
       
