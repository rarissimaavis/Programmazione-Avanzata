"""
Avete a disposizione la classe Adapter e le classi Lavoratore, Commesso, Cuoco, Musicista.
La classe Lavoratore e` stata implementata da voi mentre le restanti sono in una libreria esterna il cui
codice sorgente non puo` essere modificato.
Scrivere un programma che stampa le seguenti stringhe utilizzando solo i metodi di Adapter e Lavoratore:
• Il commesso Paolo vende abiti
• Il musicista Veronica suona musica pop
• Il cuoco Antonio cucina una lasagna
"""


class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


class Lavoratore:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "Il lavoratore {}".format(self.nome)

    def lavora(self, lavoro):
        return "svolte il seguente {}".format(lavoro)


class Commesso:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "Il commesso {}".format(self.nome)

    def vende(self, merce):
        return "vende {}".format(merce)


class Cuoco:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "Il cuoco {}".format(self.nome)

    def cucina(self, pietanza):
        return "cucina {}".format(pietanza)


class Musicista:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "Il musicista {}".format(self.nome)

    def suona(self, tipoMusica):
        return "suona {}".format(tipoMusica)


c = Commesso("Paolo")
cStr = Adapter(c, {"__str__": c.__str__})
cLav = Adapter(c, {"lavora": c.vende})
print(cStr.__str__() + " " + cLav.lavora("abiti"))

m = Musicista("Veronica")
mStr = Adapter(m, {"__str__": m.__str__})
mLav = Adapter(m, {"lavora": m.suona})
print(mStr.__str__() + " " + mLav.lavora("musica pop"))

cu = Cuoco("Antonio")
cuStr = Adapter(cu, {"__str__": cu.__str__})
cuLav = Adapter(cu, {"lavora": cu.cucina})
print(cuStr.__str__() + " " + cuLav.lavora("una lasagna"))
