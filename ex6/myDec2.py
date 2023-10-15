"""
Scrivere un decoratore di classe myDecorator che dota la classe decorata di un metodo di istanza contaVarClasse che
prende in input un tipo t e restituisce il numero di variabili di classe di tipo t della classe.
"""


def myDecorator(cls):
    def contaVarClasse(self, t):
        count = 0
        for name, value in vars(cls).items():
            if isinstance(value, t) and not (name.startswith('__') and name.endswith('__')):
                count += 1

        return count

    cls.contaVarClasse = contaVarClasse
    return cls


@myDecorator
class myClass:
    var1 = 10.1
    var2 = "Hello"
    var3 = 3.2
    var4 = "World"
    var5 = 20


obj = myClass()
print(obj.contaVarClasse(int))
print(obj.contaVarClasse(str))
