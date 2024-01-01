class FW:
    """FW memorizza la parte comune dello stato in SharedState"""

    def __init__(self, sharedState: list):
        self._shared_state = sharedState

    """op aggiunge un oggetto al file  prendendo tutta la parte condivisa dell'auto da sharedState e il resto dal
    parametro itsOwnState"""

    def op(self, itsOwnState: list, tipo: type, file):
        s = str(self._shared_state)
        u = str(itsOwnState)
        oggetto = tipo(self._shared_state + itsOwnState)
        of = open(file, "a")
        of.write("FW: Nuova macchina con stato condiviso ({}) e stato unico ({})\n".format(s, u))
        print("Il nuovo oggetto di tipo {} e` {}:".format(tipo, str(oggetto.state())))
        of.close()
        return oggetto


class FWFactory:
    """Questa classe crea oggetti FW: ne crea uno nuovo se non esiste, altrimenti resituisce uno preesistente"""

    _FWDict = {}

    """inizializza il dizionario degli FW: ciascun FW ha all'interno uno degli stati passati con initialFW"""

    def __init__(self, initialFW: dict):
        for state in initialFW:
            self._FWDict[self.get_key(state)] = FW(state)

    def get_key(self, state: list) -> str:
        """restituisce la chiave (stringa) corrispondente ad un certo stato (condiviso)"""
        return "_".join(sorted(state))

    def get_FW(self, shared_state: list) -> FW:
        """restituisce un FW con un certo stato o ne crea uno nuovo"""
        key = self.get_key(shared_state)

        if not self._FWDict.get(key):
            print("FWFactory: non trovo un FW, ne creo uno nuovo.")
            self._FWDict[key] = FW(shared_state)
        else:
            print("FWFactory: uso un FW esistente.")

        return self._FWDict[key]

    def list_FWs(self):
        count = len(self._FWDict)
        print("FWFactory: ho  {} oggetti FW: ".format(count))
        print("\n".join(self._FWDict.keys()), end="")


class car:
    def __init__(self, state: list):
        self._state = state

    def state(self): return self._state


def add(factory: FWFactory, targa: str, proprietario: str, marca: str, modello: str, colore: str):
    """Aggiunge un auto al database prendendo la parte comune (flyweight) da factory se gia` esiste;
    altrimenti aggiunge un nuovo flyweight in factory.
    Il resto delle informazioni dell'auto e` fornito dagli argomenti targa e proprietario."""

    print("\n\nClient: Aggiungo una car.")
    fw = factory.get_FW([marca, modello, colore])
    fw.op([targa, proprietario], car, "cars.txt")


if __name__ == "__main__":
    """creiamo una factory di flyweight popolandola gia` con alcuni flyweight"""

    factory = FWFactory([
        ["Chevrolet", "Camaro2018", "rosa"],
        ["Mercedes Benz", "C300", "nera"],
        ["Mercedes Benz", "C500", "rossa"],
        ["BMW", "M5", "rossa"],
        ["BMW", "X6", "bianca"],
    ])

    factory.list_FWs()

    add(factory, "DE123AT", "Bob Bab", "BMW", "M5", "rossa")
    add(factory, "AR324SD", "Mike Smith", "BMW", "X1", "rossa")
    add(factory, "HJ453FT", "Ada Klein", "BMW", "M5", "rossa")
    add(factory, "JK323OL", "Donald Summerfield", "BMW", "X1", "rossa")
    print("\n")

    factory.list_FWs()

    print("\n")
    fobj = open("cars.txt", 'r')
    for line in fobj:
        print(line)
