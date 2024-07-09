class Node:
    __slots__ = ('__next', '__value')
    def __init__(self, value) -> None:
        self.__value = value
        self.__next = None
    
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def Next(self, value) -> None:
        self.next = Node(value)

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value