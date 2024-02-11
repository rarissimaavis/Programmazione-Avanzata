"""
Scrivere una classe Prodotto che, oltre al nome, ha i seguenti attributi che ne determinano lo stato:
• quantita: quantita` presente nel magazzino di un grossista (inizialmente e` 0)
• stato_scorte che puo` avere tre valori: "altamente disponibile, "disponibile", "non disponibile" (inizialmente e` “non disponibile”).
• _acquirenti: dizionario dei negozi che hanno acquistato almeno una volta il prodotto. Le entrate hanno come chiave
  il nome dell’acquirente e come valore una tupla di due elementi (numero, data) dove numero e` la quantita` di prodotto
  acquistato dall’acquirente con il suo ultimo acquisto e data e` la data in cui e` avvenuto quest’ultimo acquisto.
La classe ha anche due metodi vendi, immagazzina ed elimina_scorte forniti per vostra convenienza dalla docente.
La classe deve anche fornire la versione pubblica vendi del metodo vendi e immagazzina del metodo immagazzina.
Il main invoca i metodi pubblici vendi e immagazzina.
Le variabili MAXSCORTE e MAXORDINE (anch’esse gia` fornite) contengono il massimo quantitativo di prodotto
immagazzinabile e il massimo quantitativo di prodotto acquistabile da un’acquirente.
• Gli attributi quantita, in_esaurimento e stato_scorte sono accessibili con il loro nome e
  modificabili con ‘=‘ mentre dizionario è modificabile con il seguente metodo:
  - il metodo aggiorna(self,nome,numero,data) che prende in input il nome di un acquirente, il numero di prodotti
    acquistati e la data dell’acquisto e inserisce nel dizionario acquirenti un’entrata con queste informazioni.
• Usare l’approccio state specific per implementare stato_scorte tenendo conto che se stato_scorte e` altamente disponibile
  allora non e` possibile immagazzinare ulteriori quantita` del prodotto mentre se e` non disponibile allora non e` possibile
  effettuare vendite del prodotto. Zero punti a chi non usa questo approccio.
• Il nome del prodotto e` una stringa settata da __init__ (self,nome).
"""

from datetime import date


class Prodotto:
    M = "altamente disponibile"
    D = "disponibile"
    E = "non disponibile"
    MAXSCORTE = 1000
    MAXORDINE = 350

    def __init__(self, nome):
        self.nome = nome
        self.quantita = 0
        self.stato_scorte = Prodotto.E
        self._acquirenti = {}

    def aggiorna(self, nome, numero, data):
        self._acquirenti[nome] = (numero, data)

    def vendi(self, nomeAcquirente, numero):
        self._vendi(nomeAcquirente, numero)

    def immagazzina(self, numero):
        self._immagazzina(numero)

    def _vendi(self, nomeAcquirente, numero):
        if numero > Prodotto.MAXORDINE or numero > self.quantita:
            print(f"Attenzione: vendita di {numero} unita` del prodotto {self.nome} non possibile")
            return
        else:
            self.quantita = self.quantita - numero
            self.aggiorna(nomeAcquirente, numero, date.today())
            if self.quantita == 0:
                self.stato_scorte = Prodotto.E
            if 0 < self.quantita < Prodotto.MAXSCORTE:
                self.stato_scorte = Prodotto.D

    def elimina_scorte(self):
        self.quantita = 0
        self.stato_scorte = Prodotto.E

    def _immagazzina(self, numero):
        if numero <= 0:
            return
        self.quantita = self.quantita + numero
        if 0 < self.quantita < Prodotto.MAXSCORTE:
            self.stato_scorte = Prodotto.D
        if self.quantita == Prodotto.MAXSCORTE:
            self.stato_scorte = Prodotto.M


