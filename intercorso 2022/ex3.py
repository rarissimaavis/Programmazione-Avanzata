"""
Scrivere nel file esercizio3.py un decorator factory decFact(L1,L2) che prende come
argomenti una lista L1 di stringhe e una lista L2 di oggetti e produce un decoratore di
classe che fa in modo che le istanze della classe nascano non solo con le variabili di istanza
aggiunte dal metodo __init__ della classe ma anche con le seguenti variabili di istanza:
• per ogni i =0,..., len(L1)-1, una variabile con nome uguale a L1[i] e valore uguale a
L2[i]. Nel caso in cui il metodo __init__ della classe originaria aggiunge gia` una
variabile di istanza con lo stesso nome di una di quelle aggiunte dal decoratore
allora il valore della variabile deve essere quello assegnato da __init__ della classe
originaria.
• potete assumere che le due liste L1 e L2 abbiano la stessa lunghezza.
"""


def decFact(L1, L2):
    def dec(cls):
        cls.oldInit = cls.__init__

        def newInit(self, *args, **kwargs):
            for v, x in zip(L1, L2):
                setattr(self, v, x)
            cls.oldInit(self, *args, **kwargs)

        cls.__init__ = newInit
        return cls

    return dec


@decFact(["var1", "var2", "var3", "var4"], ["valore1", "valore2", [100, 21], 12])
class C1:
    def __init__(self, v1, v2, v3):
        self.x1 = v1
        self.x2 = v2
        self.x3 = v3


@decFact(["var1", "var2", "var3"], ["valore1", "valore2", {"y": 4}])
class C2:
    def __init__(self, *args):
        if len(args) < 3:
            print("numero errato di argomenti")
        else:
            self.var1 = args[0]
            self.x1 = args[1]
            self.x2 = args[2]


if __name__ == "__main__":
    print("""In questo primo test i nomi della prima lista passata al decorator factory sono tutti diversi da quelli
delle  variabili di istanza aggiunte da __init__ di C1.""")
    print("Creo l'istanza c di C1.")
    c = C1('a', 'b', 10)
    print(
        "Queste sono le variabili dell'istanza c di C1: c.x1={},c.x2={},c.x3={},c.var1={},c.var2={},c.var3={},c.var4={}.". \
        format(c.x1, c.x2, c.x3, c.var1, c.var2, c.var3, c.var4))

    print("""\nIn questo secondo test, nella prima lista passata al decorator factory e` presente il nome \"var1\"  e il
metodo __init__ di C2 aggiunge una variabile di istanza con lo stesso nome.""")
    print("Creo l'esercizio1.py")
    c = C2('a', 'b', 10, 23)
    print("Queste sono le variabili dell'istanza c di C1: c.x1={},c.x2={},c.var1={},c.var2={},c.var3={}.".format(c.x1,
                                                                                                                 c.x2,
                                                                                                                 c.var1,
                                                                                                                 c.var2,
                                                                                                                 c.var3))

"""
Il programma deve stampare:

In questo primo test i nomi della prima lista passata al decorator factory sono tutti diversi da quelli
delle  variabili di istanza aggiunte da __init__ di C1.
Creo l'istanza c di C1.
Queste sono le variabili dell'istanza c di C1: c.x1=a,c.x2=b,c.x3=10,c.var1=valore1,c.var2=valore2,c.var3=[100, 21],c.var4=12.

In questo secondo test, nella prima lista passata al decorator factory e` presente il nome "var1"  e il
metodo __init__ di C2 aggiunge una variabile di istanza con lo stesso nome.
Creo l'esercizio1.py
Queste sono le variabili dell'istanza c di C1: c.x1=b,c.x2=10,c.var1=a,c.var2=valore2,c.var3={'y': 4}.

"""
