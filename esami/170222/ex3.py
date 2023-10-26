"""
Scriva nel file esercizio3.py una classe ProteggiClasse che funga come proxy della classe ClDaProteggere.
La classe ProteggiClasse deve fare in modo che possano essere usati solo i metodi leggi, scriviA, scriviZ di ClDaProteggere.
Se viene invocato uno degli altri metodi deve essere lanciata AttributeError con la stringa “Il metodo non puo` essere invocato”.
Oltre ad __init__ deve essere implementato un unico altro metodo all’interno di ProteggiClasse. Non usi l’ereditarieta`.
"""


class ProteggiClasse:
    def __init__(self):
        self.__implementation = ClDaProteggere()

    def __getattr__(self, name):
        if name in ("leggi", "scriviA", "scriviZ"):
            return getattr(self.__implementation, name)
        else:
            raise AttributeError("Il metodo non puo` essere invocato")


class ClDaProteggere:
    def __init__(self):
        pass

    def leggi(self):
        print("leggi")

    def scriviA(self):
        print("scriviA")

    def scriviZ(self):
        print("scriviZ")

    def ao(self):
        print("ao")


c = ProteggiClasse()
c.leggi()
c.scriviA()
c.scriviZ()
c.ciao()
