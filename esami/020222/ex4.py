"""
Scrivere la funzione max_num_occorrenze. Se la funzione ha bisogno di invocare altre procedure, fornire anche queste ultime.
La funzione max_num_occorrenze prende in input una parola P, una collezione iterabile di nomi di file
listaDiFile, e il parametro concorrenza.
Facendo uso di multiprocessing.JoinableQueue, la funzione deve calcolare il numero di occorrenze di P in ciascuno
dei file di listaDiFile e alla fine restituire la coppia (fileconmax,max), dove fileconmax è il file in cui P compare
il massimo numero di volte e max è questo massimo numero di volte.
Il numero di occorrenze di P in un file deve essere computato con un processo separato per ogni file di listaDiFile.
"""

import multiprocessing


def cercaConc(fileN, parola):
    ofile = open(fileN, "r")
    testo = ofile.read()
    return testo.count(parola)


def max_num_occorrenze(listaDiFile, p, concurrency):
    jobs = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()
    create_processes(jobs, results, concurrency)
    add_jobs(listaDiFile, p, jobs)
    jobs.join()

    count_dict = {}
    while not results.empty():
        fileN, count = results.get()
        count_dict[fileN] = count

    max_file = max(count_dict, key=count_dict.get)
    return max_file, count_dict[max_file]


def worker(jobs, results):
    while True:
        file, parola = jobs.get()
        result = cercaConc(file, parola)
        if result != -1:
            results.put((file, result))
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
    parola = "computer"
    print(max_num_occorrenze(files, parola, 4))


if __name__ == "__main__":
    main()

"""
('file2', 4)
"""
