"""
Scrivere una classe di base ClsBase in cui c’e` un metodo addAttr che
• prende in input due argomenti: una stringa s e un valore v,
• controlla se la classe ha l’attributo di nome s e se tale attributo non e` presente allora aggiunge alla classe
    l’attributo s con valore v; in caso contrario non fa niente.
Il metodo deve funzionare anche per le eventuali sottoclassi di ClsBase
"""


class ClsBase:
    @classmethod
    def addAttr(cls, s, v):
        if not hasattr(cls, s):
            setattr(cls, s, v)


class ClsDer(ClsBase):
    pass


ClsBase.addAttr("ue", 3)
print(ClsBase.ue)
ClsBase.addAttr("ue", 5)
print(ClsBase.ue)
ClsDer.addAttr("ao", 2)
print(ClsDer.ao)