def main():
    p1 = Prodotto("Paperini")
    print("Inizialmente il prodotto {} e` nello stato {}".format(p1.nome, p1.stato_scorte))
    print("Immagazziniamo {} unita di prodotto {}".format(Prodotto.MAXSCORTE, p1.nome))
    p1.immagazzina(Prodotto.MAXSCORTE)
    print(
        "Il prodotto {} e` nello stato {} e la quantita` di prodotto disponibile e` {}".format(p1.nome, p1.stato_scorte,
                                                                                               p1.quantita))
    print("SupermarketSun vuole acquistare 100 unita` di prodotto {}".format(p1.nome))
    p1.vendi("SupermarketSun", 100)
    print("SupermarketlongS vuole acquistare 160 unita` di prodotto {}".format(p1.nome))
    p1.vendi("SupermarketLongS", 160)
    print("SupermarketFoop vuole acquistare 150 unita` di prodotto {}".format(p1.nome))
    p1.vendi("SupermarketFoop", 150)
    print("SupermarketPrai vuole acquistare 110 unita` di prodotto {}".format(p1.nome))
    p1.vendi("SupermarketPrai", 110)
    print("SupermarketLongS vuole acquistare 150 unita` di prodotto {}".format(p1.nome))
    p1.vendi("SupermarketLongS", 150)
    print("SupermarketRonald vuole acquistare 120 unita` di prodotto {}".format(p1.nome))
    p1.vendi("SupermarketRonald", 120)
    print("SupermarketPrai vuole acquistare 140 unita` di prodotto {}".format(p1.nome))
    p1.vendi("SupermarketPrai", 140)
    print("SupermarketRonald vuole acquistare 150 unita` di prodotto {}".format(p1.nome))
    p1.vendi("SupermarketRonald", 150)
    print("SupermarketSun vuole acquistare 30 unita` di prodotto {}".format(p1.nome))
    p1.vendi("SupermarketSun", 30)

    print("\nQuesti sono gli ultimi acquisti effettuati da ciascun cliente del prodotto ", p1.nome)
    for k, v in p1._acquirenti.items():
        print("{} ha acquistato {} unita` il giorno {}".format(k, v[0], v[1]))
    print("Eliminiamo scorte del prodotto {}".format(p1.nome))
    p1.elimina_scorte()
    if p1.quantita == 0:
        print("Non vi sono piu` scorte del prodotto {} in magazzino".format(p1.nome))

    else:
        print("qualcosa non va nell'implementazione")


if __name__ == "__main__":
    main()

"""Il programma deve stampare:

Inizialmente il prodotto Paperini e` nello stato non disponibile
Immagazziniamo 1000 unita di prodotto Paperini
Il prodotto Paperini e` nello stato altamente disponibile e la quantita` di prodotto disponibile e` 1000
SupermarketSun vuole acquistare 100 unita` di prodotto Paperini
SupermarketlongS vuole acquistare 160 unita` di prodotto Paperini
SupermarketFoop vuole acquistare 150 unita` di prodotto Paperini
SupermarketPrai vuole acquistare 110 unita` di prodotto Paperini
SupermarketLongS vuole acquistare 150 unita` di prodotto Paperini
SupermarketRonald vuole acquistare 120 unita` di prodotto Paperini
SupermarketPrai vuole acquistare 140 unita` di prodotto Paperini
SupermarketRonald vuole acquistare 150 unita` di prodotto Paperini
Attenzione: vendita di 150 unita` del prodotto Paperini non possibile
SupermarketSun vuole acquistare 30 unita` di prodotto Paperini

Questi sono gli ultimi acquisti effettuati da ciascun cliente del prodotto  Paperini
SupermarketSun ha acquistato 30 unita` il giorno 2019-12-16
SupermarketLongS ha acquistato 150 unita` il giorno 2019-12-16
SupermarketFoop ha acquistato 150 unita` il giorno 2019-12-16
SupermarketPrai ha acquistato 140 unita` il giorno 2019-12-16
SupermarketRonald ha acquistato 120 unita` il giorno 2019-12-16
Eliminiamo scorte del prodotto Paperini
Non vi sono piu` scorte del prodotto Paperini in magazzino
"""
