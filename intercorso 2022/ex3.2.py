"""
Scrivere nel file esercizio3.py un decorator factory decFact(L1,L2) che prende come
argomenti una lista L1 di stringhe e una lista L2 di oggetti e produce un decoratore di
classe che fa in modo che le istanze della classe nascano non solo con le variabili di istanza
aggiunte dal metodo __init__ della classe ma anche con le seguenti variabili di istanza:
• per ogni i =0,..., len(L1)-1, una variabile con nome uguale a L1[i] e valore uguale a
L2[i]. Nel caso in cui il metodo __init__ della classe originaria aggiunge gia` una
variabile di istanza con lo stesso nome di una di quelle aggiunte dal decoratore
allora il valore della variabile deve essere quello assegnato dal decoratore.
• potete assumere che le due liste L1 e L2 abbiano la stessa lunghezza.
"""


def decFact(L1, L2):
    def dec(cls):
        cls.oldInit = cls.__init__

        def newInit(self, *args, **kwargs):
            cls.oldInit(self, *args, **kwargs)
            for v, x in zip(L1, L2):
                setattr(self, v, x)

        cls.__init__ = newInit
        return cls

    return dec


@decFact(["x1", "x2"], [100, 200])
class C1:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2


c1 = C1(10, 20)

print(c1.x1)
print(c1.x2)
