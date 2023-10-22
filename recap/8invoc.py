"""
Scrivere una classe che contiene un metodo che restituisce il numero di invocazioni degli altri metodi della classe.
Il codice dei suddetti metodi non deve essere modificato.
"""


class MyClass:
    count = 0

    def __getattribute__(self, item):
        if callable(super(MyClass, self).__getattribute__(item)):
            MyClass.count += 1
        return super(MyClass, self).__getattribute__(item)

    def m1(self):
        pass

    def m2(self):
        pass


c = MyClass()
c.m1()
c.m2()
c.m2()
print(c.count)

