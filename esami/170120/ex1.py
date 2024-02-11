"""
Scrivere una coroutine searcher(c1,c2,receiver1, receiver2) che prende in input due caratteri c1 e c2 e due
coroutine receiver1, receiver2, e si comporta come segue:
ogni volta che riceve qualcosa verifica se questa e` il nome di un file esistente e nel caso in cui lo sia cerca
all’interno del file le stringhe che cominciano con c1 e quelle che cominciano con c2, le prime vengono inviate
a receiver1 mentre le seconde a receiver2.
Nel caso in cui non esista un file con quel nome, la coroutine esegue solo la stampa della seguente stringa
"Il file {} e` inesistente", dove al posto delle parentesi deve comparire il nome del file.
Scrivere inoltre una coroutine listCreator(stop) che ogni volta che riceve una stringa la inserisce in una lista
(la lista e` una variabile locale alla coroutine) e stampa la lista aggiornata con l’aggiunta della nuova parola.
I parametri receiver1 e receiver2 di searcher sono due coroutine listCreator.
Versione da al massimo 6 punti: la coroutine listCreator non fa niente altro rispetto a
quanto sopra descritto (l’input stop viene ignorato).
Versione da al massimo 10 punti: La couroutine smette di ricevere parole non appena
riceve una parola uguale alla stringa stop passata come argomento.
Nell’implementazione della coroutine searcher occorre tenere conto del fatto che uno o entrambi i receiver
potrebbero non ricevere piu` le parole inviate.
Se ad un certo punto entrambi i receiver smettono di ricevere parole il searcher deve smettere anch’esso di ricevere stringhe.
Suggerimento: potete usare re.findall(r'\w+', testo) per estrarre parole da un testo.
"""
import functools
import re


def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        next(generator)
        return generator

    return wrapper


@coroutine
def searcher(c1, c2, receiver1, receiver2):
    alive1 = True
    alive2 = True
    while True:
        fileName = (yield)
        try:
            fOb = open(fileName, "r")
        except FileNotFoundError:
            print(f"Il file {fileName} è inesistente")
            continue

        for line in fOb:
            res = re.findall(r'\w+', line)
            for word in res:
                if word[0] == c1:
                    try:
                        receiver1.send(word)
                    except StopIteration:
                        alive1 = False
                elif word[0] == c2:
                    try:
                        receiver2.send(word)
                    except StopIteration:
                        alive2 = False
                if not (alive1 or alive2):
                    fOb.close()
                    return
        fOb.close()


@coroutine
def listCreator(stop):
    l = []
    while True:
        word = (yield)
        if word == stop:
            return
        l.append(word)
        print(f"La lista delle parole fino ad ora trovate che cominciano per '{word[0]}' è:", l)


def main():
    searchers = [searcher('a', 'A', listCreator("ancora"), listCreator("Alto")),
                 searcher('a', 'A', listCreator("alto"), listCreator("Ancora"))]

    for i, f in enumerate(searchers, start=1):
        print("Richiesta \"fileNE\" inviata al searcher {}:".format(i))
        f.send("fileNE")
        print()

    for i, f in enumerate(searchers, start=1):
        try:
            print("Richiesta \"fileI\" inviata al searcher {}:".format(i))
            f.send("fileI")
            print()


        except StopIteration:
            print(
                "Il searcher {} non accetta piu` richieste perche' entrambi i suoi ricevitori hanno smesso di ricevere parole".format(
                    i))
            print()

    for i, f in enumerate(searchers, start=1):
        try:
            print("Richiesta \"fileII.txt\" inviata al searcher  {}:".format(i))
            f.send("fileII.txt")
            print()

        except StopIteration:
            print(
                "Il searcher {} non accetta piu` richieste perche' entrambi i suoi ricevitori hanno smesso di ricevere parole".format(
                    i))
            print()

    for sel in searchers:
        sel.close()


if __name__ == "__main__":
    main()

"""
Il programma deve stampare:

Richiesta "fileNE" inviata al searcher 1:
Il file fileNE e` inesistente

Richiesta "fileNE" inviata al searcher 2:
Il file fileNE e` inesistente

Richiesta "fileI" inviata al searcher 1:
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo']
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno']
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno', 'asprigno']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo', 'Ascolta']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo', 'Ascolta', 'Ascolto']
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno', 'asprigno', 'ameno']
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno', 'asprigno', 'ameno', 'alto']
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno', 'asprigno', 'ameno', 'alto', 'affermazione']

Richiesta "fileI" inviata al searcher 2:
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo']
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno']
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno', 'asprigno']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo', 'Ascolta']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo', 'Ascolta', 'Ascolto']
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno', 'asprigno', 'ameno']
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno', 'asprigno', 'ameno', 'alto']

Richiesta "fileII.txt" inviata al searcher  1:
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno', 'asprigno', 'ameno', 'alto', 'affermazione', 'aurora']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo', 'Ascolta', 'Ascolto', 'Allenamento']
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno', 'asprigno', 'ameno', 'alto', 'affermazione', 'aurora', 'assurdo']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo', 'Ascolta', 'Ascolto', 'Allenamento', 'Alto']
La lista delle parole fino ad ora trovate che cominciano per 'a' e` ['attimo', 'almeno', 'asprigno', 'ameno', 'alto', 'affermazione', 'aurora', 'assurdo', 'ancora']
Il searcher 1 non accetta piu` richieste perche' entrambi i suoi ricevitori hanno smesso di ricevere parole

Richiesta "fileII.txt" inviata al searcher  2:
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo', 'Ascolta', 'Ascolto', 'Allenamento']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo', 'Ascolta', 'Ascolto', 'Allenamento', 'Alto']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo', 'Ascolta', 'Ascolto', 'Allenamento', 'Alto', 'Aversa']
La lista delle parole fino ad ora trovate che cominciano per 'A' e` ['Allora', 'Aperitivo', 'Ascolta', 'Ascolto', 'Allenamento', 'Alto', 'Aversa', 'Ancora']
Il searcher 2 non accetta piu` richieste perche' entrambi i suoi ricevitori hanno smesso di ricevere parole

"""
