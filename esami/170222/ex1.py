"""
Scriva nel file esercizio1.py una classe StranaTupla che estende la classe tuple e funziona in modo tale che ogni volta che
viene creata una sua istanza questa contiene solo gli elementi di ordine dispari della collezione iterabile passata a StranaTupla().
Ad esempio, se viene invocato StranaTupla([‘a’,’h’,5,’dado’,4]) allora l’istanza di StranaTupla creata è (‘a’, 5,4).
"""


class StranaTupla(tuple):
    def __new__(cls, iterable):
        elem = []
        for i, item in enumerate(iterable):
            if i % 2 == 0:
                elem.append(item)
        return super().__new__(cls, elem)


L = ['a', 'h', 5, 'dado', 4]
t = StranaTupla(L)
print(t)
