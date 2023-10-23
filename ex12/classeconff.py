"""
Scrivere un decorator factory che prende in input una classe ClasseConFF e due stringhe funz e ff e restituisce
un decoratore di classe che decora una classe in modo tale che se viene invocata funz di fatto al posto di funz
viene invocata la funzione ff della classe ClasseConFF.
"""


def decFact(funz, ff):
    def dec(cls):
        if hasattr(cls, funz):
            setattr(cls, funz, getattr(cls, ff))
        return cls
    return dec


@decFact("funz", "ff")
class ClasseConFF:
    def funz(self):
        print("funz")

    def ff(self):
        print("ff")


c = ClasseConFF()
c.funz()
c.ff()

