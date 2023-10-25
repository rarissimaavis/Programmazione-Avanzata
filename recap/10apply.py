"""
Scrivere una funzione apply(due_things) che prende in input una tupla due_things che contiene tuple della
forma (meth, arg1,arg2,…) dove meth è un metodo di istanza di una certa classe C e arg1, arg2,… sono gli
argomenti diversi da self con cui deve essere invocato meth. Nella prima tupla di due_things, meth è la classe C
e gli argomenti sono quelli da passare al costruttore per creare l’istanza di C su cui invocare i metodi delle
restanti tuple di due_things. La funzione applica restituisce una lista contenente come primo elemento l’istanza
creata e come restanti elementi i valori restituiti dalle invocazioni dei metodi delle restanti tuple.
"""


def apply(due_things):
    toReturn = []
    command = due_things[0]
    func, *args = command
    obj = func(*args)
    for i in range(1, len(due_things)):
        func, *args = due_things[i]
        res = func(obj, *args)
        toReturn.append(res)
        toReturn.insert(0, obj)
    return toReturn


class C:
    def __init__(self, value):
        self.value = value

    def method1(self, arg):
        return f"method1({arg}) called on instance with value {self.value}"

    def method2(self, arg1, arg2):
        return f"method2({arg1}, {arg2}) called on instance with value {self.value}"

    def method3(self, arg1, arg2, arg3):
        return f"method3({arg1}, {arg2}, {arg3}) called on instance with value {self.value}"


two_things = (
        (C, 42),
        (C.method1, "arg1"),
        (C.method2, "arg2.1", "arg2.2"),
        (C.method3, "arg3.1", "arg3.2", "arg3.3"),
    )
results = apply(two_things)
for result in results:
    print(result)


