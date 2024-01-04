"""
Si considerino le classi Cane e Persona fornite in mod.py. Scrivere la classe Casa con due cani e una persona (padrona del cane).
La classe Casa fa uso di un mediatore per fare in modo che
a. quando almeno uno dei due cani abbaia allora viene settata a True un flag di allerta (variabile
    self.allerta nella bozza di __init__ fornita).
b. quando il padrone torna a casa, se il flag allerta e` True, verifica per ciascun cane se tra l’ora in cui e`
    tornato a casa e l’ora in cui il cane ha mangiato per l’ultima volta sono trascorse piu` di 4 ore e in
    questo caso da` da mangiare al cane. Se nessuno dei due cani ha abbaiato tra il momento in cui il padrone
    e` uscito e quello in cui ha fatto ritorno (il flag e` False) allora il padrone al suo ritorno non fa niente.

• NB: puo` essere che il cane che abbaia non sia quello che ha fame o che ne abbai uno solo ma che
    entrambi abbiano fame, o ancora che almeno uno dei cani abbia ma nessuno dei due abbia fame.
• Suggerimento. Per ciascuno dei due punti creare un callable: uno dei due deve essere associato ad entrambi
    i cani e l’altro deve essere associato al padrone. La differenza in ore tra due orari ora1 e ora2 si
    calcola cosi` : (ora1-ora2).total_seconds()/60/60 .
"""
import datetime
from mod import Cane, Persona, Mediator


class Casa:

    def __init__(self, nomePadrone, nomeCane1, nomeCane2, oraUltimaPappa1, oraUltimaPappa2):
        self.mediator = None
        self.allerta = False
        self.padrone = Persona(nomePadrone)
        self.cane1 = Cane(nomeCane1, oraUltimaPappa1)
        self.cane2 = Cane(nomeCane2, oraUltimaPappa2)
        self.create_mediator()

    def create_mediator(self):
        self.mediator = Mediator(
            ((self.padrone, self.updatePadrone), (self.cane1, self.updateCane), (self.cane2, self.updateCane)))

    def updateCane(self, cane=None):
        print(f"Il cane {cane.nome} abbaia")
        if self.padrone.ora_ritorno == -1:
            self.allerta = True

    def updatePadrone(self, padrone=None):
        if self.allerta:
            if (self.padrone.ora_ritorno - self.cane1.oraUltimaPappa).total_seconds() / 60 / 60 > 4:
                print(f"Il padrone da` la pappa al cane {self.cane1.nome}")
                self.cane1.oraUltimaPappa = self.padrone.ora_ritorno
            if (self.padrone.ora_ritorno - self.cane2.oraUltimaPappa).total_seconds() / 60 / 60 > 4:
                print(f"Il padrone da` la pappa al cane {self.cane2.nome}")
                self.cane2.oraUltimaPappa = self.padrone.ora_ritorno
        self.allerta = False


def main():
    casa = Casa("Maria", "Bob", "Ted", datetime.datetime(year=2020, month=1, day=11, hour=10),
                datetime.datetime(year=2020, month=1, day=11, hour=11))
    print("Il cane {} ha mangiato alle {} per l'ultima volta".format(casa.cane1.nome,
                                                                     (casa.cane1.oraUltimaPappa.strftime('%H:%M'))))
    print("Il cane {} ha mangiato alle {} per l'ultima volta".format(casa.cane2.nome,
                                                                     (casa.cane2.oraUltimaPappa.strftime('%H:%M'))))

    casa.padrone.esce()
    casa.cane1.abbaia()
    casa.padrone.torna_a_casa(datetime.datetime(year=2020, month=1, day=11, hour=15))
    casa.padrone.esce()
    casa.cane2.abbaia()
    casa.padrone.torna_a_casa(datetime.datetime(year=2020, month=1, day=11, hour=17))
    casa.padrone.esce()
    casa.padrone.torna_a_casa(datetime.datetime(year=2020, month=1, day=11, hour=18))
    casa.padrone.esce()
    casa.cane1.abbaia()
    casa.padrone.torna_a_casa(datetime.datetime(year=2020, month=1, day=11, hour=23))


if __name__ == "__main__": main()

"""
Il programma deve stampare:
Il cane Bob ha mangiato alle 10:00 per l'ultima volta
Il cane Ted ha mangiato alle 11:00 per l'ultima volta
Il padrone dei cani esce di casa
Il cane Bob abbaia
Il padrone dei cani torna a casa alle 15:00
Il padrone da` la pappa al cane  Bob
Il padrone dei cani esce di casa
Il cane Ted abbaia
Il padrone dei cani torna a casa alle 17:00
Il padrone da` la pappa al cane  Ted
Il padrone dei cani esce di casa
Il padrone dei cani torna a casa alle 18:00
Il padrone dei cani esce di casa
Il cane Bob abbaia
Il padrone dei cani torna a casa alle 23:00
Il padrone da` la pappa al cane  Bob
Il padrone da` la pappa al cane  Ted


"""
