"""
Completare l’implementazione della classe UtenzeAbitazione in modo che le sue istanze possano essere
nello stato ON oppure nello stato OFF.
Oltre ai metodi gia` forniti, l’interfaccia “pubblica” della classe deve contenere i metodi apri_acqua, accendi_riscaldamento,
e get_consumi. Quando un’istanza è nello stato ON, i suddetti metodi si comportano come segue:
• apri_acqua(num_cl) incrementa la variabile di istanza _contatore_acqua del numero
  num_cl specificato come argomento
• accendi_riscaldamento(num_cl)
  • decrementa cl_serbatoio di un valore pari a num_cl se cl_serbatoio>num_cl;
    altrimenti usa tutto il gas disponibile, cioe` azzera cl_serbatoio.
  • aggiorna il registro in modo che la coppia del dizionario associata all’istanza
    abbia come valore il numero di cl di gas usati in totale fino a quel momento dall’abitazione.
  • se nel momento in cui viene invocato il metodo, cl_serbatoio è minore o uguale
    di num_cl (cio` include il caso in cui è inizialmente uguale a 0) allora il metodo
    dopo aver eventualmente eseguito i due punti precedenti, lancia ValueError in modo che
    venga visualizzata la stringa "Attenzione: il serbatoio condominiale e` vuoto".
• il metodo di istanza get_consumi() restituisce una coppia in cui il primo elemento è il consumo di acqua
  dell’abitazione e il secondo elemento è il consumo di gas dell’abitazione fino a quel momento.
Quando lo stato dell’istanza è OFF, i suddetti tre metodi non fanno niente e non restituiscono niente.
Le utenze vengono attivate e disattivate dai metodi attiva_utenze e disattiva_utenze, gia`
presenti nella classe insieme ai metodi __init__ , disponibilita_gas() e get_nome.
"""
import collections


class UtenzeAbitazione:
    ON, OFF = ("on", "off")
    cl_serbatoio = 10000
    registro = collections.defaultdict(int)

    def __init__(self, numAb):
        self._numero_abitazione = numAb
        self.stato = UtenzeAbitazione.OFF

    @property
    def state(self):
        return UtenzeAbitazione.ON if self.stato == self.ON else UtenzeAbitazione.OFF

    @state.setter
    def state(self, state):
        if state == UtenzeAbitazione.ON:
            self.apri_acqua = self.apri_acqua
            self.accendi_riscaldamento = self.accendi_riscaldamento
            self.get_consumi = self.get_consumi
        else:
            self.apri_acqua = lambda *args: None
            self.accendi_riscaldamento = lambda *args: None
            self.get_consumi = lambda *args: None

    def disponibilita_gas(self):
        return UtenzeAbitazione.cl_serbatoio

    def get_nome(self):
        return self._numero_abitazione

    def attiva_utenze(self):
        if self.stato == UtenzeAbitazione.OFF:
            self.stato = UtenzeAbitazione.ON
            self._contatore_acqua = 0
            UtenzeAbitazione.registro[self._numero_abitazione] = 0

    def disattiva_utenze(self):
        if self.stato == UtenzeAbitazione.ON:
            self.stato = UtenzeAbitazione.OFF
            UtenzeAbitazione.registro[self._numero_abitazione] = 0
            self._contatore_acqua = 0

    def apri_acqua(self, num_cl):
        if self.stato == UtenzeAbitazione.ON:
            self._contatore_acqua = num_cl

    def accendi_riscaldamento(self, num_cl):
        if self.stato == UtenzeAbitazione.ON:
            if UtenzeAbitazione.cl_serbatoio > num_cl:
                UtenzeAbitazione.registro[self._numero_abitazione] += num_cl
                UtenzeAbitazione.cl_serbatoio -= num_cl
            else:
                UtenzeAbitazione.registro[self._numero_abitazione] += UtenzeAbitazione.cl_serbatoio
                UtenzeAbitazione.cl_serbatoio = 0
                raise ValueError("Attenzione: il serbatoio condominiale e` vuoto")

    def get_consumi(self):
        return [self._contatore_acqua, UtenzeAbitazione.registro[self._numero_abitazione]]


