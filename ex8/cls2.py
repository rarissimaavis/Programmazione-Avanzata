"""
Scrivere una classe C per cui accade che ogni volta che si aggiunge una variabile di istanza ad una delle
istanze di C in realta` la variabile viene aggiunta alla classe come variabile di classe.

Modificare la classe al punto precedente in modo tale che le istanze abbiano al piu` due variabili di istanza:
varA e varB e non deve essere possibile aggiungere altre variabili di istanza oltre a queste due.
Se il programma avesse bisogno di aggiungere altre variabili oltre a quelle sopra indicate, queste altre
variabili verrebbero create come variabili di classe e non di istanza.
"""


# versione della prof
class C(object):
    __slots__ = {"varA", "varB"}

    def __setattr__(self, nome, valore):
        if nome in C.__slots__: return super(C, self).__setattr__(nome, valore)

        setattr(C, nome, valore)

    def __getattr__(self, nome):
        if nome in C.__slots__: return super(C, self).__getattr__(nome)


"Qui comincia il codice per il test"


class D(C):
    def __init__(self, vz: int, vw: int):
        self.z = vz
        self.w = vw
        self.f = lambda x: vz * x


i1 = C()
i2 = C()
i1.varA = "a"
i2.varA = 4
i1.varB = "b"
i2.varB = 300
i1.x = 6

print("i valori di i1.varA, i1.varB e i1.x sono:", i1.varA, i1.varB, i1.x)
i2.x = 10
print("i valori di i1.varA, i1.varB e i1.x sono:", i1.varA, i1.varB, i1.x)
print("i valori di i2.varA, i2.varB e i2.x sono:", i2.varA, i2.varB, i2.x)
i1.y = 6
print("i valori di i1.varA, i1.varB e i1.y sono:", i1.varA, i1.varB, i1.y)
print("i valori di i2.varA, i2.varB e i2.y sono:", i2.varA, i2.varB, i2.y)
i3 = D(1000, 3000)
print("i valori di i3.z e i3.w sono:", i3.z, i3.w)
print("D.f(6)=", D.f(6))
i4 = D(4000, 8000)
print("i valori di i4.z e i4.w sono:", i4.z, i4.w)
print("i valori di i3.z e i3.w sono:", i3.z, i3.w)
print("D.f(6)=", D.f(6))

"""
Il programma deve stampare:
i valori di i1.varA, i1.varB e i1.x sono: a b 6
i valori di i1.varA, i1.varB e i1.x sono: a b 10
i valori di i2.varA, i2.varB e i2.x sono: 4 300 10
i valori di i1.varA, i1.varB e i1.y sono: a b 6
i valori di i2.varA, i2.varB e i2.y sono: 4 300 6
i valori di i3.z e i3.w sono: 1000 3000
D.f(6)= 6000
i valori di i4.z e i4.w sono: 4000 8000
i valori di i3.z e i3.w sono: 4000 8000
D.f(6)= 24000
"""
