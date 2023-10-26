"""
Scrivere nel file esercizio2.py un decoratore di classe decoraClasse che aggiunge alla classe decorata il metodo
conQualiArgomenti che restituisce una tupla contenente:
• i valori di tutti gli argomenti posizionali (compresi quelli variabili)
• le coppie (chiave, valore) di tutti gli argomenti keyword (compresi quelli variabili) passati all’ultima invocazione di __init__
"""
import itertools


def decoraClasse(cls):
    oldInit = cls.__init__

    def __newInit__(self, *args, **kwargs):
        cls.args = args
        cls.kwargs = kwargs
        oldInit(self, *args, **kwargs)

    def conQualiArgomenti():
        args = list(cls.args)
        kwargs = list(cls.kwargs.items())
        return tuple(args + kwargs)

    setattr(cls, "__init__", __newInit__)
    setattr(cls, "conQualiArgomenti", conQualiArgomenti)
    return cls


@decoraClasse
class C:
    def __init__(self, *args, **kwargs):
        for i, x in enumerate(itertools.chain(args, kwargs.values()), start=1):
            setattr(self, "v" + str(i), x)


@decoraClasse
class D:
    def __init__(self, w, y=1000, *args, **kwargs):
        self.v1 = w
        self.v2 = y
        for i, x in enumerate(itertools.chain(args, kwargs.values()), start=3):
            setattr(self, "v" + str(i), x)


def main():
    print("Questa e` un'istanza di C")
    c = C(10, "a", "b", *[9, 11], k1=3, k2=4, **{"k3": "pippo"})
    t = C.conQualiArgomenti()
    print("questa e` la tupla restituita da C.conQualiArgomenti():", t)
    print("questo e` il __dict__ di c:", c.__dict__)

    print("Questa e` un'istanza di D")
    d = D(10, "a", "b", *[9, 11], k1=3, k2="pop", **{"k3": "pippo"})
    t = D.conQualiArgomenti()
    print("questa e` la tupla restituita da D.conQualiArgomenti():", t)
    print("questo e` il __dict__ di d:", d.__dict__)

    print("Questa e` un'altra istanza di C")
    e = C(10, 4, *(9,), **{"k3": "pippo"})
    t = C.conQualiArgomenti()
    print("questa e` la tupla restituita da C.conQualiArgomenti():", t)
    print("questo e` il __dict__ di e:", e.__dict__)

    print("Questa e` un'altra istanza di D")
    f = D(2, k1=3, k2="pop", **{"k3": "pippo"})
    t = D.conQualiArgomenti()
    print("questa e` la tupla restituita da D.conQualiArgomenti():", t)
    print("questo e` il __dict__ di f:", f.__dict__)


"""Il programma deve stampare:
Questa e` un'istanza di C
questa e` la tupla restituita da C.conQualiArgomenti(): (10, 'a', 'b', 9, 11, ('k1', 3), ('k2', 4), ('k3', 'pippo'))
questo e` il __dict__ di c: {'v1': 10, 'v2': 'a', 'v3': 'b', 'v4': 9, 'v5': 11, 'v6': 3, 'v7': 4, 'v8': 'pippo'}
Questa e` un'istanza di D
questa e` la tupla restituita da D.conQualiArgomenti(): (10, 'a', 'b', 9, 11, ('k1', 3), ('k2', 'pop'), ('k3', 'pippo'))
questo e` il __dict__ di d: {'v1': 10, 'v2': 'a', 'v3': 'b', 'v4': 9, 'v5': 11, 'v6': 3, 'v7': 'pop', 'v8': 'pippo'}
Questa e` un'altra istanza di C
questa e` la tupla restituita da C.conQualiArgomenti(): (10, 4, 9, ('k3', 'pippo'))
questo e` il __dict__ di e: {'v1': 10, 'v2': 4, 'v3': 9, 'v4': 'pippo'}
Questa e` un'altra istanza di D
questa e` la tupla restituita da D.conQualiArgomenti(): (2, ('k1', 3), ('k2', 'pop'), ('k3', 'pippo'))
questo e` il __dict__ di f: {'v1': 2, 'v2': 1000, 'v3': 3, 'v4': 'pop', 'v5': 'pippo'}
"""

if __name__ == "__main__":
    main()
