"""
Scrivere il decoratore di classe decoraClasse che trasforma la classe in una classe di cui può esistere al più n istanze.
Se si tenta di creare più istanze della classe decorata si ha un RuntimeError
"""


def decN(n):
    def decoraClasse(cls):
        cls.numInstances = 0
        cls.__oldInit__ = cls.__init__

        def __newInit__(self, *args, **kwargs):
            if cls.numInstances == n:
                raise RuntimeError
            else:
                cls.numInstances += 1
                cls.__oldInit__(self, *args, **kwargs)

        cls.__init__ = __newInit__
        return cls
    return decoraClasse


@decN(n=2)
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
try:
    c = MyClass(4)
    print("terza istanza", c.value)
except RuntimeError:
    print("no terza istanza")
