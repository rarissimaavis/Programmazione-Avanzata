"""
Scrivere una funzione generatrice generaElementi che prende in input una lista L di elementi a due a due distinti
(non c'è bisogno di controllare che gli elementi siano distinti) e permette di ottenere un iteratore
che scandisce gli elemnti della lista nel seguente modo:
- la prima volta che viene invocato next si ottiene il primo elemento della lista L[0]
Per le invocazioni successive di next si ha il seguente comportamento:
Sia L[j] l'elemento generato con la più recente invocazione di next
- se L[j] è un intero k diverso da j e compreso tra 1 e len(L)-1 allora la prossima invocazione di next restituisce L[k]
- in caso contrario non vengono generati altri elementi e le invocazioni successive di next causano un'eccezione

"""


def generaElementi(L):
    i = 0
    while len(L) > i >= 0:
        yield L[i]
        if isinstance(L[i], int) and i != L[i]:
            i = L[i]
        else:
            i = -1


if __name__ == "__main__":
    print("\nI test")
    l = [2, 8, 6, 'a', 4, 1, 3]
    for n, x in enumerate(generaElementi(l), start=1):
        print("L'elemento generato dalla  invocazione {} di next e` {}".format(n, x))

    print("\nII test")
    l = []
    for n, x in enumerate(generaElementi(l)):
        print("L'elemento generato dalla  invocazione {} di next e` {}".format(n, x))

    print("\nIII test")
    l = [2, 8, 6, 1, 4, 5, 3]
    for n, x in enumerate(generaElementi(l), start=1):
        print("L'elemento generato dalla  invocazione {} di next e` {}".format(n, x))

"""Il programma deve stampare:
I test
L'elemento generato dalla  invocazione 1 di next e` 2
L'elemento generato dalla  invocazione 2 di next e` 6
L'elemento generato dalla  invocazione 3 di next e` 3
L'elemento generato dalla  invocazione 4 di next e` a

II test

III test
L'elemento generato dalla  invocazione 1 di next e` 2
L'elemento generato dalla  invocazione 2 di next e` 6
L'elemento generato dalla  invocazione 3 di next e` 3
L'elemento generato dalla  invocazione 4 di next e` 1
L'elemento generato dalla  invocazione 5 di next e` 8

"""
