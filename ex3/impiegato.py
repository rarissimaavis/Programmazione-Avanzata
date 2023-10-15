"""
Scrivere una classe Impiegato e due sue sottoclassi Tecnico e Amministrativo
In aggiunta al metodo __init__ , le classe Impiegato puo` avere un solo altro metodo
mentre le due sottoclassi possono avere solo __init__

Scrivere poi un programma che crei un certo numero di istanze delle tre classi e stampa il numero di tecnici, il numero
di amministrativi e il numero totale di impiegati (questo potrebbe essere maggiore dalla somma del numero di tecnici
e amministrativi perche’ è possibile creare impiegati ‘‘generici’’ creando direttamente instanze della classe impiegato)
"""


class Impiegato:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def info(self):
        return f"{self.nome} {self.cognome}"


class Tecnico(Impiegato):
    def __init__(self, nome, cognome):
        super().__init__(nome, cognome)


class Amministrativo(Impiegato):
    def __init__(self, nome, cognome):
        super().__init__(nome, cognome)


impiegati = [Impiegato("A", "B"), Tecnico("C", "D"), Amministrativo("E", "F")]

num_tecnici = sum(1 for impiegato in impiegati if isinstance(impiegato, Tecnico))
num_amministrativi = sum(1 for impiegato in impiegati if isinstance(impiegato, Amministrativo))
num_impiegati_tot = len(impiegati)

print(f"Numero totale di impiegati: {num_impiegati_tot}")
print(f"Numero di tecnici: {num_tecnici}")
print(f"Numero di amministrativi: {num_amministrativi}")
