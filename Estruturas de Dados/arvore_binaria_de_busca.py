
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
# 61, 43, 16, 11, 32, 51, 55, 89, 66, 79, 77, 82

ROOT = 'root'  # valor constante que será usado como valor padrão em alguns casos no código.

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
    

    # Para a remoção de um elemento da árvore, tem 3 casos possíveis:
    # 1. Quando o elemento removido é uma folha.
    # 2. Quando o elemento removido tem apenas um filho (esquerda ou direita)
    # 3. Quando o elemento removido tem os dois filhos (esquerda e direita)
    # No 3º caso removemos o elementos, e substituimos pelo menor elemento da sua
    # sub-árvore da direita.

    def remove(self, element, node=ROOT):
        if node == ROOT:
            node = self.root
        
        # Desceu até um ramo nulo, ou seja, o elemento não está na árvore.
        if node is None:
            return node

        # se o elemento for menor, ele desce para a esquerda
        if element < node.data:
            node.left = self.remove(element, node.left)
        
        # se o elemento for menor, ele desce para a direita
        elif element > node.data:
            node.right = self.remove(element, node.right)

        # Elemento encontrado, ou seja, igual.
        else:
            # O primeiro caso, quando o elemento a ser removido é uma folha
            # retorna-se None, ao filho da esquerda ou da direita do pai do elemento, 
            # que é equivalente a remover o elemento.

            # O segundo caso, quando o elemento que apenas um filho (esquerda ou direita),
            # retorna para como filho (à esquerda ou direita) do pai do elemento, o nó do
            # filho que não é Nulo do elemento removido.

            if node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            # O terceiro caso, quando o elemento tem dois filhos.
            else:
                # O substituto será o menor elemento da sub-árvore da direita,
                # que vai substituir o elemento removido.
                substitute = self.min(node.right)

                # Trocando o valor do removido pelo seu substituto.
                node.data = substitute

                # removendo o valor substituto da sub-árvore da direita.
                node.right = self.remove(substitute, node.right)

        # retornando o proprio nó para os casos que não foram feitas alterações para à esquerda ou direita
        return node  

    
    # O menor elemento da árvore está o máximo à esquerda,
    # e que não possua um filho à esquerda.
    def min(self, node=ROOT):
        if node == ROOT:
            node = self.root

        while node.left is not None:
            node = node.left

        return node.data


    # O maior elemento da árvore está o máximo à direita,
    # e que não possua um filho à direita.
    def max(self, node=ROOT):
        if node == ROOT:
            node = self.root

        while node.right is not None:
            node = node.right

        return node.data


    # Percurso em pré ordem.
    # O percurso mostra a raíz, depois o elemento à esquerda e o elemento à dereita.
    # A ordem visitada no exemplo visto acima sera:
    # 61, 43, 16, 11, 32, 51, 55, 89, 66, 79, 77, 82

    def pre_order_route(self, node=ROOT):
        if node == ROOT:
            node = self.root

        if node is not None:
            print(node, end=' ')

            self.pre_order_route(node.left)
            self.pre_order_route(node.right)
            

    # Percurso em ordem simétrica/em ordem.
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


if __name__ == '__main__':
    bst = BinarySearchTree()

    # valores do exemplo
    valores = [61, 43, 89, 16, 51, 66, 11, 32, 55, 79, 77, 82]

    for i in valores:
        bst.insert(i)

    print('Percurso em Pré Ordem:')
    bst.pre_order_route()
    
    print('\n\nPercurso em Ordem Simétrica/Em ordem:')
    bst.inorder_route()

    print('\n\nPercurso em Pós Ordem:')
    bst.post_order_route()
    
    print('\n\nPercurso em Nível:')
    bst.route_at_level()
    
    print('\n')

    print(f'Menor elemento da árvore: {bst.min()}')  # -> 11
    print(f'Maior elemento da árvore: {bst.max()}')  # -> 89
    print(f'Altura da árvore: {bst.height()}')  # -> 5
    
    print(bst.remove(66))  # <- removendo o 66
    
    print('\nPercurso em Ordem Simétrica/Em ordem:')
    bst.inorder_route()
    
    print('\n\nPercurso em Nível:')
    bst.route_at_level()
           
