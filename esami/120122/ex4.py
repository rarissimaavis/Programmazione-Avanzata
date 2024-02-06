"""
Scrivere la funzione stampa. Se la funzione ha bisogno di invocare altre procedure, fornire anche queste ultime.
La funzione stampa prende in input una parola P, una collezione iterabile di nomi di file listaDiFile, e il parametro concorrenza.
Facendo uso di multiprocessing.JoinableQueue, la funzione stampa deve stampare per ciascuno dei file di listaDiFile
"La parola {} appare nel file {} in posizione {}.”, dove al posto delle parentesi devono comparire P,
il nome del file e la posizione in cui P appare per la prima volta nel file.
Se P non appare nel file allora stampa deve stampare “La parola {} non appare nel file {}.”,
dove al posto delle parentesi graffe devono comparire, rispettivamente, P e il nome del file.
La ricerca della parola deve essere effettuata con un processo separato per ogni file di listaDiFile e le stampe
devono essere effettuate nell’ordine in cui terminano i processi e quando sono stati elaborati tutti i file.
Il callable usato da stampa deve prendere in input la collezione dei nomi dei file e la parola.
"""
import multiprocessing


def cercaConc(fileN, parola):
    ofile = open(fileN, "r")
    testo = ofile.read()
    return testo.find(parola)


def stampa(listaDiFile, p, concurrency):
    jobs = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()
    create_processes(jobs, results, concurrency)
    add_jobs(listaDiFile, p, jobs)
    jobs.join()


def worker(jobs, results):
    while True:
        file, parola = jobs.get()
        result = cercaConc(file, parola)
        if result != -1:
            print(f"La parola {parola} appare nel file {file} in posizione {result}.")
        else:
            print(f"La parola {parola} non appare nel file {file}.")
        jobs.task_done()


def create_processes(jobs, results, concurrency):
    for _ in range(concurrency):
        process = multiprocessing.Process(target=worker, args=(jobs, results))
        process.daemon = True
        process.start()


def add_jobs(listaDiFile, p, jobs):
    for fn in listaDiFile:
        jobs.put((fn, p))


def main():
    files = ["file1", "file2", "file3", "file4"]
    parola = "algorithms"
    stampa(files, parola, 4)


if __name__ == "__main__":
    main()

"""
Ecco cosa deve essere stampato (l'ordine delle righe potrebbe cambiare):

La parola algorithms appare nel file file1 in posizione 43.
La parola algorithms appare nel file file2 in posizione 30.
La parola algorithms appare nel file file3 in posizione 25.
La parola algorithms appare nel file file4 in posizione 18.
"""
