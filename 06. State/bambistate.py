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
        return self.state

    @state.setter
    def state(self, state):
        if state == Bambino.ISCRITTO:
            self.pred = self.__iscritto_pred
            self.succ = self.__iscritto_succ
            self.salta_anno = self.__iscritto_salta_anno
            self.stampaStato = self.__iscritto_stampaStato
        elif state == Bambino.ALSECONDOANNO:
            self.pred = self.__alsecondoanno_pred
            self.succ = self.__alsecondoanno_succ
            self.salta_anno = self.__alsecondoanno_salta_anno
            self.stampaStato = self.__alsecondoanno_stampaStato
        elif state == Bambino.ALTERZOANNO:
            self.pred = self.__alterzoanno_pred
            self.succ = self.__alterzoanno_succ
            self.salta_anno = self.__alterzoanno_salta_anno
            self.stampaStato = self.__alterzoanno_stampaStato
        elif state == Bambino.DIPLOMATO:
            self.pred = self.__diplomato_pred
            self.succ = self.__diplomato_succ
            self.salta_anno = self.__diplomato_salta_anno
            self.stampaStato = self.__diplomato_stampaStato

    def __iscritto_pred(self):
        print(f"Il bambino  e` appena stato {Bambino.ISCRITTO} al I anno e non puo` tornare in uno stato precedente")

    def __iscritto_succ(self):
        self.state = Bambino.ALSECONDOANNO

    def __iscritto_salta_anno(self):
        self.state = Bambino.ALTERZOANNO

    def __iscritto_stampaStato(self):
        print("Il bambino e` nello stato", Bambino.ISCRITTO)

    def __alsecondoanno_pred(self):
        self.state = Bambino.ISCRITTO

    def __alsecondoanno_succ(self):
        self.state = Bambino.ALTERZOANNO

    def __alsecondoanno_salta_anno(self):
        self.state = Bambino.DIPLOMATO

    def __alsecondoanno_stampaStato(self):
        print("Il bambino e` nello stato", Bambino.ALSECONDOANNO)

    def __alterzoanno_pred(self):
        self.state = Bambino.ALSECONDOANNO

    def __alterzoanno_succ(self):
        self.state = Bambino.DIPLOMATO

    def __alterzoanno_salta_anno(self):
        print(f"Il bambino e` nello stato {Bambino.ALTERZOANNO}  e non puo` saltare un anno")

    def __alterzoanno_stampaStato(self):
        print("Il bambino e` nello stato", Bambino.ALTERZOANNO)

    def __diplomato_pred(self):
        self.state = Bambino.ALTERZOANNO

    def __diplomato_succ(self):
        print(f"Il bambino  si e` gia` {Bambino.DIPLOMATO} e non puo` avanzare in uno stato successivo")

    def __diplomato_salta_anno(self):
        print(f"Il bambino  si e` gia` {Bambino.DIPLOMATO} e non puo` saltare un anno")

    def __diplomato_stampaStato(self):
        print("Il bambino e` nello stato", Bambino.DIPLOMATO)


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
