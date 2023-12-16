"""
Método que calcula por força bruta o segmento da soma máxima de um vetor qualquer.
Esse método vai calcular a soma de todos os segmentos possíveis de um vetor 
e identificar por meio de comparações qual o maior deles.
"""
def segmentoMaximo(vetor):
    # posição de inicio do segmento
    e = 0
    # posição de fim do segmento
    d = 0
    # segmento com a maior soma
    maior_segmento_soma = 0
    limites = {0, 0}

    # formar todos os segmentos de um vetor, len(vetor) = n
    for e in range(len(vetor)):
        for d in range(e, len(vetor)):
            # calcula a soma do segmento
            soma_segmento = 0
            for indice in range(e, d + 1):
                soma_segmento = soma_segmento +  vetor[indice]
            # compara a soma do segmento com a maior soma de segmento encontrada
            if (soma_segmento > maior_segmento_soma):
                maior_segmento_soma = soma_segmento
                # identifica os limites do segmento
                limites = {e, d}
    
    return maior_segmento_soma, limites


def main():
    vetor = [-16, 20, -10, 12, 27, -6, -4, 8]

    maior_segmento, limites = segmentoMaximo(vetor)

    print(maior_segmento)
    print(limites)


main()