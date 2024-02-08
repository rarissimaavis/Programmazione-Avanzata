"""
Scrivere la funzione cerca. Se la funzione ha bisogno di invocare altre procedure, fornire anche quest’ultime.
La funzione cerca prende in input una lista di stringhe listaParole e una lista di nomi di file listaDiFile,
e il parametro concorrenza.
Facendo uso di multiprocessing.JoinableQueue, la funzione cerca deve stampare per ciascuno dei file di listaDiFile
la parola di listaParole che appare piu` volte nel file.
Cio` deve essere fatto con un processo separato per ogni file di listaDiFile e le stampe devono essere effettuate
nell’ordine in cui terminano i processi.
Il callable usato per effettuare la ricerca nel singolo file deve prendere in input la lista di parole e il nome del file.
NB: ricordatevi di riposizionare il cursore all’inizio del file con seek(0) ogni volta che cominciate a cercare una nuova parola nel file.
"""
import multiprocessing


def cercaConc(fileN, listaStringhe):
    count_dict = {parola: 0 for parola in listaStringhe}
    ofile = open(fileN, "r")
    for parola in listaStringhe:
        ofile.seek(0)
        testo = ofile.read().split()
        count_dict[parola] += sum(1 for word in testo if word == parola)
    max_parola = max(count_dict, key=count_dict.get)
    return max_parola


def cerca(listaDiFile, listaParole, concurrency):
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
            print(f"La stringa della lista {listaParole} che appare più volte nel file {file} è \"{result}\".")
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
    cerca(files, parole, 4)


if __name__ == "__main__":
    main()

"""
Ecco cosa deve essere stampato (l'ordine delle righe potrebbe cambiare):

La stringa della lista ['computer', 'very', 'with', 'it', 'algorithms'] che appare più volte nel file file1 è "computer".
La stringa della lista ['computer', 'very', 'with', 'it', 'algorithms'] che appare più volte nel file file2 è "very".
La stringa della lista ['computer', 'very', 'with', 'it', 'algorithms'] che appare più volte nel file file3 è "with".
La stringa della lista ['computer', 'very', 'with', 'it', 'algorithms'] che appare più volte nel file file4 è "it".
"""
