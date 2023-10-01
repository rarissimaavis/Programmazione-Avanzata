class LinkedList:
    class Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def add_head(self, element):
        newNode = self.Node(element, self._head)
        if self._size == 0:
            self._tail = newNode
        self._head = newNode
        self._size += 1

    def add_tail(self, element):
        newNode = self.Node(element, None)
        if self._size == 0:
            self._head = newNode
        else:
            self._tail._next = newNode
        self._tail = newNode
        self._size += 1

    def __len__(self):
        return self._size

    def __getitem__(self, j):
        cnt = 0
        if j < 0: j = self._size + j
        if j < 0 or j >= self._size:
            raise IndexError()
        current = self._head
        while current is not None:
            if cnt == j:
                return current._element
            else:
                current = current._next
                cnt += 1

    def __str__(self):
        toReturn = '<'
        current = self._head
        while current is not None:
            toReturn += str(current._element)
            current = current._next
            if current is not None:
                toReturn += ', '
        toReturn += '>'
        return toReturn
