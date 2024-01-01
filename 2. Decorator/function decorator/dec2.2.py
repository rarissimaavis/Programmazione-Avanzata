"""
Scrivere il decoratore di funzione decora che trasforma la funzione decorata in una funzione che lancia
l’eccezione TypeError se uno o più argomenti non sono di tipo str. La funzione deve restituire una stringa
formata dagli argomenti ricevuti in input e dal risultato intervallati da uno spazio.
Non dimenticate di convertire il risultato in stringa quando lo inserite nella stringa output.

Esempio: se la funzione riceve in input “il” , “risultato”, “è” , la funzione non lancia l’eccezione e restituisce
la stringa “Il risultato è …” dove al posto dei puntini deve apparire il risultato della funzione.
"""
from functools import wraps


# versione della prof
def decora(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        out = ""
        for arg in list(args) + [v for k, v in kwargs.items()]:
            # for arg in chain((args), kwargs.values()):
            # chain iteratore su tutti gli argomenti in input

            if type(arg) != str:  # con tipo generico prende in input tipo e qua confronta con tipo
                raise TypeError
            out += arg + " "
        res = str(f(*args, **kwargs))
        out += res
        return out

    return wrapper


@decora
def add(a, b):
    return a + b


result = add("1", "2")
print(result)
