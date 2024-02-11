"""
Scrivere una classe che permetta di usare una lista in uno statement with
"""


class WithLista(list):
    def __init__(self, lista):
        self.lista = lista

    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self):
        self.file.close()
