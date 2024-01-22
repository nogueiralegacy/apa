def guloso(vetor):
    soma_atual = maior_soma = vetor[0]

    for elemento in vetor[1:]:
        soma_atual = max(elemento, soma_atual + elemento)
        maior_soma = max(maior_soma, soma_atual)

    return maior_soma


def main():
    vetor = [-16, 20, -10, 12, 27, -6, -4, 8]

    maior_segmento = guloso(vetor)

    print(maior_segmento)


main()