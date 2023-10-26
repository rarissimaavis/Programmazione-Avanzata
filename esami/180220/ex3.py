"""
Scrivere un decorator factory decoratorFactory che permette di parametrizzare il decoratore dell’esercizio 2 con un
tipo t in modo che l’iteratore restituito da elencaVariabili iteri solo sulle variabili di istanza di tipo t.
Il codice relativo a questo esercizio deve essere scritto nel file esercizio3.py.
"""


def decFact(t):
    def decoratoreDiClasse(cls):
        def elencaVariabili(self):
            for key, value in self.__dict__.items():
                if isinstance(value, t):
                    yield key

        setattr(cls, "elencaVariabili", elencaVariabili)
        return cls

    return decoratoreDiClasse


@decFact(str)
class C:
    def __init__(self):
        self.a = 1
        self.b = 3.3
        self.c = "ao"
        self.d = 2


c = C()
for x in c.elencaVariabili():
    print(x)
