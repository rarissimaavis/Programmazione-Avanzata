"""
Scrivere il decoratore di funzione decora che trasforma la funzione decorata in una funzione che lancia
l’eccezione TypeError se uno o più argomenti non sono di tipo str. La funzione deve restituire una stringa
formata dagli argomenti ricevuti in input e dal risultato intervallati da uno spazio.
Non dimenticate di convertire il risultato in stringa quando lo inserite nella stringa output.

Esempio: se la funzione riceve in input “il” , “risultato”, “è” , la funzione non lancia l’eccezione e restituisce
la stringa “Il risultato è …” dove al posto dei puntini deve apparire il risultato della funzione.
"""
from functools import wraps


def decora(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not all(isinstance(arg, str) for arg in args) or not all(
                isinstance(value, str) for key, value in kwargs.items()):
            raise TypeError

        res = f(*args, **kwargs)
        return " ".join(args) + " " + str(res)

    return wrapper


@decora
def add(a, b):
    return a + b


try:
    result = add("1", "2")
    print(result)
except TypeError:
    print("TypeError was raised because one of the arguments is not a string.")


@decora
def f(a, b, c, number):
    return number


try:
    result = f("Il", "risultato", "è", number="12")
    print(result)
except TypeError:
    print("TypeError was raised because one of the arguments is not a string.")
