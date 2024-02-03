"""
Scrivere, all’interno della classe Client, il metodo di istanza entrust che prende in input due liste.
La prima lista contiene delle stringhe mentre la seconda contiene dei caratteri singoli.
La funzione entrust crea una catena di gestori e le invia coppie del tipo (si, ci),
dove si è l’i-esima stringa della prima lista e ci è l’i-esimo carattere della seconda lista.
Ciascun gestore della catena è una coroutine e per una data coppia (s,c) funziona come segue.
• Se la stringa s non è vuota, comincia con una lettera dell’alfabeto e questa è uguale a c (secondo membro della coppia)
  allora la richiesta viene gestita dal gestore handler_eq che stampa “Richiesta {} gestita da handler_eq”.
• Se la stringa s non è vuota, comincia con una lettera dell’alfabeto e questa è diversa da c (secondo membro della coppia)
  allora la richiesta viene gestita dal gestore handler_diff che stampa “Richiesta {} gestita da handler_diff: richiesta modificata”.
  Il gestore quindi cancella il primo carattere della stringa ricevuta e la invia ad una
  nuova catena di gestori uguale a quella creata da entrust.
• Se la stringa s non è vuota e comincia con una numero compreso tra 0 e 9 allora la richiesta viene gestita dal gestore
  handler_digit che stampa “Richiesta {} gestita da handler_digit”.
• Se la stringa s è vuota o comincia con un carattere che non è ne’ una lettera ne’ un digit allora la richiesta viene
  gestita dal gestore DefaultHandler che stampa “Messaggio da DefaultHandler: non è stato possibile gestire la richiesta {} ".
Nelle suddette stampe il nome della richiesta deve comparire al posto delle parentesi graffe.
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
def handler_eq(successor=None):
    while True:
        s, c = (yield)
        if s and s[0].isalpha() and s[0] == c:
            print(f"Richiesta {s, c} gestita da handler_eq")
        if successor is not None:
            successor.send((s, c))


@coroutine
def handler_diff(successor=None):
    while True:
        s, c = (yield)
        if s and s[0].isalpha() and s[0] != c:
            print(f"Richiesta {s, c} gestita da handler_diff: richiesta modificata")
            s = s[1:]
        if successor is not None:
            successor.send((s, c))


@coroutine
def handler_digit(successor):
    while True:
        s, c = (yield)
        if s and s[0].isdigit():
            print(f"Richiesta {s, c} gestita da handler_digit")
        if successor is not None:
            successor.send((s, c))


@coroutine
def DefaultHandler(successor=None):
    while True:
        s, c = (yield)
        if not s or not (s[0].isdigit() or s[0].isalpha()):
            print(f"Messaggio da DefaultHandler: non è stato possibile gestire la richiesta {s, c}")
        if successor is not None:
            successor.send((s, c))


# test
class Client:

    def __init__(self):
        self.handler = handler_eq(handler_diff(handler_digit(DefaultHandler(None))))

    def entrust(self, requests1, requests2):
        for i in range(len(requests1)):
            try:
                self.handler.send((requests1[i], requests2[i]))
            except StopIteration:
                print("La catena ha smesso di accettare richieste")

        self.handler.close()


client = Client()

requests1 = ["apple", "123", "a123", "xyz", ""]
requests2 = ["a", "4", "b", "x", "5"]

client.entrust(requests1, requests2)

