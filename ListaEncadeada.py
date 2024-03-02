from Node import Node
class ListaEncadeada:
    def __init__(self):
        self.head = None

    def insert(self, value) -> None:
        if self.isEmpty():
            self.head = Node(value)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(value)

    def isEmpty(self):
        return self.head is None
    
    def run(self) -> None:
        node = self.head
        while(node is not None):
            print(node.value)
            node = node.next
