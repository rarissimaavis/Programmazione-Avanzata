"""
Modificare la funzione al punto precedente in modo che la funzione decorata
• operi su qualsiasi elemento della lista che puo` essere convertito in int
• non lanci un’eccezione se un elemento della lista non puo` essere convertito a int
    • cio` puo` non dipendere dal tipo dell’elemento ma dal suo specifico valore, ad esempio "anna"
"""


def decInt(f):
    def wrapper(*args, **kwargs):
        L = []
        for arg in args:
            if not isinstance(arg, list):
                raise TypeError
            for el in arg:
                try:
                    L.append(int(float(el)))
                except ValueError:
                    pass
        for key, value in kwargs.items():
            if not isinstance(value, list):
                raise TypeError
            for el in value:
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
