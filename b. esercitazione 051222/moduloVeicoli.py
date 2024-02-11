import collections
import datetime
import inspect


class Veicolo:
    def __init__(self, id_veicolo):
        self.manovratore = None
        self.id_veicolo = id_veicolo


# Le variabili con '_' davanti non devono essere "lette" o modificate direttamente.
class Auto(Veicolo):
    def __init__(self, id_auto):
        super().__init__(id_auto)
        self._spia_benzina = True

    # metodi di modifica dell' attributo "privato " _spia_benzina
    def reset_spia(self):
        self._spia_benzina = False

    # metodo invocato nel main
    def sonoARiserva(self):
        if self.manovratore is not None:
            self.manovratore.aziona(self)


# Le variabili con '_' davanti non devono essere "lette" o modificate direttamente.
class Autobus(Veicolo):
    def __init__(self, id_autobus, tragitto):
        super().__init__(id_autobus)
        self._ora_ultima_fermata = datetime.time(0, 0)
        self._tragitto = tragitto

    # metodi invocati dal main
    def arrivaAllaFermata(self):
        if self.manovratore is not None:
            self.manovratore.aziona(self)

    def arrivaAlCapolinea(self):
        if self.manovratore is not None:
            self.manovratore.aziona(self)

    # metodi di modifica degli attributi "privati"
    def aggiorna_direzione(self):
        self._tragitto = (self._tragitto[1], self._tragitto[0])
        return self._tragitto

    def aggiorna_ora_ultima_fermata(self):
        self._ora_ultima_fermata = datetime.datetime.now().time()
        return self._ora_ultima_fermata
