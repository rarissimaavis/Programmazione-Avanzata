"""
Generatore ricorsivo che restituisce gli elementi di una lista invertiti
"""


def recRevList(L):
    if not L:
        return
    yield L[-1]
    yield from recRevList(L[:-1])


L = [1, 2, 3, 4, 5]
for item in recRevList(L):
    print(item)
