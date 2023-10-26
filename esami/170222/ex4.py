"""
Scriva nel file esercizio4.py un decorator factory decFact(*pos_args,**keyw_args) che restituisce un decoratore di classe
che fa in modo che le istanze della classe vengano inizializzate come descritto di seguito
• per ogni i =1,..., len(pos_args), vi sia una variabile di istanza con nome uguale a quello della i-esima stringa di
    pos_args e valore uguale a None (si assuma che gli elementi di pos_args siano di tipo str)
• per ogni parametro keyword, vi sia una variabile di istanza con nome e valore uguali alla chiave e al valore
    dell’argomento keyword, rispettivamente.
• le inizializzazioni fatte dal metodo __init__ della classe originaria devono essere preservate e nel caso in cui il metodo
    __init__ della classe originaria aggiunga una variabile di istanza con lo stesso nome delle variabili descritte nei due
    punti precedenti, allora il valore della variabile deve essere quello assegnato dal metodo __init__ della classe originaria.
"""


def decFact(*pos_args, **keyw_args):
    def dec(cls):
        oldInit = cls.__init__

        def __newInit__(self, *args, **kwargs):
            for i in range(len(pos_args)):
                setattr(self, pos_args[i], None)
            for key, value in keyw_args.items():
                setattr(self, key, value)
            oldInit(self, *args, **kwargs)

        cls.__init__ = __newInit__
        return cls

    return dec


@decFact('a', 'b', c='ue')
class MyClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


c = MyClass("a", "b", "ao")
print(c.a)
print(c.b)
print(c.c)
