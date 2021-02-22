
package edjava_02_lista_duplamente_encadeada;

/**
 * @author david-ferreira
 */

public class DoublyLinkedList {
    protected Node header;  // sentinela cabeçalho.
    protected Node trailer;  // sentinela cauda.
    protected Long size;
	
	
    public DoublyLinkedList() {  // metodo construtor. 
        header = new Node(null, null, null);
        trailer = new Node(null, header, null);  // o prev do trailer aponta para o header(cabeçalho).
        header.setNext(trailer);  // o next do header aponta para o trailer(cauda).
        size = (long) 0;
    }

    // Adiciona um nodo "newElement" antes de "element_in_frent"
    // Gera um "IllegalArgumentException" se element_in_frent for o cabeçalho.
    public void addBefore(Node element_in_frent, Node newElement) throws IllegalArgumentException {
        Node temp = element_in_frent.getPrev();

        /*
         * 1. Coloca como prev do newElement o nó que está atras do element_in_frent.
         * 2. Coloca como next do newElement o nó do element_in_frent.
         * 3. Coloca como prev do element_in_frent o novo elemento(addBefore).
         * 4. Coloca como next do temp o newElement (no começo, o temp estava atras do element_in_frent)
         */

        newElement.setPrev(temp);  
        newElement.setNext(element_in_frent);
        element_in_frent.setPrev(newElement);
        temp.setNext(newElement);

        size++;
    }
	
    // Adiciona um nodo "newElement" depois de "element_behind"
    // Gera um "IllegalArgumentException" se element_behind for a cauda.
    public void addAfter(Node element_behind, Node newElement) throws IllegalArgumentException {
        Node temp = element_behind.getNext();

        /*
         * 1. Coloca como prev do newElement o nó element_behind.
         * 2. Coloca como next do newElement o nó que estava a frente do element_behind.
         * 3. Coloca como next do elemento_behind o novo elemento(addAfter).
         * 4. Coloca como prev do temp o newElement (no começo, o temp estava na frente do element_behind)
         */

        newElement.setPrev(element_behind);  
        newElement.setNext(element_behind.getNext());
        element_behind.setNext(newElement);
        temp.setPrev(newElement);

        size++;
    }
		
    // Gera um "IllegalArgumentException" se element for o cabeçalho/cauda.
    public void removeElement(Node element) throws IllegalArgumentException {
        Node atras = element.getPrev();
        Node frente = element.getNext();

        atras.setNext(frente);
        frente.setPrev(atras);

        element.setPrev(null);
        element.setNext(null);
        size--;
    }
	
    public void removeFirst() {
        removeElement(header.getNext());
    }

    public void removeLast() {
        removeElement(trailer.getPrev());
    }

    public void addLast(Node newElement) {
        addBefore(trailer, newElement);  // passando a sentinela da cauda (trailer).
    }

    public void addFirst(Node newElement) {
        addBefore(header.getNext(), newElement);  // passando a cabeça da lista.
    }

    public Node getLast() {  
        return trailer.getPrev();  // retorna o ultimo nó.
    }
	
    // retorna a lista em forma de String, ex: "[]".
    public String toString() {
        String lista_em_string = "[";
        Node point = header.getNext();

        while (point.getElement() != null) {
            lista_em_string += point.getElement();
            point = point.getNext();

            if (point.getElement() != null) 
                lista_em_string += ", ";		
        }

        return lista_em_string + "]";	
    }
	
    public long getSize() {
	return size;
    }
}
