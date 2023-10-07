"""
Scrivere la classe MyDictionary che implementa gli operatori di dict riportati di seguito.
MyDictionary deve avere solo una variabile di istanza e questa deve essere di tipo lista.
Per rappresentare le coppie, dovete usare la classe MyPair che ha due variabili di istanza (key e value)
e i metodi getKey, getValue, setKey, setValue.
"""
import collections.abc

class MyDictionary:
    class MyPair:
        def __init__(self, key, value):
            self._key = key
            self._value = value

        def getKey(self):
            return self._key

        def getValue(self):
            return self._value

        def setKey(self, newKey):
            self._key = newKey

        def setValue(self, newValue):
            self._value = newValue


    def __init__(self):
        self._dictionary = list()

    def __getitem__(self, key):
        if not isinstance(key, collections.abc.Hashable):
            raise TypeError("unashable type:", str(type(key)))
        for el in self._dictionary:
            if key == el.getKey():
                return el.getValue()
        raise KeyError(key)

    def __setitem__(self, key, value):
        if not isinstance(key, collections.abc.Hashable):
            raise TypeError("unashable type:", str(type(key)))
        for el in self._dictionary:
            if key == el.getKey():
                el.setValue(value)
                break
        else:
            self._dictionary.append(MyDictionary.MyPair(key, value))

    def __contains__(self, key):
        if not isinstance(key, collections.abc.Hashable):
            raise TypeError("unashable type:", str(type(key)))
        for el in self._dictionary:
            if el.getKey() == key:
                return True
        return False

    def __eq__(self, other):
        if len(self._dictionary) != len(other._dictionary): return False
        for el1 in self._dictionary:
            flag = False
            for el2 in other._dictionary:
                if el1.getKey() == el2.getKey() and el1.getValue() == el2.getValue():
                    flag = True
                    break
        return flag

    def __delitem__(self, key):
        for el in self._dictionary:
            if el.getKey() == key:
                self._dictionary.remove(el)
                return
        raise KeyError(key)

    def __str__(self):
        if not self._dictionary: return "{}"
        outputDict = "{"
        for el in self._dictionary:
            key = el.getKey()
            value = el.getValue()
            outputDict += f"'{key}': {value}, "
        outputDict = outputDict[:-2]
        outputDict += "}"
        return outputDict




