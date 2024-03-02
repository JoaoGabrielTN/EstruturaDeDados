class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
    def setNext(self, value):
        self.next = Node(value)
