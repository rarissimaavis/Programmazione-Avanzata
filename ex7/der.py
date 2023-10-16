"""
Scrivere un decoratore di classe che, se applicato ad una classe, la modifica in modo che funzioni
come se fosse stata derivata dalla seguente classe base.
N.B. le classi derivate da ClasseBase non hanno bisogno di modificare i metodi f() e g() e la variabile varC.
Inoltre quando vengono create le istanze di una classe derivata queste ’’nascono’’ con lo stesso valore
di varI settato da __init__ di ClasseBase.
"""


class ClasseBase:
    varC = 1000

    def __init__(self):
        self.varI = 10

    def f(self, v):
        print(f"{v} * {self.varI} =", v * self.varI)

    @staticmethod
    def g(x):
        print(f"{x} * {ClasseBase.varC} =",x * ClasseBase.varC)


def dec(cls):
    cls.__init__ = ClasseBase.__init__
    cls.varC = ClasseBase.varC
    cls.f = ClasseBase.f
    cls.g = staticmethod(ClasseBase.g)
    return cls


@dec
class MyClass:
    pass


c = MyClass()
c.f(3)
MyClass.g(3)
