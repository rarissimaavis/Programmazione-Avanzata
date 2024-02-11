"""
Scrivere un decorator factory DecoratorFactF che prende in input un valore v e restituisce un decoratore di funzione
che modifica il comportamento della funzione decorata come segue:
• se la funzione è invocata con tutti gli argomenti di tipo uguale a quello di v allora la funzione restituisce lo
  stesso valore che avrebbe restituito la funzione originaria;
• se uno o piu` argomenti sono di tipo diverso da quello di v allora la funzione restituisce il valore che la funzione
  originaria avrebbe restituito se fosse stata invocata solo su tutti gli argomenti dello stesso tipo di v;
• se la funzione originaria lancia un’eccezione, questa deve essere lanciata anche dalla funzione decorata.
"""
from functools import wraps


def DecoratorFactF(v):
    def dec(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if all(isinstance(arg, type(v)) for arg in args) and all(
                    isinstance(kwarg, type(v)) for kwarg in kwargs.values()):
                return f(*args, **kwargs)
            else:
                new_args = [arg for arg in args if isinstance(arg, type(v))]
                new_kwargs = {key: value for key, value in kwargs.items() if isinstance(value, type(v))}
                try:
                    return f(*new_args, **new_kwargs)
                except Exception as e:
                    raise e

        return wrapper

    return dec


if __name__ == "__main__":

    def funct(x, y, z=3, **kwargs):
        l = [v for k, v in kwargs.items()]
        return [x, y, z] + l


    def funzione(*args, **kwargs):
        l = [v for k, v in kwargs.items()]
        return list(args) + l


    functInt = DecoratorFactF(1)(funct)
    functTuple = DecoratorFactF((2, 3))(funct)
    functList = DecoratorFactF([1, 2, 3])(funct)

    funzioneInt = DecoratorFactF(1)(funzione)
    funzioneTuple = DecoratorFactF((2, 3))(funzione)
    funzioneList = DecoratorFactF([1, 2, 3])(funzione)

    print("Invoco functInt(100,200,k1=10,k2=11)")
    try:
        print(functInt(100, 200, k1=10, k2=11))
    except TypeError as e:
        print(e)
    print("Invoco funct sullo stesso input")
    try:
        print(funct(100, 200, k1=10, k2=11))
    except TypeError as e:
        print(e)

    print("\nInvoco functTuple(100,200,k1=10,k2=11)")
    try:
        print(functTuple(100, 200, k1=10, k2=11))
    except TypeError as e:
        print(e)
    print("Invoco funct sullo stesso input")
    try:
        print(funzione(100, 200, k1=10, k2=11))
    except TypeError as e:
        print(e)

    print("\nInvoco functList([100],[200,5],k1=[10,6],k2=11)")
    try:
        print(functList([100], [200, 5], k1=[10, 6], k2=11))
    except TypeError as e:
        print(e)
    print("Invoco funzione sullo stesso input")
    try:
        print(funct([100], [200, 5], k1=[10, 6], k2=11))
    except TypeError as e:
        print(e)

    print("\nInvoco functInt(100,(2,),k1=10,k2=11)")
    try:
        print(functInt(100, (2,), k1=10, k2=11))
    except TypeError as e:
        print(e)
    print("Invoco funct sullo stesso input")
    try:
        print(funct(100, (2,), k1=10, k2=11))
    except TypeError as e:
        print(e)

    print("\nInvoco functInt(100,200,k1=10,k2=11,**{\'k3\':(5,8),\'k4\':\'op\',\'k5\':8})")
    try:
        print(functInt(100, 200, k1=10, k2=11, **{'k3': (5, 8), 'k4': "op", 'k5': 8}))
    except TypeError as e:
        print(e)
    print("Invoco funct sullo stesso input")
    try:
        print(funct(100, 200, k1=10, k2=11, **{'k3': (5, 8), 'k4': "op", 'k5': 8}))
    except TypeError as e:
        print(e)

    print("\nInvoco funzioneInt(100,200,k1=10,k2=11)")
    try:
        print(funzioneInt(100, 200, k1=10, k2=11))
    except TypeError as e:
        print(e)
    print("Invoco funzione sullo stesso input")
    try:
        print(funzione(100, 200, k1=10, k2=11))
    except TypeError as e:
        print(e)

    print("\nInvoco funzioneTuple(100,200,k1=10,k2=11)")
    try:
        print(funzioneTuple(100, 200, k1=10, k2=11))
    except TypeError as e:
        print(e)
    print("Invoco funzione sullo stesso input")
    try:
        print(funzione(100, 200, k1=10, k2=11))
    except TypeError as e:
        print(e)

    print("\nInvoco funzioneList([100],[200,5],k1=[10,6],k2=11)")
    try:
        print(funzioneList([100], [200, 5], k1=[10, 6], k2=11))
    except TypeError as e:
        print(e)
    print("Invoco funzione sullo stesso input")
    try:
        print(funzione([100], [200, 5], k1=[10, 6], k2=11))
    except TypeError as e:
        print(e)

    print("\nInvoco funzioneInt(100,(2,),k1=10,k2=11)")
    try:
        print(funzioneInt(100, (2,), k1=10, k2=11))
    except TypeError as e:
        print(e)
    print("Invoco funzione sullo stesso input")
    try:
        print(funzione(100, (2,), k1=10, k2=11))
    except TypeError as e:
        print(e)

    print("\nInvoco funzioneInt(100,200,k1=10,k2=11,**{\'k3\':(5,8),\'k4\':\'op\',\'k5\':8})")
    try:
        print(funzioneInt(100, 200, k1=10, k2=11, **{'k3': (5, 8), 'k4': "op", 'k5': 8}))
    except TypeError as e:
        print(e)
    print("Invoco funzione sullo stesso input")

    try:
        print(funzione(100, 200, k1=10, k2=11, **{'k3': (5, 8), 'k4': "op", 'k5': 8}))
    except TypeError as e:
        print(e)

"""Il programma deve stampare:
Invoco functInt(100,200,k1=10,k2=11)
[100, 200, 3, 10, 11]
Invoco funct sullo stesso input
[100, 200, 3, 10, 11]

Invoco functTuple(100,200,k1=10,k2=11)
funct() missing 2 required positional arguments: 'x' and 'y'
Invoco funct sullo stesso input
[100, 200, 10, 11]

Invoco functList([100],[200,5],k1=[10,6],k2=11)
[[100], [200, 5], 3, [10, 6]]
Invoco funzione sullo stesso input
[[100], [200, 5], 3, [10, 6], 11]

Invoco functInt(100,(2,),k1=10,k2=11)
funct() missing 1 required positional argument: 'y'
Invoco funct sullo stesso input
[100, (2,), 3, 10, 11]

Invoco functInt(100,200,k1=10,k2=11,**{'k3':(5,8),'k4':'op','k5':8})
[100, 200, 3, 10, 11, 8]
Invoco funct sullo stesso input
[100, 200, 3, 10, 11, (5, 8), 'op', 8]

Invoco funzioneInt(100,200,k1=10,k2=11)
[100, 200, 10, 11]
Invoco funzione sullo stesso input
[100, 200, 10, 11]

Invoco funzioneTuple(100,200,k1=10,k2=11)
[]
Invoco funzione sullo stesso input
[100, 200, 10, 11]

Invoco funzioneList([100],[200,5],k1=[10,6],k2=11)
[[100], [200, 5], [10, 6]]
Invoco funzione sullo stesso input
[[100], [200, 5], [10, 6], 11]

Invoco funzioneInt(100,(2,),k1=10,k2=11)
[100, 10, 11]
Invoco funzione sullo stesso input
[100, (2,), 10, 11]

Invoco funzioneInt(100,200,k1=10,k2=11,**{'k3':(5,8),'k4':'op','k5':8})
[100, 200, 10, 11, 8]
Invoco funzione sullo stesso input
[100, 200, 10, 11, (5, 8), 'op', 8]
"""
