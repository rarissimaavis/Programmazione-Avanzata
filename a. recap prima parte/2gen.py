"""
Scrivere una funzione che prende in input un intero positivo n e restituisce e produce un generatore degli
interi 0, 1, 3, 6, 10, ... . In altre parole, l’i-esimo elemento e` (0+1+2+...+i-1)
"""


def gen(n):
    sum = 0
    for i in range(n):
        sum += i
        yield sum


for i in gen(5):
    print(i, end=" ")
