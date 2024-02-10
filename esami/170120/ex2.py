"""
Scrivere un decorator factory decFact(L1,L2) che prende in input una lista di stringhe e una stringa di oggetti e produce
un decoratore che fa in modo che le istanze della classe nascano non solo con le variabili di istanza aggiunte dal metodo
__init__ della classe ma anche con le seguenti variabili di istanza:
• per ogni i =1,…, len(L1), una variabile con nome uguale a quello della i-esima
  stringa di L1 e valore uguale all’i-esimo oggetto di L2.
Nel caso in cui __init__ della classe originaria aggiungeva gia` una variabile di istanza con nome uguale all’i-esima
stringa di L1 allora il valore della variabile deve essere quello assegnato da __init__ della classe originaria.
"""


def decFact(L1, L2):
    def dec(cls):
        __oldInit__ = cls.__init__

        def __newInit__(self, *args, **kwargs):
            __oldInit__(self, *args, **kwargs)
            for attr, value in zip(L1, L2):
                if not hasattr(self, attr):
                    setattr(self, attr, value)

        cls.__init__ = __newInit__
        return cls

    return dec


@decFact(["var1", "var2", "var3"], [10, 20, 30])
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


obj = MyClass(1, 2)
print(obj.a, obj.b)
print(obj.var1, obj.var2, obj.var3)

"""
1 2
10 20 30
"""
