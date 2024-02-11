"""
Si consideri il modulo moduloVeicoli.py fornito dalla docente. Le classi presenti nel file moduloVeicoli.py
hanno dei metodi che quando invocati richiedono che venga svolta una certa azione.
Questi metodi invocano il metodo azione() della classe Manovratore sulla variabile di
istanza manovratore perche` venga svolta l’azione richiesta.
Scrivere nel file esercizio.py la classe Manovratore e la classe Strada che usa un oggetto
Manovratore per fare in modo che:
i. quando l’auto è a riserva, venga fatto rifornimento, cioe` spia_benzina venga
  settata a false ed effettuata la stampa di “L’auto {} sta facendo benzina”
ii. quando un autobus effettua una fermata, deve essere aggiornata ora_ultima_fermata con l’ora corrente
  ed effettuata la stampa di “L’autobus {} sta effettuando una fermata alle ore {}”.
I valori delle variabili il cui nome inizia con ‘_’ non possono essere letti o modificati direttamente.
I metodi per aggiornare queste variabili sono forniti nelle classi.
Il metodo aziona() NON deve contenere statement condizionali.
Il metodo __init__ della classe Strada prende in input due tuple: la prima contiene i nomi id_veicolo delle auto
e la seconda contiene le tuple (id_veicolo, tratta), deve tratta è una tupla di due stringhe.
Strada deve fornire il metodo di istanza getVeicolo(id_veicolo) che prende in input il nome
del veicolo e restituisce il veicolo con quel nome.
La versione “base” dell’esercizio prevede che nella strada ci siano due auto e due autobus.
La versione con bonus prevede che Strada funzioni per un numero arbitrario di auto e autobus.
La versione con superbonus prevede che la versione con bonus funzioni in modo che, oltre a
quanto gia` specificato da I e II, se un autobus arriva al capolinea, venga effettuata la stampa di “L’autobus {} è
arrivato al capolinea: ora il suo tragitto è {}.” e venga modificato il tragitto con quello in direzione opposta.
Non usate un unico metodo per gestire sia la fermata che l’arrivo al capolinea.
"""
import collections
import inspect
from moduloVeicoli import Autobus, Auto


class Manovratore:
    def __init__(self, memberCallablePairs):
        self.callablesForMember = collections.defaultdict(list)
        for membro, caller in memberCallablePairs:
            self.callablesForMember[membro].append(caller)
            membro.manovratore = self

    def aziona(self, member):
        callables = self.callablesForMember.get(member)
        if callables is not None:
            for caller in callables:
                caller(member)
        else:
            raise AttributeError(f"Nessun metodo registrato per {member}")


class Strada:
    def __init__(self, nomi_auto, info_autobus):
        self.dictVeicoli = {}
        self.automobili = []
        self.autobus = []
        for i in range(len(nomi_auto)):
            auto = Auto(nomi_auto[i])
            self.automobili.insert(i, auto)
            self.dictVeicoli[nomi_auto[i]] = auto
        for i in range(len(info_autobus)):
            autobus = Autobus(info_autobus[i][0], info_autobus[i][1])
            self.dictVeicoli[info_autobus[i][0]] = autobus
            self.autobus.insert(i, autobus)
        self.crea_manovratore()

    def getVeicolo(self, name):
        return self.dictVeicoli.get(name)

    def crea_manovratore(self):
        listaCallables = [(veicolo, self.fai_benzina) if type(veicolo) == Auto else (veicolo, self.effettua_fermata) for
                          veicolo in self.dictVeicoli.values()]
        listaCallables += [(veicolo, self.arrivo_capolinea) for veicolo in self.dictVeicoli.values() if
                           type(veicolo) == Autobus]
        self.manovratore = Manovratore(listaCallables)

    def fai_benzina(self, auto):
        print(f"L'auto {auto.id_veicolo} sta facendo benzina")
        auto.reset_spia()

    def effettua_fermata(self, autobus):
        st = inspect.stack()
        framecaller = st[2]
        caller = framecaller[3]
        if caller == "arrivaAllaFermata":
            ora = autobus.aggiorna_ora_ultima_fermata()
            print(f"L'autobus {autobus.id_veicolo} sta effettuando una fermata alle ore {ora.strftime('%H:%M:%S')}")

    def arrivo_capolinea(self, autobus):
        st = inspect.stack()
        framecaller = st[2]
        caller = framecaller[3]
        if caller == "arrivaAlCapolinea":
            print(
                f"L'autobus {autobus.id_veicolo} è arrivato al capolinea: ora il suo tragitto è {autobus.aggiorna_direzione()}")


