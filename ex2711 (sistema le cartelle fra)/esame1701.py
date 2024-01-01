"""
Scrivere nel file esercizio1_da_6.py o nel file esercizio1_da_10.py, a seconda della versione che si decide di svolgere,
una coroutine searcher(c1,c2,receiver1, receiver2) che prende in input due caratteri c1 e c2 e due coroutine receiver1,
receiver2, e si comporta come segue: ogni volta che riceve qualcosa verifica se questa e` il nome di un file esistente e
nel caso in cui lo sia cerca all’interno del file le stringhe che cominciano con c1 e quelle che cominciano con c2
Le prime vengono inviate a receiver1 mentre le seconde a receiver2. Nel caso in cui non esista un file con quel nome,
la coroutine esegue solo la stampa della seguente stringa "Il file {} e` inesistente", dove al posto delle parentesi
deve comparire il nome del file.
Scrivere inoltre una coroutine listCreator(stop) che ogni volta che riceve una stringa la inserisce in una lista
(la lista e` una variabile locale alla coroutine) e stampa la lista aggiornata con l’aggiunta della nuova parola.
I parametri receiver1 e receiver2 di searcher sono due coroutine listCreator.
Versione da al massimo 6 punti: la coroutine listCreator non fa niente altro rispetto a quanto sopra descritto
(l’input stop viene ignorato).
Versione da al massimo 10 punti: La couroutine smette di ricevere parole non appena riceve una parola uguale alla
stringa stop passata come argomento. Nell’implementazione della coroutine searcher occorre tenere conto del fatto che
uno o entrambi i receiver potrebbero non ricevere piu` le parole inviate. Se ad un certo punto entrambi i receiver
smettono di ricevere parole il searcher deve smettere anch’esso di ricevere stringhe.
Suggerimento: potete usare re.findall(r'\w+', testo) per estrarre parole da un testo.
"""

def main():
    searcher s = [searcher('a', 'A', listCreator("ancora"), listCreator("Alto"))
        , searcher('a', 'A', listCreator("alto"), listCreator("Ancora"))]

    for i, f in enumerate(searchers, start=1):
        print("Richiesta \"fileNE\" inviata al searcher {}:".format(i))
        f.send("fileNE")
        print()

    for i, f in enumerate(searchers, start=1):
        try:
            print("Richiesta \"fileI.txt\" inviata al searcher {}:".format(i))
            f.send("fileI.txt")
            print()


        except StopIteration:
            print \
                ("Il searcher {} non accetta piu` richieste perche' entrambi i suoi ricevitori hanno smesso di ricevere parole".format
                 (i))
            print()

    for i, f in enumerate(searchers, start=1):
        try:
            print("Richiesta \"fileII.txt\" inviata al searcher  {}:".format(i))
            f.send("fileII.txt")
            print()

        except StopIteration:
            print \
                ("Il searcher {} non accetta piu` richieste perche' entrambi i suoi ricevitori hanno smesso di ricevere parole".format
                 (i))
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

Richiesta "fileI.txt" inviata al searcher 1:
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

Richiesta "fileI.txt" inviata al searcher 2:
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
