"""
Scrivere una classe MyProxy che è il proxy della classe MyClass. Ogni volta che viene invocato un metodo di
istanza della classe MyProxy, di fatto viene invocato l’omonimo metodo di istanza di MyClass.

NON deve essere usata l’ereditarietà.
Si assuma che __init__ di MyClass prenda in input unn argomento x e che il comportamento dei suoi
metodi di istanza dipenda dal valorie di x passati a __init__
"""


class MyClass:
    def __init__(self, a):
        self.a = a

    def meth(self):
        print("ao", self.a)


class MyProxy:
    def __init__(self, a):
        self._myClass = MyClass(a)

    def __getattr__(self, name):
        try:
            return getattr(self._myClass, name)
        except AttributeError:
            pass


p = MyProxy(3)
p.meth()
