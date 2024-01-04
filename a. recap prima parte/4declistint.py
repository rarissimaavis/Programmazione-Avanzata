"""
Definire un decoratore di funzione che trasforma una funzione che prende in input un numero variabile di numeri in una
funzione che prende in input una lista e opera solo sugli elementi della lista di tipo float, int e str convertiti in int
"""


def decInt(f):
    def wrapper(*args, **kwargs):
        L = []
        for arg in args:
            if not isinstance(arg, list):
                raise TypeError
            for el in arg:
                if isinstance(el, (int, float, str)):
                    try:
                        L.append(int(float(el)))
                    except ValueError:
                        pass
        for key, value in kwargs.items():
            if not isinstance(value, list):
                raise TypeError
            for el in value:
                if isinstance(el, (int, float, str)):
                    try:
                        L.append(int(float(el)))
                    except ValueError:
                        pass
        return f(*L)
    return wrapper


@decInt
def somma(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


res = somma([1, 2.5, '3', 4.7, '5.2', 'abc', 6])
print(res)

res = somma([1, 2.5, '3', 4.7, '5.2', 'abc', 6], my_list=[10, 20, '30'])
print(res)
