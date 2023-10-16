"""
Scrivere la classe MyString che crea strimhje tutte di lettere maiuscole
"""


class MyString(str):

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj = obj.upper()
        return obj


s = MyString("ao 123 prova")

print(s)
