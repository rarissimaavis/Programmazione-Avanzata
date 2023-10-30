"""
Scrivere una funzione che prende in input una sequenza di richieste (liste di due interi) e passa ciascuna richiesta
ad una catena di gestori ciascuno dei quali è una coroutine.
• Se il primo intero della lista è nell’intervallo [0,4] allora la richiesta viene gestita dal gestore Handler_04 che
    stampa “Richiesta {} gestita da Handler_04“.
• Se il primo intero della lista è nell’intervallo [5,9] allora la richiesta viene gestita da gestore Handler_59 che
    stampa “Richiesta {} gestita da Handler_59“.
• Se il primo intero della lista è maggiore di 9 allora la richiesta viene gestita dal gestore Handler_gt9 che stampa
    “Messaggio da Handler_gt9: non è stato possibile gestire la richiesta {}. Richiesta modificata".
    Dopo aver effettuato la stampa Handler_gt9 sottrae al primo intero della lista il secondo intero della lista e lo
    invia nuovamente ad una nuova catena di gestori.
• Se la richiesta non è una lista di due numeri o il primo intero della lista è minore di 0 la richiesta viene gestita da
    Default_Handler che stampa semplicemente “Richiesta {} gestita da Default_Handler: non è stato possibile gestire la richiesta {}”.
Nelle suddette stampe la lista nella richiesta deve comparire al posto delle parentesi graffe.
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
def Handler_04(successor=None):
    while True:
        event = (yield)
        if isinstance(event[0], int) and isinstance(event, list) and len(event) == 2 and 0 <= event[0] <= 4:
            print(f"Richiesta {event} gestita da Handler_04")
        elif successor is not None:
            successor.send(event)


@coroutine
def Handler_59(successor=None):
    while True:
        event = (yield)
        if isinstance(event[0], int) and isinstance(event, list) and len(event) == 2 and 5 <= event[0] <= 9:
            print(f"Richiesta {event} gestita da Handler_59")
        elif successor is not None:
            successor.send(event)


@coroutine
def Handler_gt9(successor=None):
    while True:
        event = (yield)
        if isinstance(event[0], int) and isinstance(event[1], int) and isinstance(event, list) and len(event) == 2 and event[0] > 9:
            print(f"Messaggio da Handler_gt9: non è stato possibile gestire la richiesta {event}. Richiesta modificata")
            event[0] -= event[1]
            handler = Handler_04(Handler_59(Handler_gt9(Default_Handler(None))))
            handler.send(event)
        elif successor is not None:
            successor.send(event)


@coroutine
def Default_Handler(successor):
    while True:
        event = (yield)
        if not (isinstance(event, list) and len(event) == 2 and isinstance(event[0], int) and isinstance(event[1], int)) or event[0] < 0:
            print(f"Richiesta {event} gestita da Default_Handler: non è stato possibile gestire la richiesta {event}")
        elif successor is not None:
            successor.send(event)


# test
class Client:
    """Client: Uses handlers"""

    def __init__(self):
        self.handler = Handler_04(Handler_59(Handler_gt9(Default_Handler(None))))

    def delegate(self, requests):
        """Iterates over requests and sends them, one by one, to handlers as per sequence of handlers defined above."""
        for request in requests:
            self.handler.send(request)
        self.handler.close()


# Create a client object
cliente = Client()

# Create richieste to be processed.
richieste = []

for i in range(0, 15, 2):
    richieste.append([i, 7])
richieste.append([-3, 4])
richieste.append(["a", 2])
richieste.append([1, 2, 4])
cliente.delegate(richieste)

"""
Il programma deve stampare:

Richiesta [0, 7] gestita da Handler_04
Richiesta [2, 7] gestita da Handler_04
Richiesta [4, 7] gestita da Handler_04
Richiesta [6, 7] gestita da Handler_59
Richiesta [8, 7] gestita da Handler_59
Messaggio da Handler_gt9:  non e` stato possibile gestire la richiesta [10, 7]. Richiesta modificata
Richiesta [3, 7] gestita da Handler_04
Messaggio da Handler_gt9:  non e` stato possibile gestire la richiesta [12, 7]. Richiesta modificata
Richiesta [5, 7] gestita da Handler_59
Messaggio da Handler_gt9:  non e` stato possibile gestire la richiesta [14, 7]. Richiesta modificata
Richiesta [7, 7] gestita da Handler_59
Richiesta [-3, 4] gestita da Default_Handler:  non e` stato possibile gestire la richiesta [-3, 4]
Richiesta ['a', 2] gestita da Default_Handler:  non e` stato possibile gestire la richiesta ['a', 2]
Richiesta [1, 2, 4] gestita da Default_Handler:  non e` stato possibile gestire la richiesta [1, 2, 4]
"""
