"""
Scrivere nel file esercizio1.py una funzione generatrice generaQuadratoInput che prende come argomento
un intero m>=1 e restituisce un iteratore dei quadrati degli interi via via digitati dall'utente fino a quando
gli interi digitati sono minori o uguali di m.
Più precisamente, se it è l'iteratore generato da generaQuadratoInput(m) allora ogni volta che viene digitato next(it)
• il programma si mette in attesa che l'utente digiti qualcosa (seguito da return) e se l'utente digita un intero
minore o uguale di m allora nex(it) restituisce il quadrato dell'intero digitato; se invece l'intero digitato è maggiore di m,
 o l'utente digita qualcosa che non è un intero o interrompe l'esecuzione del programma, l'iteratore it smette di funzionare.

Sulla linea di comando dove viene immesso il numero fate comparire il prompt "Digita un intero--> ".

Suggerimenti: Per prendere valori input da tastiera potete usare input(). Non dimenticate di trasformare in intero il
valore preso in input prima di elevarlo al quadrato. Assicuratevi che il vostro codice "superi" il secondo test
inserito nei commenti. Se non "supera" il primo test il punteggio sara` un po' piu` basso.
"""


def generaQuadratoInput(m):
    while True:
        try:
            x = int(input("Digita un intero --> "))
            if x <= m:
                yield x*x
            else:
                break
        except (KeyboardInterrupt, ValueError):
            break


if __name__ == "__main__":
    it = generaQuadratoInput(100)

    for x in it:
        print("Questo e` il quadrato del numero digitato: ", x)

    print("Input non valido o l'utente ha forzato l'interruzione dello script:l'iteratore ha smesso di funzionare")
    print("Provo a invocare di nuovo next(it).")
    try:
        next(it)
    except StopIteration:
        print("L'iteratore ha smesso di funzionare")

"""
I test:
Se digito unn intero maggiore di 100 o qualcosa che non e` un intero, o se interrompo con ctrl+c lo script, il programma
stampa:

Digita un intero--> 
Input non valido o l'utente ha forzato l'interruzione dello script:l'iteratore ha smesso di funzionare
Provo a invocare di nuovo next(it).
L'iteratore ha smesso di funzionare

======================================================
II test:
Se invece eseguo nuovamente lo script e digito gli interi 5,2,10,6,104, il programma stampa:

Digita un intero--> 5
Questo e` il quadrato del numero digitato:  25
Digita un intero--> 2
Questo e` il quadrato del numero digitato:  4
Digita un intero--> 10
Questo e` il quadrato del numero digitato:  100
Digita un intero--> 6
Questo e` il quadrato del numero digitato:  36
Digita un intero--> 104
Input non valido o l'utente ha forzato l'interruzione dello script:l'iteratore ha smesso di funzionare
Provo a invocare di nuovo next(it).
L'iteratore ha smesso di funzionare


"""
