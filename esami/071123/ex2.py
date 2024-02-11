"""
Scrivere un decorator factory decoratorFact che prende in input un tipo t e restituisce un decoratore di classe decorator
che dota la classe decorata di un metodo di istanza addToList che restituisce una lista contenente i nomi e i valori
delle variabili di tipo t dell’istanza per cui è invocato. Ciascuna coppia (nome, valore) deve essere all'interno
di una tupla. Il codice della classe non deve essere modificato.
"""


def decoratorFact(t):
    def decorator(cls):
        def addToList(self):
            l = []
            for name, value in self.__dict__.items():
                if isinstance(value, t):
                    l.append((name, value))
            return l
        setattr(cls, "addToList", addToList)
        return cls
    return decorator


@decoratorFact(int)
class classe1:
    def meth1(self):
        self.w1 = dict({'dado': 408, 'sei': 9})
        self.w2 = dict({'lancio': 4139})
        self.v1 = classe1()
        self._a = 3

    def meth2(self):
        self.w3 = dict({'pippo': 408, 'topolino': 39})
        self.i = 5
        self.e2 = classe1()
        self.w4 = dict({'paperino': 12, 'minnie': 43})


@decoratorFact(classe1)
class classe2(classe1):
    def __init__(self):
        self.m = classe1()


q = classe2()
L = q.addToList()
print("le variabili di istanza di q di tipo classe1 sono:", L)
q.meth1()
L = q.addToList()
print("le variabili di istanza di q di tipo classe1 sono:", L)
q.meth2()
L = q.addToList()
print("le variabili di istanza di q di tipo classe1 sono:", L)
y = classe1()
L = y.addToList()
print("le variabili di istanza di y di tipo int sono:", L)
y.meth1()
L = y.addToList()
print("le variabili di istanza di y di tipo int sono:", L)

"""
Il programma deve stampare :
le variabili di istanza di q di tipo classe1 sono: [('m', <__main__.classe1 object at 0x11484f2e0>)]
le variabili di istanza di q di tipo classe1 sono: [('m', <__main__.classe1 object at 0x11484f2e0>), ('v1', <__main__.classe1 object at 0x11484e590>)]
le variabili di istanza di q di tipo classe1 sono: [('m', <__main__.classe1 object at 0x11484f2e0>), ('v1', <__main__.classe1 object at 0x11484e590>), ('e2', <__main__.classe1 object at 0x11484f2b0>)]
le variabili di istanza di y di tipo int sono: []
le variabili di istanza di y di tipo int sono: [('_a', 3)]
"""
