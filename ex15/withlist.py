"""
Scrivere una classe che permetta di usare una lista in uno statement with
"""
#versione 1
class Lista_suppCM:
    def __init__(self, listaCM):
        self.l_obj = listaCM

    def __enter__(self):
        return self.l_obj

    def __exit__(self, ty, value, traceback):
        print("Eccezione")
        del self.l_obj
        #continua

