"""
Scrivere un decorator factory che genera un decoratore di classe che dota la classe di un metodo statico che restituisce
il numero di invocazioni del metodo passato come parametro al decorator factory.
"""


def decFact(method):
    def dec(cls):
        cls.count = 0
        oldMethod = getattr(cls, method)

        def newMethod(*args, **kwargs):
            cls.count += 1
            return oldMethod(*args, **kwargs)

        setattr(cls, method, newMethod)
        @staticmethod
        def nTimes():
            return cls.count
        setattr(cls, "nTimes", nTimes)
        return cls

    return dec


@decFact("ao")
class MyClass:
    def ao(self):
        print("ao")


c = MyClass()
c.ao()
c.ao()
print(c.nTimes())
