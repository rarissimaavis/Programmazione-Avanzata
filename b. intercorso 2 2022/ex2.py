"""
Scrivere nel file esercizio2.py una coroutine trovaNumeri(m,calcola1, calcola2) che prende in input un intero m
e due coroutine calcola1, calcola2, e si comporta come segue:
ogni volta che riceve qualcosa verifica se questa e` il nome di un file esistente e, nel caso in cui lo sia,
cerca all’interno del file le stringhe che rappresentano interi.
Queste stringhe vengono convertite nei corrispondenti interi e questi vengono poi inviati a calcola1 se
maggiori di m e a calcola2 se minori o uguali di m. La coroutine trovanumeri effettua una stampa ogni volta
che prova ad inviare un intero ad una delle due coroutine calcola1 e calcola2.
Nel caso in cui non esista un file con quel nome, la coroutine smette di funzionare dopo aver stampato "Il file {} e` inesistente:
trovanumeri smette di funzionare", dove al posto delle parentesi deve comparire il nome del file e smette di funzionare.
Scrivere inoltre una coroutine eleva(esp, massimo) che prende in input due interi esp e stop e ogni volta che riceve
un intero lo eleva ad esp e stampa la somma degli interi fino a quel momento ricevuti tutti elevati ad esp.
Si veda output per capire come e` fatta l'intera stringa da stampare.
I parametri calcola1 e calcola2 di trovanumeri sono due coroutine eleva.
La couroutine eleva smette di funzionare non appena stampa una somma maggiore di massimo.
Nell’implementazione della coroutine trovanumeri occorre tenere conto del fatto che uno o entrambe le coroutine
calcola1 e calcola2 potrebbero non ricevere piu` gli interi che esso invia loro.
Se una sola delle coroutine smette di funzionare allora trovanumeri smette di provare a inviare richieste a questa
coroutine. Non appena si accorge che una delle due coroutine smette di funzionare effettua una stampa.
Se ad un certo punto entrambe le coroutine calcola1 e calcola2 smettono di funzionare, trovanumeri deve smettere anch’esso di funzionare.
Bonus: fate in modo che la coroutine eleva stampi il nome del parametro di
trovanumeri a cui essa corrispone (si veda seconda stampa dell'output).
Suggerimento: potete usare re.findall(r'\w+', testo) per estrarre parole da un testo.
"""
import functools
import inspect
import re


def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        next(generator)
        return generator

    return wrapper


@coroutine
def trovanumeri(m, calcola1, calcola2):
    alive1 = True
    alive2 = True
    while True:
        fileName = (yield)
        try:
            fOb = open(fileName, "r")
        except FileNotFoundError:
            print(f"Il file {fileName} è inesistente: trovanumeri smette di funzionare")
            break

        for line in fOb:
            res = re.findall(r'\w1', line)
            for word in res:
                try:
                    i = int(word)
                    if i > m and alive1:
                        try:
                            print(f"trovanumeri prova a inviare {i} alla prima coroutine.")
                            calcola1.send(i)
                        except StopIteration:
                            print("la prima coroutine ha smesso di funzionare")
                            alive1 = False
                    elif i <= m and alive2:
                        try:
                            print(f"trovanumeri prova a inviare {i} alla seconda coroutine")
                            calcola2.send(i)
                        except StopIteration:
                            print("la seconda coroutine ha smesso di funzionare")
                            alive2 = False
                except ValueError:
                    pass
        fOb.close()
        if not alive1 or alive2:
            break


@coroutine
def eleva(esp, massimo):
    somma = 0
    while True:
        if somma > massimo:
            break
        i = (yield)
        if i is not None:
            st = inspect.stack()
            framecaller = st[1]
            x = re.findall(r'\w+', framecaller.code_context[0])
            somma += pow(i, esp)
            print(
                f"{x[0]}: è arrivato l'intero {i}. Il valore della somma di tutti i valori ricevuti elevati a {esp} è {somma}")


if __name__ == "__main__":
    quadrato1 = eleva(2, 100)
    cubo1 = eleva(3, 50)

    tn = [trovanumeri(4, quadrato1, cubo1), trovanumeri(4, cubo1, quadrato1)]
    print("Test")
    for i, f in enumerate(tn, start=1):
        try:
            print(f"Richiesta \"fileNonEsiste.txt\" inviata al trovanumeri {tn}.")
            f.send("fileNonEsiste.txt")
        except Exception:
            pass

    print("Test 2")
    for i, f in enumerate(tn, start=1):
        try:
            print(f"Richiesta \"numeri.txt\" inviata al trovanumeri {tn}.")
            f.send("numeri.txt")
        except Exception:
            pass
