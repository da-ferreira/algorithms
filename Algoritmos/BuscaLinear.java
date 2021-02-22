
package algoritmos;

/**
 * @author david-ferreira
 */

public class BuscaLinear {
    public static int busca_linear(int vetor[], int item) {
        for (int i=0; i < vetor.length; i++)
            if (vetor[i] == item) {
                return i;
            }
        
        return -1; // o elemento nao esta no vetor.
    }
}
