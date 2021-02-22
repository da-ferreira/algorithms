
package ed_01_lista_simplesmente_encadeada;

/**
 * @author david-ferreira
 */

class Node {
    private String element;  // A lista será homogenea, os elementos são strings
    private Node next;
	
    
    // Em java o método construtor é representado pelo nome da classe.
    // Cria um nó com o elemento e o proximo nó.
    public Node(String dado, Node nodo) {
        element = dado;
        next = nodo;
    }
	
    public String getElement() {
        return element;  // retorna o elemento do nó
    }

    public Node getNext() {
        return next;  // retorna o proximo elemento do nó
    }

    public void setElement(String newElement) {
        element = newElement;  // modifica o elemento do nó
    }

    public void setNext(Node newNext) {
        next = newNext;  // modifica o next do nó.
    }
}
