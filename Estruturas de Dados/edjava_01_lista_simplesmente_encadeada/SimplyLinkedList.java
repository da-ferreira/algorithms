
package edjava_01_lista_simplesmente_encadeada;

/**
 * @author david-ferreira
 */

public class SimplyLinkedList {
    protected Node head;  // nó da cabeça da lista.
    protected Node tail;  // nó da calda da lista.
    protected long size;  // tamanho da lista
	
	
    public SimplyLinkedList() {  // construtor que cria uma lista vazia.
        head = null; 
        tail = null;
        size = 0;
    }

    public void addHead(String element) {
        Node newElement = new Node(element, head);
		
        if (size == 0)
                tail = newElement;

        head = newElement;
        size++;
    }

    public void addTail(String element) {
        Node newElement = new Node(element, null);  // criando um novo elemento e apontando next dele para null.

        if (size == 0) {
            head = newElement;
            tail = newElement;
        }
        else {
            tail.setNext(newElement);
            tail = newElement;
        }

        size++;
    }

    public void removeFirst() {
        if (size == 0) 
            throw new EmptySimplyLinkedList("The list is empty.");

        Node to_remove = head;  // variavel está apontando para cabeça, que sera removida.
        head = head.getNext();
        to_remove.setNext(null);  // aponta o next do elemento removido para null (garbage collector)
        size--;
    }
	
    // retorna a lista em forma de String, ex: "[]".
    public String toString() {
        String lista = "[";
        Node point = head;

        while (point != null) {
            lista += point.getElement();
                point = point.getNext();

            if (point != null) 
                lista += ", ";		
        }

        return lista + "]";	
    }
	
    public long getSize() {
	return size;
    }
}
