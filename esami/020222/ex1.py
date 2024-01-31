"""
Scrivere una funzione che prende in input una sequenza di richieste (numeri) e passa ciascuna richiesta
ad una catena di gestori ciascuno dei quali e` una coroutine.
• Se il numero è compreso tra 0 e 100 allora la richiesta viene gestita dal gestore
  gestore_0_100 che stampa “Richiesta {} gestita da gestore_0_100”.
• Se il numero è compreso tra 101 e 200 allora la richiesta viene gestita dal gestore
  gestore_101_200 che stampa “Richiesta {} gestita da gestore_101_200”.
• Se il numero comincia con un numero negativo allora la richiesta viene gestita dal
  gestore gestore_negativo che smette di funzionare immediatamente dopo aver stampato
  “Richiesta {} gestita da gestore_negativo: la catena smette di funzionare”.
• Se il numero è maggiore di 200, allora la richiesta viene gestita dal gestore gestoreDiDefault
  che stampa “Messaggio da gestoreDiDefault: non e` stato possibile gestire la richiesta {}".
Se un gestore tenta di inviare una richiesta al suo successore e si accorge che questo
ha smesso di funzionare allora anch’esso deve smettere di funzionare.
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
def gestore_0_100(successor=None):
    while True:
        req = (yield)
        if 0 <= req <= 100:
            print(f"Richiesta {req} gestita da gestore_0_100")
        elif successor is not None:
            try:
                successor.send(req)
            except StopIteration:
                break


@coroutine
def gestore_101_200(successor=None):
    while True:
        req = (yield)
        if 101 <= req <= 200:
            print(f"Richiesta {req} gestita da gestore_101_200")
        elif successor is not None:
            try:
                successor.send(req)
            except StopIteration:
                break


@coroutine
def gestore_negativo(successor):
    while True:
        req = (yield)
        if req < 0:
            print(f"Richiesta {req} gestita da gestore_negativo: la catena smette di funzionare")
            break
        elif successor is not None:
            try:
                successor.send(req)
            except StopIteration:
                break


@coroutine
def gestoreDiDefault(successor=None):
    while True:
        req = (yield)
        if req > 200:
            print(f"Messaggio da gestoreDiDefault: non e` stato possibile gestire la richiesta {req}")
        elif successor is not None:
            try:
                successor.send(req)
            except StopIteration:
                break


# test
class Client:
    """Client: Uses handlers"""

    def __init__(self):
        self.handler = gestore_0_100(gestore_101_200(gestore_negativo(gestoreDiDefault(None))))

    def delegate(self, requests):
        """Iterates over requests and sends them, one by one, to handlers as per sequence of handlers defined above."""
        for request in requests:
            try:
                self.handler.send(request)
            except StopIteration:
                print("La catena ha smesso di accettare richieste")

        self.handler.close()


# Create a client object
cliente = Client()

# Create richieste to be processed
richieste = []

richieste = [101, 99, 300, -1, 5]

cliente.delegate(richieste)

"""
Il programma stampa:
Richiesta 101 gestita da gestore_101_200
Richiesta 99 gestita da gestore_0_100
Messaggio da gestoreDiDefault: non e` stato possibile gestire la richiesta 300
Richiesta -1 gestita da gestore_negativo: la catena smette di funzionare
La catena ha smesso di accettare richieste
La catena ha smesso di accettare richieste
"""
