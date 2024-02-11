"""
Scrivere una coroutine sender(receiver, maximum) che prende in input una coroutine receiver e un numero maximum, e si comporta come segue:
ogni volta che riceve qualcosa controlla se quanto ha ricevuto è un numero e se lo è lo somma
ad una variabile locale sum e lo inserisce in una lista L.
Quando questa variabile raggiunge valore maggiore o uguale a maximum, sender invia L a receiver e poi azzera
sum e pone L uguale alla lista vuota.
Se sender riceve un oggetto che non è un numero allora smette di funzionare dopo aver fatto in modo che
anche receiver smetta di funzionare.
Scrivere inoltre una coroutine writer(file) che ogni volta che riceve una collezione scrive gli elementi
della collezione su una nuova linea del file di nome file separati da uno spazio.
Se il file non esiste writer lo crea; se il file esiste gia` allora write comincia a scrivere sotto l’ultima linea del file.
Il parametro receiver di sender e` una coroutine writer.
"""
import functools


def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        next(generator)
        return generator

    return wrapper


@coroutine
def sender(receiver, maximum):
    somma = 0
    L = []
    while True:
        data = (yield)
        if isinstance(data, int):
            somma += data
            L.append(data)
            if somma >= maximum:
                receiver.send(L)
                somma = 0
                L = []
        else:
            receiver.close()
            return


@coroutine
def writer(file):
    while True:
        data = (yield)
        file_handler = open(file, "a")
        file_handler.write(" ".join(map(str, data)) + "\n")
        file_handler.close()


def main():
    s = sender(writer("file"), 100.5)

    for i in range(3, 10):
        for x in range(1, 30, i):
            try:
                s.send(x)

            except StopIteration:
                print("Il sender {} non accetta piu` richieste perche' e` stato inviato un oggetto non numerico")
                print()
    o = open("file", 'r')
    print("Questo e` il contenuto del file:")
    for line in o:
        print(line)

    for i in range(6, 10):
        for x in range(7, 60, i):
            try:
                s.send(x)
            except StopIteration:
                print("Il sender {} non accetta piu` richieste perche' e` stato inviato un oggetto non numerico")
                print()

    o = open("file", 'r')
    print("Questo e` il contenuto del file:")
    for line in o:
        print(line)

    for i in range(6, 8):
        for x in range(7, 15, i):
            try:
                s.send(x)
            except StopIteration:
                print("Il sender {} non accetta piu` richieste perche' e` stato inviato un oggetto non numerico")
                print()

    try:
        s.send('pop')
    except StopIteration:
        print("Il sender {} non accetta piu` richieste perche' e` stato inviato un oggetto non numerico")
        print()

    o = open("file", 'r')
    print("Questo e` il contenuto del file:")
    for line in o:
        print(line)

    s.close()


if __name__ == "__main__":
    main()

"""
Ricordatevi di cancellare il file ogni volta che eseguite il programma!

Il programma deve stampare: 

Questo e` il contenuto del file:
1 4 7 10 13 16 19 22 25 

28 1 5 9 13 17 21 25 

29 1 6 11 16 21 26 

1 7 13 19 25 1 8 15 22 

29 1 9 17 25 1 10 19 

Questo e` il contenuto del file:
1 4 7 10 13 16 19 22 25 

28 1 5 9 13 17 21 25 

29 1 6 11 16 21 26 

1 7 13 19 25 1 8 15 22 

29 1 9 17 25 1 10 19 

28 7 13 19 25 31 

37 43 49 

55 7 14 21 28 

35 42 49 

56 7 15 23 

31 39 47 

55 7 16 25 

34 43 52 

Il sender {} non accetta piu` richieste perche' e` stato inviato un oggetto non numerico

Questo e` il contenuto del file:
1 4 7 10 13 16 19 22 25 

28 1 5 9 13 17 21 25 

29 1 6 11 16 21 26 

1 7 13 19 25 1 8 15 22 

29 1 9 17 25 1 10 19 

28 7 13 19 25 31 

37 43 49 

55 7 14 21 28 

35 42 49 

56 7 15 23 

31 39 47 

55 7 16 25 

34 43 52 

"""
