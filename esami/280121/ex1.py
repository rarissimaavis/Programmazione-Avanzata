"""
Scrivere una funzione che prende in input una sequenza di richieste (stringhe) e passa ciascuna richiesta ad una catena
di gestori ciascuno dei quali e‘ una coroutine (usando il decoratore @coroutine visto a lezione).
• Se la stringa comincia con una lettera compresa tra ‘a’ e ‘g’ allora la richiesta viene
  gestita dal gestore gestore_ag che stampa “Richiesta {} gestita da gestore_ag“.
• Se la stringa comincia con una lettera compresa tra ‘h’ e ‘n’ allora la richiesta viene
  gestita dal gestore gestore_hn che stampa “Richiesta {} gestita da gestore_hn“.
• Se la stringa NON comincia con una lettera allora la richiesta viene gestita dal gestore gestore_distr che stampa
  “Richiesta {} gestita da gestore_distr: uso improprio della catena di gestori“ e poi smette di funzionare.
• Se la stringa comincia con una lettera dell’alfabeto successiva ad ‘n’ o con una maiuscola allora la richiesta viene gestita
  dal gestore gestoreDiDefault che stampa “Messaggio da gestoreDiDefault: non è stato possibile gestire la richiesta {}“.
Nelle suddette stampe il nome della richiesta deve comparire al posto delle parentesi graffe.
Se ad un certo punto un gestore manda la richiesta al suo successore e il successore smette di funzionare allora anche
il gestore che inviato la richiesta deve smettere di funzionare.
Prima di smettere di funzionare il gestore deve stampare “Il successore di {} ha smesso di funzionare a causa della
richiesta {} e di conseguenza smette di funzionare anche {}“, dove al posto della I e III coppia di parentesi graffe
deve comparire il nome del gestore e al posto della II coppia il nome della richiesta.
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
def gestore_ag(successor=None):
    while True:
        req = (yield)
        if "a" <= req[0] <= "g":
            print(f"Richiesta {req} gestita da gestore_ag")
        if successor is not None:
            try:
                successor.send(req)
            except StopIteration:
                print(f"Il successore di {gestore_ag.__name__} ha smesso di funzionare a causa della richiesta {req} e di conseguenza smette di funzionare anche {gestore_ag.__name__}")
                break


@coroutine
def gestore_hn(successor=None):
    while True:
        req = (yield)
        if "h" <= req[0] <= "n":
            print(f"Richiesta {req} gestita da gestore_hn")
        if successor is not None:
            try:
                successor.send(req)
            except StopIteration:
                print(f"Il successore di {gestore_hn.__name__} ha smesso di funzionare a causa della richiesta {req} e di conseguenza smette di funzionare anche {gestore_hn.__name__}")
                break


@coroutine
def gestore_distr(successor):
    while True:
        req = (yield)
        if not req[0].isalpha():
            print(f"Richiesta {req} gestita da gestore_distr: uso improprio della catena di gestori")
            break
        if successor is not None:
            try:
                successor.send(req)
            except StopIteration:
                print(f"Il successore di {gestore_distr.__name__} ha smesso di funzionare a causa della richiesta {req} e di conseguenza smette di funzionare anche {gestore_distr.__name__}")
                break


@coroutine
def gestoreDiDefault(successor=None):
    while True:
        req = (yield)
        if req[0] > "n" or req[0].isupper():
            print(f"Messaggio da gestoreDiDefault: non e` stato possibile gestire la richiesta {req}")
        if successor is not None:
            try:
                successor.send(req)
            except StopIteration:
                break


# test
class Client:
    """Client: Uses handlers"""

    def __init__(self):
        self.handler = gestore_ag(gestore_hn(gestore_distr(gestoreDiDefault(None))))

    def delegate(self, requests):
        """Iterates over requests and sends them, one by one, to handlers as per sequence of handlers defined above."""
        for request in requests:
            try:
                self.handler.send(request)
            except StopIteration:
                print("La catena ha smesso di accettare richieste")

        self.handler.close()


cliente = Client()

richieste = ["b", "l", "x", "M", "1cc"]

cliente.delegate(richieste)
