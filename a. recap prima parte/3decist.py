"""
Definire un decoratore di classe che permette alla classe decorata di contare le sue istanze
"""


def count(cls):
    cls.numInstances = 0
    oldInit = cls.__init__

    def __newInit__(self, *args, **kwargs):
        cls.numInstances += 1
        oldInit(self, *args, **kwargs)

    cls.__init__ = __newInit__
    return cls


@count
class Spam:
    pass


@count
class Sub(Spam):
    pass


@count
class Other(Spam):
    pass


spam = Spam()
sub = Sub()
other = Other()
print("spam: ", spam.numInstances)
print("sub: ", sub.numInstances)
print("other: ", other.numInstances)
other = Other()
print("other: ", other.numInstances)
print("spam: ", spam.numInstances)
