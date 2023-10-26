"""
Scrivere nel file esercizio2.py una funzione applica(da_fare) che prende in input una tupla da_fare che contiene tuple
della forma (m, a1,a2,…) dove m è un metodo di istanza di una certa classe C e a1, a2,… sono gli argomenti diversi
da self con cui deve essere invocato m.
Nella prima tupla di da_fare, m è la classe C e gli argomenti sono quelli da passare al costruttore per creare l’istanza
di C su cui invocare i metodi delle restanti tuple di da_fare.
La funzione applica restituisce una lista contenente come primo elemento l’istanza creata e come restanti elementi i
valori restituiti dalle invocazioni dei metodi delle restanti tuple.
"""


def applica(da_fare):
    toReturn = []
    command = da_fare[0]
    f, *a = command
    obj = f(*a)
    toReturn.insert(0, obj)
    for i in range(1, len(da_fare)):
        f, *a = da_fare[i]
        res = f(obj, *a)
        toReturn.append(res)
        #toReturn.insert(0, obj)
    return toReturn


class C:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ao(self, c, d):
        return c + d


res = applica(((C, 1, 2), (C.ao, 2, 1), (C.ao, 3, 4)))
print(res)
