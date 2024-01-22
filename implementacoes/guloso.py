"""
Método que a partir de algoritmo guloso, algoritmo Kadane, encontra o maior 
segmento de um vetor de inteiros. O algoritmo têm complexidade O(n), ou seja, 
polinomeal já que percorre o vetor apenas uma vez para encontrar o Segmento da Soma Máxima.
"""

def guloso(vetor):
    soma_atual = maior_soma = vetor[0]
    e = 0
    d = 0

    for indice in range(1, len(vetor)):

        # registra o limite inferior do segmento da soma máxima
        if (vetor[indice] > soma_atual + vetor[indice]):
            e = indice
        # verifica se é necessário começar um novo segmento
        soma_atual = max(vetor[indice], soma_atual + vetor[indice])
        maior_soma = max(maior_soma, soma_atual)
        # registra o limite superior do segmento da soma máxima
        if (maior_soma == soma_atual):
            d = indice

    limites = {e, d}

    return maior_soma, limites


def main():
    vetor = [-16, 20, -10, 12, 27, -6, -4, 8]

    maior_segmento, limites = guloso(vetor)

    print(maior_segmento)
    print(limites)


main()