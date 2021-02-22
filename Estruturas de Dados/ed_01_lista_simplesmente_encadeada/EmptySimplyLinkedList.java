
package ed_01_lista_simplesmente_encadeada;

@SuppressWarnings("serial")

// A exceção será o nome da classe, ou seja,
// quando a lista estiver vazia.
class EmptySimplyLinkedList extends RuntimeException {  // está herdando da classe RuntimeException
    public EmptySimplyLinkedList(String error) {
        super(error);
    }
}
