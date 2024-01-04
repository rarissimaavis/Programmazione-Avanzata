"""
Definire un decoratore di funzione che trasforma una funzione che prende in input un numero variabile di numeri in una
funzione che prende in input una lista e opera solo sugli elementi della lista di tipo float, int e str convertiti in int
"""


def decInt(f):
    def wrapper(*args, **kwargs):
        if len(args) + len(kwargs) != 1 or len(args) == 1 and not isinstance(args[0], list) or len(kwargs) == 1 and not isinstance(list(kwargs.values())[0], list):
            raise TypeError
        L = []
        if args:
            for el in args[0]:
                try:
                    L.append(int(float(el)))
                except ValueError:
                    pass
        if kwargs.items():
            for el in list(kwargs.values())[0]:
                try:
                    L.append(int(float(el)))
                except ValueError:
                    pass
        return f(*L)
    return wrapper


@decInt
def somma(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


class MyClass:
    number = "11.2"

    def __index__(self):
        return self.number


cls = MyClass()
res = somma([cls.number, 2.5, '3', 4.7, '5.2', 'abc', 6])
print(res)
