"""
Scrivere nel file esercizio2.py un decorator factory dFact che restituisce un decoratore di funzione che “trasforma”
la funzione f in un generatore che all’i-esima invocazione di next restituisce il valore ottenuto invocando f con gli
argomenti ottenuti sommando L[i] a tutti gli argomenti con cui la funzione f è invocata originariamente.
Se la suddetta somma causa un’eccezione TypeError allora il generatore smette di restituire valori.
"""
from functools import wraps
from math import prod


def dFact(L):
    def dec(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                for i in range(len(L)):
                    newArgs = [arg + L[i] for arg in args]
                    newKwargs = {key: value + L[i] for key, value in kwargs.items()}
                    yield f(*newArgs, **newKwargs)
            except TypeError:
                return

        return wrapper

    return dec


# primo test
def g(x, z=4):
    return prod([x, z])


h = dFact([0, 2, 1])(g)
t = dFact([0, 2, 1, "5", 8])(g)

print(
    "Eseguo un for che stampa 3 valori, cioe` un numero di valori uguale al numero di elementi della la lista passata al decorator factory")
for r in h(2):
    print(r)
print("Eseguo un for che stampa 3 valori nonostante la lista passata al decorator factory contenesse 5 elementi")
for r in t(2):
    print(r)


# secondo test
def g(x, z=4, *y):
    return prod([x, z] + list(y))


h = dFact([0, 2, 1])(g)
t = dFact([0, 2, 1, "5", 8])(g)
print(
    "Eseguo un for che stampa 3 valori, cioe` un numero di valori uguale al numero di elementi della la lista passata al decorator factory")
for r in h(2, 1, 0, 3):
    print(r)
print("Eseguo un for che stampa 3 valori nonostante la lista passata al decorator factory contenesse 5 elementi")
for r in t(2, 1, 0, 3):
    print(r)


# terzo test
def g(x, z=4, **y):
    return prod([x, z] + list(y.values()))


h = dFact([0, 2, 1])(g)
t = dFact([0, 2, 1, "5", 8])(g)
print(
    "Eseguo un for che stampa 3 valori, cioe` un numero di valori uguale al numero di elementi della la lista passata al decorator factory")
for r in h(*(1, 2), k1=4, k2=3):
    print(r)
print("Eseguo un for che stampa 3 valori nonostante la lista passata al decorator factory contenesse 5 elementi")
for r in t(*(1, 2), k1=4, k2=3):
    print(r)

"""Il programma deve stampare:
Eseguo un for che stampa 3 valori, cioe` un numero di valori uguale al numero di elementi della la lista passata al decorator factory
8
16
12
Eseguo un for che stampa 3 valori nonostante la lista passata al decorator factory contenesse 5 elementi
8
16
12
Eseguo un for che stampa 3 valori, cioe` un numero di valori uguale al numero di elementi della la lista passata al decorator factory
0
120
24
Eseguo un for che stampa 3 valori nonostante la lista passata al decorator factory contenesse 5 elementi
0
120
24
Eseguo un for che stampa 3 valori, cioe` un numero di valori uguale al numero di elementi della la lista passata al decorator factory
24
360
120
Eseguo un for che stampa 3 valori nonostante la lista passata al decorator factory contenesse 5 elementi
24
360
120


"""
