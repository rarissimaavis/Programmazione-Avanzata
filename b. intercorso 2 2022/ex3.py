"""
Scrivere un programma in cui vi e` una classe libro che puo` essere osservata da un numero arbitrario di osservatori
e che oltre all’attributo titolo ha i seguenti attributi che ne determinano lo stato:
a) riferimenti: dizionario dei riferimenti presenti al suo interno. Un riferimento e` un testo citato dal libro.
  Riferimenti e` quindi un dizionario di coppie (chiave, valore) dove chiave e` un intero e valore e` un libro.
b) numero_copie: un intero che rappresenta il numero di copie vendute
c) alta_progressione: flag che viene settato a True se e solo se il numero di copie aumenta almeno del doppio rispetto
  al valore precedente ed e` settato a False se il numero di copie aumenta meno della meta` del valore precedente.
Se numero_copie viene aggiornato in modo diverso da quelli indicati, il flag non viene settato. Ogni volta che questo
flag viene settato viene fatta la notifica agli osservatori anche se il nuovo valore del flag e` uguale a quello vecchio.
Gli attributi numero_copie e alta_progressione sono accessibili con il loro nome e modificabili con ‘=‘.
Il dizionario riferimenti viene creato e riempito dal metodo __init__ di Libro. Il metodo __init__ riceve in input il
titolo del libro e la lista dei libri da inserire nel dizionario riferimenti.
L’i-esimo libro della lista avra` chiave i nel dizionario.
Attenzione: le entrate del dizionario riferimenti non devono essere modificabili con ‘=’.
Se, ad esempio, si usa l’istruzione riferimento[k]=libro allora viene lanciata l’eccezione RuntimeError.

Scrivere inoltre gli osservatori VistaIst e VistaStorica.
VistaIst deve stampare
• "Cambio stato: nuove vendite del libro \"{}\" per un totale di copie vendite pari a {} \n"
  se il cambio stato e` dovuto ad un aggiornamento di numero_copie.
• "Cambio stato: con l'ultimo acquisto, il libro \"{}\" ha piu` che raddoppiato le vendite\n" se il cambio stato e` dovuto
  al fatto che le vendite sono raddoppiate, cioe` al fatto che alta_progressione e` stato settato a True (anche se era gia` True)
• "Cambio stato: con l'ultimo acquisto, le vendite di \"{}\" sono aumentate meno della meta`\n” se il cambio stato e`
  dovuto al fatto che le vendite sono aumentate meno della meta`, cioe` al fatto che alta_progressione e` stato
  settato a False (anche se era gia` False).
VistaStorica crea due liste storia_vendite e andamento_vendite:
• storia_vendite e` una lista di triple della forma [titolo,numerocopie,tempo] . Ogni volta che viene aggiornato l’attributo
  numero_copie di uno dei libri osservati, viene aggiunta una tripla della forma [titolo, numerocopie, tempo] a storia_vendite,
  dove titolo e` il titolo del libro il cui numero di copie e` cambiato, numerocopie e` il nuovo numero totale di copie
  vendute del libro e tempo e` il tempo in cui avviene l’aggiornamento.
• andamento_vendite e` una lista di coppie della forma [stringa, tempo]. Ogni volta che viene settato alta_progressione
  viene inserita una coppia [stringa, tempo] in andamento_vendite, dove tempo e` il tempo in cui avviene l’aggiornamento
  e stringa e` "Raddoppio vendite di \"{}\"" se alta_progressione e` settato a True (anche se era gia` True) oppure e`
  "Incremento delle vendite di \"{}\" inferiore ad un mezzo del valore precedente" se alta_progressione e` settato a False (anche se era gia` False).
VistaStorica ha anche il metodo storia() che restituisce una lista il cui primo elemento e` la lista
storia_vendite e il cui secondo elemento e` la lista andamento_vendite.
Nelle suddette stampe al posto delle parentesi graffe devono comparire il nome del libro e/o il numero di copie, a seconda dei casi.
"""
import copy
import itertools
from datetime import time


class Observed:
    def __init__(self):
        self.__observers = set()

    def observers_add(self, observer, *observers):
        for observer in itertools.chain((observer,), observers):
            self.__observers.add(observer)
            observer.update((self, None))

    def observer_discard(self, observer):
        self.__observers.discard(observer)

    def observers_notify(self, event):
        for observer in self.__observers:
            observer.update((self, event))


class Libro(Observed):
    class MyDict(dict):
        oldsetitem = dict.__setitem__

        def __setitem__(self, key, value):
            raise RuntimeError("Operazione vietata")

    def __init__(self, titolo, riferimenti=None):
        super().__init__()
        self.titolo = titolo
        self.riferimenti = Libro.MyDict()
        for key, value in enumerate(riferimenti):
            self.riferimenti.oldsetitem(key, value)
        self.__alta_progressione = False
        self.__numero_copie = 0

    @property
    def alta_progressione(self):
        return self.__alta_progressione

    @alta_progressione.setter
    def alta_progressione(self, bests):
        if self.__alta_progressione != bests:
            self.__alta_progressione = bests
        self.observers_notify(["best seller", self])

    @property
    def numero_copie(self):
        return self.__numero_copie

    @numero_copie.setter
    def numero_copie(self, ncopie):
        if ncopie != self.__numero_copie:
            old = self.__numero_copie
            self.__numero_copie = ncopie
            self.observers_notify(["numero copie", self])
            if ncopie - old > old:
                self.alta_progressione = True
            if old > 2 * (ncopie - old):
                self.alta_progressione = False


class VistaIst:
    def update(self, ob):
        if ob is None:
            pass
        elif ob[0] == "numero copie":
            print(
                f"Cambio stato: nuove vendite del libro \"{ob[1].titolo}\" per un totale di copie vendute pari a {ob[1].numero_copie}\n")
        elif ob[0] == "best seller":
            if ob[1].alta_progressione:
                print(
                    f"Cambio stato: con l'ultimo acquisto, il libro \"{ob[1].titolo}\" ha piu` che raddoppiato le vendite\n")
            else:
                print(
                    f"Cambio stato: con l'ultimo acquisto, le vendite di \"{ob[1].titolo}\" sono aumentate meno della meta`\n")


class VistaStorica:
    def __init__(self):
        self.storia_vendite = []
        self.andamento_vendite = []

    def update(self, ob):
        if ob is None:
            pass
        elif ob[0] == "best seller":
            self.storia_vendite.append((copy.copy(ob[1].titolo), ob[1].numero_copie, time.time()))
        elif ob[0] == "numero copie":
            if ob[1].alta_progressione:
                print(f"Raddoppio vendite di \"{ob[1].titolo}\"")
            else:
                print(f"Incremento delle vendite di \"{ob[1].titolo}\" inferiore ad un mezzo del valore precedente")

    def storia(self):
        return [self.storia_vendite, self.andamento_vendite]

