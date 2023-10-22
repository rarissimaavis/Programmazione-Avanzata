"""
Scrivere una classe C con all’interno due classi TaleEQuale1 e TaleEQuale2.
Le istanze di ognuna delle due classi devono essere tra di loro identiche e anche identiche alle istanze
dell’altra classe (identiche vuol dire che hanno gli stessi attributi).

Scrivere poi la classe Diversa che ha come classi base TaleEQuale1 e TaleEQuale2. Le istanze di Diversa
sono tra di loro identiche ma non condividono lo stesso stato delle istanze delle due classi base.
"""


class C:
    _shared = {}

    class TaleEQuale1:
        def __new__(cls, *args, **kwargs):
            obj = super().__new__(cls, *args, **kwargs)
            obj.__dict__ = C._shared
            return obj

    class TaleEQuale2:
        def __new__(cls, *args, **kwargs):
            obj = super().__new__(cls, *args, **kwargs)
            obj.__dict__ = C._shared
            return obj

    class Diversa(TaleEQuale1, TaleEQuale2):
        _shared = {}

        def __new__(cls, *args, **kwargs):
            obj = super().__new__(cls, *args, **kwargs)
            obj.__dict__ = C._shared
            return obj


c = C.TaleEQuale1()
c.a = 5
d = C.TaleEQuale2()
print(d.a)
