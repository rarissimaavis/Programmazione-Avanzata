"""
Esercizio: Scrivere la classe ClasseB che ha il metodo di istanza contaVarClasse(self,t,n) che
    – prende in input un tipo t e un intero n
    – restituisce il numero di variabili di classe di tipo t delle prime n classi nella gerarchia formata dalla classe
    di cui self e` istanza e dalle sue superclassi, le prime n secondo l’ordine indicato in __mro__ .
    Se il numero di classi nella suddetta gerarchia è minore di n allora vengono considerate tutte le classi della gerarchia.
"""

class ClasseB:
    def contaVarClasse(self, t, n):
        mro = type(self).__mro__
        count = 0
        for cls in mro[:n]:
            if hasattr(cls, '__dict__'):
                count += sum(1 for nome, tipo in vars(cls).items() if isinstance(tipo, t) and not (nome.startswith('__') and nome.endswith('__')))
        return count


class A(ClasseB):
    a = 3


class B(A):
    b = "b"


class C(B):
    c = [1, 2, 3]


class D(C):
    d = "d"
    e = 3


obj = D()
tipo = int
n = 3
count = obj.contaVarClasse(tipo, n)
print(f"Numero di variabili di classe di tipo {tipo} nelle prime {n} classi: {count}")

