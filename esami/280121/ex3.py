"""
Scrivere la classe FSet che estende frozenset in modo tale che quando si crea un’istanza di
FSet , l’istanza di FSet creata contenga solo gli elementi di ordine dispari dell’oggetto
iterabile (il primo, il terzo, ecc.) passata come argomento a FSet(). Se FSet() non prende
input niente allora l’istanza creata è vuota.
NB: gli elementi di ordine dispari corrispondono agli elementi di indice pari.
"""


class FSet(frozenset):
    def __new__(cls, iterable):
        elem = []
        for i, item in enumerate(iterable):
            if i % 2 == 0:
                elem.append(item)
        return super().__new__(cls, elem)


L = ['a', 'h', 5, 'dado', 4]
s = FSet(L)
print(s)
