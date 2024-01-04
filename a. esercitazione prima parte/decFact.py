"""
Scrivere un decorator factory decFact che prende in input un tipo e restituisce un decoratore che dota la
classe decorata di un metodo statico riportaVariabiliDiClasse che non prende in input alcun argomento.
II metodo riporta VariabiliDiClasse restituisce un generatore di triple. Ciascuna tripla contiene come primo elemento
il nome di una variabile di classe, come secondo elemento il valore della suddetta variabile, e come terzo elemento
la classe in cui viene trovata la variabile (potrebbe essere C o una delle sue superclassi).
"""


def decFact(tipo):
    def decoratore(cls):
        @staticmethod
        def riportaVariabiliDiClasse():
            s = set()
            for cl in cls.__mro__:
                for e in cl.__dict__:
                    if e not in s:
                        s.add(e)
                        if isinstance(getattr(cl, e), tipo):
                            yield e, getattr(cl, e), cl

        setattr(cls, "riportaVariabiliDiClasse", riportaVariabiliDiClasse)
        return cls

    return decoratore


@decFact(int)
class A:
    a = 10


@decFact(int)
class B(A):
    b = 20


a = A()
b = B()
for nome, valore, classe in a.riportaVariabiliDiClasse():
    print(f"Nome: {nome}, Valore: {valore}, Classe: {classe.__name__}")
for nome, valore, classe in b.riportaVariabiliDiClasse():
    print(f"Nome: {nome}, Valore: {valore}, Classe: {classe.__name__}")
