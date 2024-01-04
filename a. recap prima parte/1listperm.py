"""
Scrivere una funzione che prende in input una lista L e restituisce una lista di |L|! liste in cui ciascuna
lista contiene una diversa permutazione degli elementi della lista input L
"""


def listPerms(L):
    if len(L) == 0:
        return [L]
    perms = []
    for i in range(len(L)):
        first = [L[i]]
        rest = L[:i] + L[i + 1:]
        for perm in listPerms(rest):
            perms.append(first + perm)
    return perms


L = [1, 2, 3]
res = listPerms(L)
for perm in res:
    print(perm)
