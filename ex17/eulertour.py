# versione modificata del codice presente su github (Copyright 2013, Michael H. Goldwasser)
# per essere usato nel libro:
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013

# visita generica, che per poter essere specializzata ha 3 metodi ausiliari
# a seconda della visita che voglio fare implemento uno o più di questi metodi

from linked_binary_tree import LinkedBinaryTree


# anche se non utilizza il concetto di classe astratta è comunque un template method

class BinaryEulerTour:
    # lega la classe BET a un particolare albero di cui si vuole fare la visita
    def __init__(self, tree):
        self._tree = tree

    def tree(self):
        return self._tree

    def execute(self):
        if len(self._tree) > 0:
            return self._tour(self._tree.root())

    # non sa ancora cosa deve fare, invocherà uno o più metodi che non fanno niente -> template method
    def _tour(self, p):
        results = [None, None]
        self._previsit(p)
        if self._tree.left(p) is not None:
            results[0] = self._tour(self._tree.left(p))
        self._invisit(p)
        if self._tree.right(p) is not None:
            results[1] = self._tour(self._tree.right(p))
        answer = self._postvisit(p, results)
        return answer

    def _invisit(self, p):
        pass

    def _previsit(self, p):
        pass

    def _postvisit(self, p, results):
        pass


# stampa degli elementi secondo l'ordine di una visita inorder
class InorderPrint(BinaryEulerTour):
    def _invisit(self, p):
        print(p.element(), end=" ")


class SumPostorder(BinaryEulerTour):
    def _postvisit(self, p, results):
        res = p.element()

        if results[0]: res += results[0]
        if results[1]: res += results[1]
        return res


tree = LinkedBinaryTree()

root = tree._add_root(1)
lroot = tree._add_left(root, 2)
llroot = tree._add_left(lroot, 3)
rlroot = tree._add_right(lroot, 4)
rroot = tree._add_right(root, 5)
lrroot = tree._add_left(rroot, 6)

print("\nStampiamo gli elementi dell'albero nell'ordine in cui vengono visitati da una inorder:")
I = InorderPrint(tree)
I.execute()
print("\nOra sommiamo gli elementi dell'albero:")
S = SumPostorder(tree)
print(S.execute())
