"""
Scrivere nel file esercizio2.py la classe Useless le cui istanze vengono create in modo da
essere identiche all'ultimo oggetto di tipo Prototype creato dal programma (identiche vuol
dire che hanno esattamente gli stessi attributi e che ciascun attributo ha lo stesso valore in
tutte le istanze identiche tra loro). Ad esempio, se il programma crea due istanze prot1 e
prot2 di Prototype allora tutte le istanze di Useless create dopo la creazione di prot1 e
prima di quella di prot2 saranno identiche a prot1 mentre tutte quelle create dopo la
creazione di prot2 saranno identiche a prot2. Se quando viene creata un'istanza di Useless
non e` stata ancora creata ancora un'istanza di Prototype allora le istanze di Useless
vengono create "normalmente", cioe` ognuna ha i propri attributi che potrebbero essere
diversi da quelli delle altre istanze.
• La classe Useless NON deve avere un suo metodo __init__ .
• La classe Prototype e` gia` scritta nel file esercizio2.py e ovviamente non deve
essere modificata. La classe Prototype fornisce il metodo getLastInstance() che
puo` essere convenientemente usato per implementare la classe Useless.
"""


class Prototype:
    __lastInstance__ = None

    def __init__(self, a):
        self.var = a
        Prototype.__lastInstance__ = self

    @staticmethod
    def getLastInstance():
        return Prototype.__lastInstance__


class Useless:
    def __new__(cls, *args, **kwargs):
        obj = super(cls, cls).__new__(cls, *args, **kwargs)
        if Prototype.getLastInstance() is not None:
            obj.__dict__ = Prototype.getLastInstance().__dict__
        return obj


print("Creo due istanze di Useless senza aver creato prima un'istanza di Prototype")
diversa1 = Useless()
diversa2 = Useless()
diversa1.x = "20"
diversa2.x = "30"
diversa1.f = lambda z: z + 3
print("la variabile x di diversa1 e` {} mentre quella di diversa2 e` {}".format(diversa1.x, diversa2.x))
print("invoco diversa1.f(4) e ottengo", diversa1.f(4))
print("invoco diversa2.f(3) e viene stampato:")
try:
    diversa2.f(3)
except AttributeError as e:
    print(e)

print("\nCreo l'istanza prot1 di Prototype e subito dopo l'istanza usel1 di useless")
prot1 = Prototype('100')
usel1 = Useless()
print("Verifico che prot1 e usel1 non sono lo stesso oggetto")
if prot1 is not usel1:
    print("Tutto ok: prot1 e usel1 non sono lo stesso oggetto")
else:
    print("C'e` un problemaL prot1 e usel1 sono lo stesso oggetto")

try:
    v = usel1.var
    if v == prot1.var:
        print("prot1 e usel1 hanno entrambe la variabile var e il valore di questa variabile e` ", prot1.var)
    else:
        print(
            "C'e` un problema: prot1 e usel1 hanno entrambe la variabile var ma il valore di var di prot1 e` {} e quello di usel1 e`{} ".format(
                prot1.var, usel1.var))
except AttributeError:
    print("C'e` un problema: usel1 non ha la variabile var")

print("modifico il valore della variabile var di prot1")
usel1.var = "pop"
try:
    v = usel1.var
    if v == prot1.var:
        print("prot1 e usel1 hanno entrambe la variabile var e il valore di questa variabile e` ", prot1.var)
    else:
        print(
            "C'e` un problema: prot1 e usel1 hanno entrambe la variabile var ma il valore di var di prot1 e` {} e quello di usel1 e`{} ".format(
                prot1.var, usel1.var))
except AttributeError:
    print("C'e` un problema: usel1 non ha la variabile var")

print("aggiungo la variabile newvar a usel1")
usel1.newvar = "carla"
try:
    v = prot1.newvar
    if v == usel1.newvar:
        print("prot1 e usel1 hanno entrambe la variabile newvar e il valore di questa variabile e` ", prot1.newvar)
except AttributeError:
    print("C'e` un problema: usel1 non ha la variabile newvar")

print("\nCreo l'istanza prot2 di Prototype e subito dopo l'istanza usel2 di useless")
prot2 = Prototype('5')
usel2 = Useless()

try:
    v = usel2.var
    if v == prot2.var:
        print("prot2 e usel2 hanno entrambe la variabile var il valore di questa variabile e` ", prot2.var)
    else:
        print(
            "C'e` un problema: prot2 e usel2 hanno entrambe la variabile var ma il valore di var di prot2 e` {} e quello di usel2 e`{} ".format(
                prot2.var, usel2.var))
except AttributeError:
    print("C'e` un problema: usel2 non ha la variabile var")

print("modifico il valore della variabile var di prot2")
try:
    v = usel2.var
    if v == prot2.var:
        print("prot2 e usel2 hanno entrambe la variabile var e il valore di questa variabile e`", prot2.var)
    else:
        print(
            "C'e` un problema: prot2 e usel2 hanno entrambe la variabile var ma il valore di var di prot2 e` {} e quello di usel2 e`{} ".format(
                prot2.var, usel2.var))
except AttributeError:
    print("C'e` un problema: usel2 non ha la variabile var")

print("aggiungo la variabile newnewvar a usel2")
usel2.newnewvar = "anna"
try:
    v = prot2.newnewvar
    if v == usel2.newnewvar:
        print("prot2 e usel2 hanno entrambe la variabile newnewvar e il valore di questa variabile e` ",
              prot2.newnewvar)
except AttributeError:
    print("C'e` un problema: usel2 non ha la variabile newnewvar")

try:
    usel1.newnewvar
except AttributeError:
    print("\nusel1 non ha newnewvar ed e` giusto cosi`")

try:
    usel2.newvar
except AttributeError:
    print("usel2 non ha newvar ed e` giusto cosi`")

if prot1.var != usel2.var:
    print("Tutto ok: i valori della variabile di istanza var di prot1 e usel2 sono diversi")
else:
    print("c'e` un problema")

"""Il programma deve stampare:

Creo due istanze di Useless senza aver creato prima un'istanza di Prototype
la variabile x di diversa1 e` 20 mentre quella di diversa2 e` 30
invoco diversa1.f(4) e ottengo 7
invoco diversa2.f(3) e viene stampato:
'Useless' object has no attribute 'f'

Creo l'istanza prot1 di Prototype e subito dopo l'istanza usel1 di useless
Verifico che prot1 e usel1 non sono lo stesso oggetto
Tutto ok: prot1 e usel1 non sono lo stesso oggetto
prot1 e usel1 hanno entrambe la variabile var e il valore di questa variabile e`  100
modifico il valore della variabile var di prot1
prot1 e usel1 hanno entrambe la variabile var e il valore di questa variabile e`  pop
aggiungo la variabile newvar a usel1
prot1 e usel1 hanno entrambe la variabile newvar e il valore di questa variabile e`  carla

Creo l'istanza prot2 di Prototype e subito dopo l'istanza usel2 di useless
prot2 e usel2 hanno entrambe la variabile var il valore di questa variabile e`  5
modifico il valore della variabile var di prot2
prot2 e usel2 hanno entrambe la variabile var e il valore di questa variabile e` 5
aggiungo la variabile newnewvar a usel2
prot2 e usel2 hanno entrambe la variabile newnewvar e il valore di questa variabile e`  anna

usel1 non ha newnewvar ed e` giusto cosi`
usel2 non ha newvar ed e` giusto cosi`
Tutto ok: i valori della variabile di istanza var di prot1 e usel2 sono diversi


"""
