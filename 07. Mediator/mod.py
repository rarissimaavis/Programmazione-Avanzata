import collections


class Mediated:
    def __init__(self):
        self.mediator = None

    def on_change(self):
        if self.mediator is not None:
            self.mediator.on_change(self)


class Cane(Mediated):
    def __init__(self, nome, ora):
        super().__init__()
        self.nome = nome
        # ora in cui il cane ha mangiato per l'ultima volta
        self.oraUltimaPappa = ora

    def abbaia(self):
        self.on_change()


class Persona(Mediated):

    def __init__(self, nome):
        super().__init__()
        self.nome = nome
        # ora_ritorno e` settata a -1 quando la persona e` fuori casa
        self.ora_ritorno = 0

    def torna_a_casa(self, ora):
        print("Il padrone dei cani torna a casa alle", ora.strftime('%H:%M'))
        self.ora_ritorno = ora
        self.on_change()

    def esce(self):
        print("Il padrone dei cani esce di casa")
        self.ora_ritorno = -1


class Mediator:
    def __init__(self, memberCallablePairs):
        self.callablesForMember = collections.defaultdict(list)
        for membro, caller in memberCallablePairs:
            self.callablesForMember[membro].append(caller)
            membro.mediator = self

    # member puo` essere una persona o un cane
    def on_change(self, member):
        callables = self.callablesForMember.get(member)
        if callables is not None:
            for caller in callables:
                caller(member)
        else:
            raise AttributeError("Nessun metodo registrato per {}".format(member))