def main():
    casa1 = UtenzeAbitazione(11)
    casa2 = UtenzeAbitazione(15)

    casa1.attiva_utenze()
    casa2.attiva_utenze()
    casa1.apri_acqua(15)
    casa2.apri_acqua(20)
    if casa1.get_consumi():
        print("Fino a questo momento l'abitazione {} ha consumato {} cl di acqua e {} cl di gas".format(casa1.get_nome(), casa1.get_consumi()[0], casa1.get_consumi()[1]))
    if casa2.get_consumi():
        print("Fino a questo momento l'abitazione {} ha consumato {} cl di acqua e {} cl di gas".format(casa2.get_nome(), casa2.get_consumi()[0], casa2.get_consumi()[1]))

    casa2.accendi_riscaldamento(5)
    casa1.accendi_riscaldamento(5)
    casa2.apri_acqua(20)
    if casa1.get_consumi():
        print("Fino a questo momento l'abitazione {} ha consumato {} cl di acqua e {} cl di gas".format(casa1.get_nome(), casa1.get_consumi()[0], casa1.get_consumi()[1]))
    if casa2.get_consumi():
        print("Fino a questo momento l'abitazione {} ha consumato {} cl di acqua e {} cl di gas".format(casa2.get_nome(), casa2.get_consumi()[0], casa2.get_consumi()[1]))

    casa1.disattiva_utenze()
    casa1.accendi_riscaldamento(35)

    casa2.attiva_utenze()
    casa2.apri_acqua(20)
    if casa1.get_consumi():
        print("Fino a questo momento l'abitazione {} ha consumato {} cl di acqua e {} cl di gas".format(casa1.get_nome(), casa1.get_consumi()[0], casa1.get_consumi()[1]))
    if casa2.get_consumi():
        print("Fino a questo momento l'abitazione {} ha consumato {} cl di acqua e {} cl di gas".format(casa2.get_nome(), casa2.get_consumi()[0], casa2.get_consumi()[1]))

    casa2.accendi_riscaldamento(9100)
    if casa2.get_consumi():
        print("Fino a questo momento l'abitazione {} ha consumato {} cl di acqua e {} cl di gas".format(casa2.get_nome(), casa2.get_consumi()[0], casa2.get_consumi()[1]))

    casa1.attiva_utenze()
    casa1.accendi_riscaldamento(885)

    if casa1.get_consumi():
        print("Fino a questo momento l'abitazione {} ha consumato {} cl di acqua e {} cl di gas".format(casa1.get_nome(), casa1.get_consumi()[0], casa1.get_consumi()[1]))

    print("Numero cl di gas presenti nel serbatoio condominiale:", UtenzeAbitazione.cl_serbatoio)

    print("L'appartamento numero {} ha programmato l'accensione del riscaldamento che comporta un consumo di {} cl di gas".format(casa2.get_nome(), 10))

    try:
        casa2.accendi_riscaldamento(10)
    except ValueError as e:
        print(e)
    if casa2.get_consumi():
        print("Fino a questo momento l'abitazione {} ha consumato {} cl di acqua e {} cl di gas".format(casa2.get_nome(), casa2.get_consumi()[0], casa2.get_consumi()[1]))


if __name__ == "__main__":
    main()

"""
Il programma deve stampare:

Fino a questo momento l'abitazione 11 ha consumato 15 cl di acqua e 0 cl di gas
Fino a questo momento l'abitazione 15 ha consumato 20 cl di acqua e 0 cl di gas

Fino a questo momento l'abitazione 11 ha consumato 15 cl di acqua e 5 cl di gas
Fino a questo momento l'abitazione 15 ha consumato 20 cl di acqua e 5 cl di gas

Fino a questo momento l'abitazione 11 ha consumato 0 cl di acqua e 0 cl di gas
Fino a questo momento l'abitazione 15 ha consumato 20 cl di acqua e 5 cl di gas

Fino a questo momento l'abitazione 15 ha consumato 20 cl di acqua e 9105 cl di gas

Fino a questo momento l'abitazione 11 ha consumato 0 cl di acqua e 885 cl di gas

Numero cl di gas presenti nel serbatoio condominiale: 5
L'appartamento numero 15 ha programmato l'accensione del riscaldamento che comporta un consumo di 10 cl di gas
Attenzione: il serbatoio condominiale e` vuoto
Fino a questo momento l'abitazione 15 ha consumato 20 cl di acqua e 9110 cl di gas
"""
