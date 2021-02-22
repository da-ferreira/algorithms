
package edjava_02_lista_duplamente_encadeada;

/**
 * @author david-ferreira
 */

public class Node {
    protected String element;
    private Node prev;  // elemento anterior.
    private Node next;  // elemento posterior.
	
    // método construtor.
    public Node (String elemento, Node anterior, Node posterior) {  
        element = elemento;
        prev = anterior;
        next = posterior;
    }
	
    public String getElement() {
        return element;  // retorna o elemento do nó
    }
	
    public Node getPrev() {
        return prev;  // retorna o elemento anterior do nó.
    }
	
    public Node getNext() {
        return next;  // retorna o proximo elemento do nó
    }

    public void setElement(String newElement) {
        element = newElement;  // modifica o elemento do nó
    }

    public void setPrev(Node newPrev) {
        prev = newPrev;  // modifica o prev do nó.
    }

    public void setNext(Node newNext) {
        next = newNext;  // modifica o next do nó.
    }
}