def main():
    print("Test con 2 auto e 2 autobus:")
    automobiliID = ("AB123CD", "AF234EF")
    autobusInfo = (("11", ("via Roma", "via Poseidonia")), ("21", ("via Canalone", "via Vinciprova")))
    strada = Strada(automobiliID, autobusInfo)
    auto1 = strada.getVeicolo("AB123CD")
    auto2 = strada.getVeicolo("AF234EF")
    bus1 = strada.getVeicolo("11")
    bus2 = strada.getVeicolo("21")

    auto1.sonoARiserva()
    auto2.sonoARiserva()
    bus1.arrivaAllaFermata()
    bus1.arrivaAllaFermata()
    bus1.arrivaAlCapolinea()
    bus2.arrivaAllaFermata()
    bus2.arrivaAllaFermata()
    bus2.arrivaAlCapolinea()

    print("\nOra usiamo un numero diverso di veicoli")
    automobiliID = ("AB123CD", "AF234EF", "BG345KL")
    autobusInfo = (("11", ("via Roma", "via Poseidonia")), ("21", ("via Canalone", "via Vinciprova")),
                   ("10", ("piazza delle Concordia", "via Ligea")),
                   ("1", ("piazza Malta", "Vietri sul Mare")))
    strada = Strada(automobiliID, autobusInfo)
    auto1 = strada.getVeicolo("AB123CD")
    auto2 = strada.getVeicolo("AF234EF")
    auto3 = strada.getVeicolo("BG345KL")
    bus1 = strada.getVeicolo("11")
    bus2 = strada.getVeicolo("21")
    bus3 = strada.getVeicolo("10")
    bus4 = strada.getVeicolo("1")

    auto3.sonoARiserva()
    auto1.sonoARiserva()
    auto2.sonoARiserva()
    bus4.arrivaAllaFermata()
    bus3.arrivaAllaFermata()
    bus2.arrivaAllaFermata()
    bus1.arrivaAllaFermata()
    bus1.arrivaAlCapolinea()
    bus1.arrivaAllaFermata()
    bus2.arrivaAllaFermata()
    bus2.arrivaAlCapolinea()
    bus2.arrivaAlCapolinea()
    bus3.arrivaAllaFermata()
    bus4.arrivaAlCapolinea()
    bus2.arrivaAllaFermata()
    bus2.arrivaAllaFermata()
    bus3.arrivaAlCapolinea()
    bus3.arrivaAllaFermata()
    bus4.arrivaAlCapolinea()
    bus2.arrivaAllaFermata()
    bus2.arrivaAllaFermata()
    bus3.arrivaAlCapolinea()


if __name__ == "__main__":
    main()

"""
Il programma con superbonus deve stampare  (gli orari ovviamente sono diversi)::
Test con 2 auto e 2 autobus:
L’auto AB123CD sta facendo benzina
L’auto AF234EF sta facendo benzina
L’autobus 11 sta effettuando una fermata alle ore 19:39:44
L’autobus 11 sta effettuando una fermata alle ore 19:39:44
L’autobus 11 è arrivato al capolinea: ora il suo tragitto e` ('via Poseidonia', 'via Roma')
L’autobus 21 sta effettuando una fermata alle ore 19:39:44
L’autobus 21 sta effettuando una fermata alle ore 19:39:44
L’autobus 21 è arrivato al capolinea: ora il suo tragitto e` ('via Vinciprova', 'via Canalone')

Ora usiamo un numero diverso di veicoli
L’auto BG345KL sta facendo benzina
L’auto AB123CD sta facendo benzina
L’auto AF234EF sta facendo benzina
L’autobus 1 sta effettuando una fermata alle ore 19:39:44
L’autobus 10 sta effettuando una fermata alle ore 19:39:44
L’autobus 21 sta effettuando una fermata alle ore 19:39:44
L’autobus 11 sta effettuando una fermata alle ore 19:39:44
L’autobus 11 è arrivato al capolinea: ora il suo tragitto e` ('via Poseidonia', 'via Roma')
L’autobus 11 sta effettuando una fermata alle ore 19:39:44
L’autobus 21 sta effettuando una fermata alle ore 19:39:44
L’autobus 21 è arrivato al capolinea: ora il suo tragitto e` ('via Vinciprova', 'via Canalone')
L’autobus 21 è arrivato al capolinea: ora il suo tragitto e` ('via Canalone', 'via Vinciprova')
L’autobus 10 sta effettuando una fermata alle ore 19:39:44
L’autobus 1 è arrivato al capolinea: ora il suo tragitto e` ('Vietri sul Mare', 'piazza Malta')
L’autobus 21 sta effettuando una fermata alle ore 19:39:44
L’autobus 21 sta effettuando una fermata alle ore 19:39:44
L’autobus 10 è arrivato al capolinea: ora il suo tragitto e` ('via Ligea', 'piazza delle Concordia')
L’autobus 10 sta effettuando una fermata alle ore 19:39:44
L’autobus 1 è arrivato al capolinea: ora il suo tragitto e` ('piazza Malta', 'Vietri sul Mare')
L’autobus 21 sta effettuando una fermata alle ore 19:39:44
L’autobus 21 sta effettuando una fermata alle ore 19:39:44
L’autobus 10 è arrivato al capolinea: ora il suo tragitto e` ('piazza delle Concordia', 'via Ligea')
"""
