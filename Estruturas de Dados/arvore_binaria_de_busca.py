
# Autor: David Ferreira de Almeida
# Implementacao de uma Árvore Binária de Busca
#
# Exemplo de uma Árvore Binária de Busca que será usado durante o código.
# O elemento à esquerda são menores que o valor do pai, e os elementos à 
# direita são maiores ou iguais ao valor do pai.
#
#             61
#             /\ 
#            /  \
#           /    \
#          43    89
#         / \    /
#        16 51  66
#       / \  \   \
#      11 32 55  79
#                / \
#               77 82
#

ROOT = 'root'

# o nó permite ligar os elementos esparsos da árvore
class Node:
    def __init__(self, element):  # atributos da classe
        self.data = element
        self.left = None
        self.right = None


    def __str__(self):
        return f'{self.data}'


class BinarySearchTree:
    def __init__(self, element=None, node=None):

        # Iniciando a raíz da árvore a partir de um nó já criado.        
        if node is not None:
            self.root = node

        # Caso contrário, cria-se um nó e atribui para a raíz da árvore.
        elif element is not None:
            self.root = Node(element)
        else:
            self.root = None
    

    def insert(self, element):
        father = None  # pai do elemento que será inserido
        point = self.root

        while point is not None:
            father = point
            
            # Se o elemento for menor, ele segue descendo à esquerda,
            # caso contrário, segue descendo à direita.
            if element < point.data:
                point = point.left
            else:
                point = point.right
            
        # Se a árvore estiver vazia, o elemento que entra é a raíz.
        if father is None:
            self.root = Node(element)
        
        # Adicionando o elemento
        elif element < father.data:
            father.left = Node(element)
        else:
            father.right = Node(element)
    

    def search(self, element, node=0):

        # Começa a busca pela raíz.
        if node == 0:
            node = self.root

        # Caso o item não esteja na árvore retorna None
        if node is None:
            return node

        # Retorna uma sub-árvore
        elif node.data == element:
            return BinarySearchTree(node=node)
        
        elif element < node.data:
            return self.search(element, node.left)  # Se o elemento for menor que o valor do nó, ele segue pela esquerda.
        
        return self.search(element, node.right)  # Se for maior, segue pela direita.


    # Percurso em ordem simétrica.
    # O percurso mostra primeiro o elemento da esquerda, depois a raíz, e
    # o elemento da direita, recursivamente. Na BST os elementos ficam em ordem crescente,
    # quando é usado esse percurso.
    # A ordem visitada no exemplo visto acima sera:
    # 11, 16, 32, 43, 51, 55, 61, 66, 77, 79, 82, 89

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
    # 11, 32, 16, 55, 51, 43, 77, 82, 79, 66, 89, 61

    def post_order_route(self, node=None):
        if node is None:  # Começa o percurso pela raíz da árvore
            node = self.root

        if node.left is not None:
            self.post_order_route(node.left)
        
        if node.right is not None:
            self.post_order_route(node.right)
        
        print(node, end=' ')  # mostrando o elemento do nó
    

    # Percurso em Nível
    # O elementos visitados são os de cada nivel da árvore, da esquerda para a direita.
    # Para obter esse percurso é necessário usar uma Fila, seguindo a regra: primeiro a entrar,
    # primeiro a sair.
    # A ordem visitada no exemplo visto acima sera: 
    # 61, 43, 89, 16, 51, 66, 11, 32, 55, 79, 77, 82

    
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


if __name__ == '__main__':
    bst = BinarySearchTree()

    # valores do exemplo
    valores = [61, 43, 89, 16, 51, 66, 11, 32, 55, 79, 77, 82]

    for i in valores:
        bst.insert(i)
    
    print('Percurso em Nível:')
    bst.route_at_level()

    print('\n\nPercurso em Pós Ordem:')
    bst.post_order_route()

    print('\n\nPercurso em Ordem Simétrica:')
    bst.inorder_route()
    print()
  
