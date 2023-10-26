"""
Scrivere nella classe C, fornita nel file esercizio1.py, un metodo di classe aggiungiProprieta che per ciascuna
variabile di classe di C di tipo str, crea una property con lo stesso nome della variabile.
Il setter della property deve effettuare l’assegnamento solo se il valore da assegnare è una stringa.
In caso contrario deve lanciare TypeError con argomento la stringa “Non e` possibile assegnare {} alla variabile {}”
dove al posto delle parentesi graffe devono comparire il valore e il nome passati al setter.
"""


class C:
    @classmethod
    def aggiungiProprieta(cls):
        for name, value in cls.__dict__.items():
            if isinstance(value, str) and not value.startswith("__"):

                privName = "__" + name

                def getter(self):
                    return getattr(self, privName)

                def setter(self, value):
                    if isinstance(value, str):
                        setattr(self, privName, value)
                    else:
                        raise TypeError(f"Non e` possibile assegnare {value} alla variabile {name}")

                setattr(cls, name, property(getter, setter))


C.x = 2
C.y = "a"
C.z = "b"
C.w = (1, 2)

C.aggiungiProprieta()
c = C()
print("c e` un'istanza della classe C che ha le variabili di classe x di tipo int,y e z di tipo str, e w di dipo tuple")
try:
    c.z = "anna"
    print("c.z={}. Tutto ok.".format(c.z))
except TypeError as e:
    print(e)
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")

try:
    c.x = [1, 2]
    print("c.x={}. Tutto ok.".format(c.x))
except TypeError as e:
    print(e)
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")

try:
    c.y = 3
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")
except TypeError as e:
    print(e, end=' ')
    print("ed e` corretto che sia cosi`")


class D(C):
    n = "u"


print("\nLa classe D ha come classe base C e, oltre alle variabili di classe di D, ha la variabile n di tipo str")
D.aggiungiProprieta()
print("d e` un'istanza della classe D. ")

d = D()
try:
    d.z = "anna"
    print("d.z={}. Tutto ok.".format(d.z))
except TypeError as e:
    print(e)
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")

try:
    d.x = [1, 2]
    print("d.x={}. Tutto ok.".format(d.x))
except TypeError as e:
    print(e)
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")

try:
    d.y = 3
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")
except TypeError as e:
    print(e, end=' ')
    print("ed e` corretto che sia cosi`")

try:
    d.n = 3
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")
except TypeError as e:
    print(e, end=' ')
    print("ed e` corretto che sia cosi`")

print("\nOra assegnamo a D variabili di classe omonime a quelle di C ma con valori diversi")
D.x = "papera"
D.y = 11
D.z = [1, 2, 3]
D.w = "airone"

D.aggiungiProprieta()
d = D()
try:
    d.z = set((1, 4))
    print("d.z={}. Tutto ok.".format(d.z))
except TypeError as e:
    print(e)
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")

try:
    d.x = [1, 2]
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")
except TypeError as e:
    print(e, end=' ')
    print("ed e` corretto che sia cosi`")

try:
    d.w = "pop"
    print("d.w={}. Tutto ok.".format(d.w))
except TypeError as e:
    print(e)
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")

try:
    d.w = 6
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")
except TypeError as e:
    print(e, end=' ')
    print("ed e` corretto che sia cosi`")

try:
    d.n = 3
    print("Attenzione! Qualcosa non va nella soluzione dell'esercizio.")
except TypeError as e:
    print(e, end=' ')
    print("ed e` corretto che sia cosi`")

"""
Il programma deve stampare:
c e` un'istanza della classe C che ha le variabili di classe x di tipo int,y e z di tipo str, e w di dipo tuple
c.z=anna. Tutto ok.
c.x=[1, 2]. Tutto ok.
Non e` possibile assegnare 3 alla variabile y ed e` corretto che sia cosi`

La classe D ha come classe base C e, oltre alle variabili di classe di D, ha la variabile n di tipo str
d e` un'istanza della classe D. 
d.z=anna. Tutto ok.
d.x=[1, 2]. Tutto ok.
Non e` possibile assegnare 3 alla variabile y ed e` corretto che sia cosi`
Non e` possibile assegnare 3 alla variabile n ed e` corretto che sia cosi`

Ora assegnamo a D variabili di classe omonime a quelle di C ma con valori diversi
d.z={1, 4}. Tutto ok.
Non e` possibile assegnare [1, 2] alla variabile x ed e` corretto che sia cosi`
d.w=pop. Tutto ok.
Non e` possibile assegnare 6 alla variabile w ed e` corretto che sia cosi`
Non e` possibile assegnare 3 alla variabile n ed e` corretto che sia cosi`

"""""
