from Node import Node
from functools import lru_cache
import reprlib
class Linked_list:

    def __init__(self, val):
        self.__head = val

    @property
    def head(self):
        return self.__head
    
    @head.setter
    def head(self, new_head):
        self.__head = new_head
    
    def __bool__(self) -> bool:
        return bool(self.head)

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode.value                         # Para que serve o yield?
            currNode = currNode.next

    def __str__(self) -> str:
        components = reprlib.repr(tuple(self))           # Estou passando todos elementos da LinkedList para uma tupla.
        return 'Linked_list({})'.format(components)      # creio que não haja nenhum forma mais eficiente.

    def __eq__(self, other) -> bool:
        return tuple(self) == tuple(other)

    def insert(self, value) -> None:
        if self.isEmpty():
            self.head = Node(value)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(value)

    def isEmpty(self) -> bool:
        return self.head is None
    
    def run(self) -> None:
        node = self.head
        while(node is not None):
            print(node.value)
            node = node.next
