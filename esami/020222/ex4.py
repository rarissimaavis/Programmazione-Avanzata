"""
Scrivere la funzione max_num_occorrenze. Se la funzione ha bisogno di invocare altre procedure, fornire anche queste ultime.
La funzione max_num_occorrenze prende in input una parola P, una collezione iterabile di nomi di file
listaDiFile, e il parametro concorrenza.
Facendo uso di multiprocessing.JoinableQueue, la funzione deve calcolare il numero di occorrenze di P in ciascuno
dei file di listaDiFile e alla fine restituire la coppia (fileconmax,max), dove fileconmax è il file in cui P compare
il massimo numero di volte e max è questo massimo numero di volte.
Il numero di occorrenze di P in un file deve essere computato con un processo separato per ogni file di listaDiFile.
"""

