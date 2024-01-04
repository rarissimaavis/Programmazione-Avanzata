"""
Immaginiamo che un bambino venga iscritto alla scuola media. Il bambino puo` essere in uno dei seguenti stati:
a. iscritto: il bimbo e` inizialmente iscritto al primo anno
b. alSecondoAnno: il bimbo e` promosso al secondo anno
c. alTerzoAnno: il bimbo e` promosso al terzo anno
d. diplomato: al termine del terzo, il bimbo consegue il diploma di scuola media.
La classe Bambino ha il metodo succ per passare allo stato successivo, il metodo pred per passare a quello precedente
(retrocesso in caso di debiti formativi non recuperati) e il metodo salta_anno per saltare un anno (da iscritto si salta
al terzo anno e dal secondo anno al diploma).
Lo stato iscritto non ha stati che lo precedono; lo stato diplomato non ha stati che vengono dopo di esso.
La classe Bambino ha anche un metodo stampaStato per stampare lo stato del bambino.
Scrivere la classe Bambino usando un approccio state-specific in cui lo stato del bambino e` una proprieta`.
Non usare altre classi oltre la classe Bambino.
"""


class Bambino:
    ISCRITTO, ALSECONDOANNO, ALTERZOANNO, DIPLOMATO = ("iscritto", "alSecondoAnno", "alTerzoAnno", "diplomato")

    def __init__(self):
        self.state = Bambino.ISCRITTO

    @property
    def state(self):
        # se la versione pubblica è uguale alla versione privata allora il metodo esiste, altrimenti c'è una lambda
        if self.succ != self._succ: return Bambino.DIPLOMATO
        if self.pred != self._pred: return Bambino.ISCRITTO
        if self.succ == self._succ and self._salta_anno != self._salta_anno: return Bambino.ALTERZOANNO
        if self.succ != self._succ: return Bambino.DIPLOMATO

    @statoBimbo.setter
    def state(self, state):
        if state == Bambino.ISCRITTO:
            self.pred = self._pred
            self.succ = self._succ
            self.salta_anno = self._salta_anno
        elif state == Bambino.ALSECONDOANNO:
            self.pred =
            self.succ = self._succ
            self.salta_anno = self._salta_anno
        elif state == Bambino.ALTERZOANNO:
            self.pred = self._pred
            self.succ = self._succ
            self.salta_anno = self.__alterzoanno_salta_anno
        elif state == Bambino.DIPLOMATO:
            self.pred = self._pred
            self.succ = self._succ
            self.salta_anno = self.__diplomato_salta_anno


    def _succ(self):
        self.statoBimbo = self.statoBimbo+1

    def _pred(self):
        self.statoBimbo = self.statoBimbo-1

    def _salta_anno(self):
        self.statoBimbo = self.statoBimbo+1



def main():
    bambino = Bambino()
    bambino.stampaStato()
    bambino.pred()
    bambino.succ()
    bambino.stampaStato()
    bambino.succ()
    bambino.stampaStato()
    bambino.salta_anno()
    bambino.succ()
    bambino.stampaStato()
    bambino.succ()


if __name__ == "__main__":
    main()

"""IL programma deve stampare:

Il bambino e` nello stato  iscritto
Il bambino  e` appena stato iscritto al I anno e non puo` tornare in uno stato precedente
Il bambino e` nello stato  alSecondoAnno
Il bambino e` nello stato  alTerzoAnno
Il bambino e` nello stato alTerzoAnno  e non puo` saltare un anno
Il bambino e` nello stato  diplomato
Il bambino  si e` gia` diplomato e non puo` avanzare in uno stato successivo
"""
