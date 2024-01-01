"""
Scrivere un decoratore di classe che, se applicato ad una classe, la modifica in modo che funzioni
come se fosse stata derivata dalla seguente classe base.
N.B. le classi derivate da ClasseBase non hanno bisogno di modificare i metodi f() e g() e la variabile varC.
Inoltre quando vengono create le istanze di una classe derivata queste ’’nascono’’ con lo stesso valore
di varI settato da __init__ di ClasseBase.
"""


def ClasseBaseDecorator(classe):
    classe.varC = 1000
    oldInit = classe.__init__

    def __newInit__(self, *args, **kwargs):
        oldInit(self, *args, **kwargs)
        self.varI = 10

    def f(self, v):
        print(f"{v} * {self.varI} =", v * self.varI)

    @staticmethod
    def g(x):
        print(f"{x} * {classe.varC} =", x * classe.varC)

    classe.__init__ = __newInit__
    classe.f = f
    classe.g = g
    return classe


@ClasseBaseDecorator
class MyClass:
    pass


c = MyClass()
c.f(3)
MyClass.g(3)
