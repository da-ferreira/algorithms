
package algoritmos;

/**
 * @author da-ferreira
 */

public class BuscaBinaria {
    public static int sort(int vetor[], int item) {
        int inicio = 0;
        int fim = vetor.length - 1;
        
        while (inicio <= fim) {
            int meio = (inicio + fim) / 2;
            
            if (item == vetor[meio]) {
                return meio;
            }
            else if (item < vetor[meio]) {
                fim = meio - 1;
            }
            else if (item > vetor[meio]) {
                inicio = meio + 1;
            }
        }
        
        return -1;  // o elemento não está no vetor.
    }
}
