"""
Scrivere nel file esercizio2.py un decoratore di classe decoratoreDiClasse che dota la classe decorata di un metodo di istanza elencaVariabili.
Il metodo elencaVariabili è un generatore che restituisce un iteratore delle variabili di istanza di tipo int dell’istanza per cui è invocato.
"""


def decoratoreDiClasse(cls):
    def elencaVariabili(self):
        for key, value in self.__dict__.items():
            if isinstance(value, int):
                yield key

    setattr(cls, "elencaVariabili", elencaVariabili)
    return cls


@decoratoreDiClasse
class C:
    def __init__(self):
        self.a = 1
        self.b = 3.3
        self.c = "ao"
        self.d = 2


c = C()
for x in c.elencaVariabili():
    print(x)
