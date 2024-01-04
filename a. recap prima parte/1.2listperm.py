"""
Scrivere una funzione che prende in input una lista L e restituisce una lista di |L|! liste in cui ciascuna
lista contiene una diversa permutazione degli elementi della lista input L
"""
import itertools


def listPerms(L):
    perms = list(itertools.permutations(L))
    return [list(perm) for perm in perms]


L = [1, 2, 3]
res = listPerms(L)
for perm in res:
    print(perm)
