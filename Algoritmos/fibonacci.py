"""
Implementação da Sequência de Fibonacci
"""

def fibonacci(termo):
    """
    :param termo: O termo da sequencia
    :return: O valor do termo informado
    """

    if termo in [1, 2]:
        return termo - 1
    
    term1 = 0
    term2 = 1

    for i in range(termo - 2):
        fib = term1 + term2
        
        term1 = term2
        term2 = fib
    
    return fib


if __name__ == '__main__':
    t = int(input('Termo: '))
    print(f'O {t}° termo de fibonacci é: {fibonacci(t)}')
