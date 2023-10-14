# versione che si spacca (RecursionError)

def count(aClass):
    aClass.numInstances = 0

    def __newInit__(self, *args, **kwargs):
        aClass.numInstances += 1
        aClass.__init__(self, *args, **kwargs)

    aClass.__init__ = __newInit__
    return aClass


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
print("spam", spam.numInstances)
print("sub", sub.numInstances)
print("other", other.numInstances)
other = Other()
print("other", other.numInstances)
print("spam", spam.numInstances)
print("sub", sub.numInstances)
