# versione modificata dell'ex4 dell'esame 17/01/20
"""
Scrivere la funzione stampa. Se la funzione ha bisogno di invocare altre procedure, fornire anche quest’ultime.
La funzione cerca prende in input una lista di stringhe listaParole, una collezione iterabile di nomi di file listaDiFile
e il parametro concorrenza.
Facendo uso di multiprocessing.JoinableQueue, la funzione stampa deve stampare per ciascuno dei file di listaDiFile
la parola del file che appare per prima in listaParole se esiste.
Se nessuna delle parole di listaParole appare nel file allora stampa deve stampare "Nessuna parola della lista appare nel file {}.",
dove al posto delle parentesi graffe deve comparire il nome del file.
Cio` deve essere fatto con un processo separato per ogni file di listaDiFile e le stampe devono essere effettuate
nell’ordine in cui terminano i processi.
Il callable usato da stampa deve prendere in input la lista di file e la parola.
NB: ricordatevi di riposizionare il cursore all’inizio del file con seek(0) ogni volta che cominciate a cercare una nuova parola nel file.
"""
import multiprocessing


def cercaConc(fileN, listaStringhe):
    count = 0
    toReturn = ""
    ofile = open(fileN, "r")
    for parola in listaStringhe:
        ofile.seek(0)
        testo = ofile.read()
        if parola in testo:
            return parola
    return toReturn


def stampa(listaDiFile, listaParole, concurrency):
    jobs = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()
    create_processes(jobs, results, concurrency)
    add_jobs(listaDiFile, listaParole, jobs)
    jobs.join()


def worker(jobs, results):
    while True:
        file, listaParole = jobs.get()
        result = cercaConc(file, listaParole)
        if result != "":
            print(f"La stringa del file {file} che appare per prima nella lista {listaParole} è \"{result}\".")
        else:
            print(f"Nessuna parola della lista appare nel file {file}.")
        jobs.task_done()


def create_processes(jobs, results, concurrency):
    for _ in range(concurrency):
        process = multiprocessing.Process(target=worker, args=(jobs, results))
        process.daemon = True
        process.start()


def add_jobs(listaDiFile, listaParole, jobs):
    for fn in listaDiFile:
        jobs.put((fn, listaParole))


def main():
    files = ["file1", "file2", "file3", "file4"]
    parole = ["computer", "very", "with", "it", "algorithms"]
    stampa(files, parole, 4)


if __name__ == "__main__":
    main()

"""
Ecco cosa deve essere stampato (l'ordine delle righe potrebbe cambiare):

La stringa del file file1 che appare per prima nella lista ['computer', 'very', 'with', 'it', 'algorithms'] è "computer".
La stringa del file file2 che appare per prima nella lista ['computer', 'very', 'with', 'it', 'algorithms'] è "very".
La stringa del file file3 che appare per prima nella lista ['computer', 'very', 'with', 'it', 'algorithms'] è "with".
La stringa del file file4 che appare per prima nella lista ['computer', 'very', 'with', 'it', 'algorithms'] è "it".
"""
