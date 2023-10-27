"""
Scrivere il decoratore di classe decoraClasse che trasforma la classe in una classe di cui può esistere al più un'istanza.
Se si tenta di creare più di un'istanza della classe decorata si ha un RuntimeError
"""


def decoraClasse(cls):
    cls.numInstances = 0
    cls.__oldInit__ = cls.__init__

    def __newInit__(self, *args, **kwargs):
        if cls.numInstances == 1:
            raise RuntimeError
        else:
            cls.numInstances = 1
            cls.__oldInit__(self, *args, **kwargs)

    cls.__init__ = __newInit__
    return cls


@decoraClasse
class MyClass:
    def __init__(self, value):
        self.value = value


a = MyClass(2)
print("prima istanza", a.value)
try:
    b = MyClass(3)
    print("seconda istanza", b.value)
except RuntimeError:
    print("no seconda istanza")
