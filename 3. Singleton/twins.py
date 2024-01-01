"""Scrivere all'interno della classe Top, due classi Twin1 e Twin2 nessuna della quali è derivata dall'altra.
Le istanze di ciascuna classe devono essere tra di loro identiche e anche identiche alle istanze dell'altra classe
(identiche vuol dire stessi attributi)
Scrivere poi la classe Der1 le cui istanze non condividono lo stesso stato delle istanze delle due classi base.
"""


class Top:
    _shared = {}

    class Twin1:
        def __new__(cls, *args, **kwargs):
            o = super(Top.Twin1, cls).__new__(cls, *args, **kwargs)
            o.__dict__ = Top._shared
            return o

    class Twin2:
        def __new__(cls, *args, **kwargs):
            o = super(Top.Twin2, cls).__new__(cls, *args, **kwargs)
            o.__dict__ = Top._shared
            return o


class Der1(Top.Twin1):
    _shared = {}

    def __new__(cls, *args, **kwargs):
        o = super(Top.Twin1, Top.Twin1).__new__(cls, *args, **kwargs)
        o.__dict__ = Der1._shared
        return o
