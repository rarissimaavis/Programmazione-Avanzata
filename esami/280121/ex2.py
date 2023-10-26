"""
Scrivere nel file esercizio2.py un decorator factory myDecoratorFact che prende in input un intero n e restituisce un
decoratore di funzione che modifica il comportamento della funzione decorata in modo che se la funzione è invocata con
numero di argomenti diverso da n allora la funzione lancia TypeError in modo che il programma fornito dalla docente
effettui le stampe desiderate (si veda la parte commentata alla fine del file).
"""
from functools import wraps


def decFact(n):
    def dec(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if len(args) + len(kwargs) != n:
                raise TypeError
            return f(*args, **kwargs)

        return wrapper

    return dec


@decFact(2)
def add(a, b):
    return a + b


print(add(1, 2))
try:
    add(1)
except TypeError as e:
    print("ue")
