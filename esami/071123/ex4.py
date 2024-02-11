"""
Scrivere la funzione creaDiz. Se la funzione ha bisogno di invocare altre procedure, fornire anche queste ultime.
La funzione creaDiz prende in input una lista di tuple e il parametro concorrenza, e crea un numero di istanze di dict
pari al numero di elementi della lista.
L’i-esima istanza creata deve avere un numero di chiavi uguale alla lunghezza delle tupla i-esima.
Le coppie (chiave,valore) dell’i-esimo dizionario sono (1,t1),(2,t2),…, (1,tj),..., dove tj e` il j-esimo elemento della i-esima tupla.
Facendo uso di Futures, creaDiz deve creare ciascuna istanza di dict con un processo separato e stampare i contenuti dei dizionari.
Le stampe devono essere effettuate nell’ordine in cui terminano i processi.
"""
import concurrent.futures


def creaDizionario(t):
    d = dict()
    s = 0
    for j in range(0, len(t)):
        d[j + 1] = t[j]
    return d


# solo per rendere più evidente chi sono i job
def get_jobs(tuples):
    for t in tuples:
        yield t


def creaDiz(tuples, concurrency):
    futures = set()
    with concurrent.futures.ProcessPoolExecutor(max_workers=concurrency) as executor:
        for i, t in enumerate(get_jobs(tuples)):
            future = executor.submit(creaDizionario, t)
            futures.add(future)
        wait_for(futures)


def wait_for(futures):
    for future in concurrent.futures.as_completed(futures):
        print(f"Le entrate del dizionario sono {future.result()}")


def main():
    L = [i for i in range(100)]
    t = tuple(L)
    lista = [t, ("a", 2, 4, "b"), ("pop", "www", 3.2, [3],), (set((1, 2, 3)), "bbb", "qqq", 5.2, [3, 4, 5], [10, 4, 6])]

    creaDiz(lista, 3)


if __name__ == "__main__":
    main()

"""  Ecco cosa deve essere stampato (l'ordine delle righe potrebbe cambiare):
Le entrate del dizionario sono {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9, 11: 10, 12: 11, 13: 12, 14: 13, 15: 14, 16: 15, 17: 16, 18: 17, 19: 18, 20: 19, 21: 20, 22: 21, 23: 22, 24: 23, 25: 24, 26: 25, 27: 26, 28: 27, 29: 28, 30: 29, 31: 30, 32: 31, 33: 32, 34: 33, 35: 34, 36: 35, 37: 36, 38: 37, 39: 38, 40: 39, 41: 40, 42: 41, 43: 42, 44: 43, 45: 44, 46: 45, 47: 46, 48: 47, 49: 48, 50: 49, 51: 50, 52: 51, 53: 52, 54: 53, 55: 54, 56: 55, 57: 56, 58: 57, 59: 58, 60: 59, 61: 60, 62: 61, 63: 62, 64: 63, 65: 64, 66: 65, 67: 66, 68: 67, 69: 68, 70: 69, 71: 70, 72: 71, 73: 72, 74: 73, 75: 74, 76: 75, 77: 76, 78: 77, 79: 78, 80: 79, 81: 80, 82: 81, 83: 82, 84: 83, 85: 84, 86: 85, 87: 86, 88: 87, 89: 88, 90: 89, 91: 90, 92: 91, 93: 92, 94: 93, 95: 94, 96: 95, 97: 96, 98: 97, 99: 98, 100: 99}
Le entrate del dizionario sono {1: 'a', 2: 2, 3: 4, 4: 'b'}
Le entrate del dizionario sono {1: 'pop', 2: 'www', 3: 3.2, 4: [3]}
Le entrate del dizionario sono {1: {1, 2, 3}, 2: 'bbb', 3: 'qqq', 4: 5.2, 5: [3, 4, 5], 6: [10, 4, 6]}
"""
