"""
Scrivere la classe MyString che crea stringhe tutte di lettere maiuscole
"""


class MyString(str):
    #per semplicità assumiamo che __init__ prenda in input una sequenza
    def __new__(cls, s):
        st = []
        for c in s:
            st += c.capitalize()

        obj = super(MyString, cls).__new__(cls, st)
        return obj


s = MyString(["a", "b"])

print(s)
