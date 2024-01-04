from LinkedList import LinkedList
lst = [1, 3, 5, 6]
lista = LinkedList()
for val in lst:
    lista.add_head(val)
print(lista)
if lista:
    print('lista piena')
else:
    print('lista vuota')
print(lista[1])
print(lista[-1])
if 5 in lista:
    print('presente')
else:
    print('assente')
for val in lista:
    print(val, end=' ')
