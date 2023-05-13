class SinglyListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class DoublyListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        """ Adiciona um elemento à primeira posição da lista,
            no caso, a head """
        if self.is_empty():
            self.head = SinglyListNode(data)
        else:
            new_node = SinglyListNode(data)
            new_node.next = self.head
            self.head = new_node

    def add_last(self, data):
        """ Adiciona um elemento à última posição da lista """
        if self.is_empty():
            self.head = SinglyListNode(data)

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = SinglyListNode(data)

    def pop(self):
        """ Deleta o último elemento adicionado à lista """
        if self.is_empty():
            print('Lista vazia')
        else:
            self.head = self.head.next

    def show(self):
        """ Mosta todos os elementos da lista """
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def search(self, data):
        """ Recebe um dado qualquer e busca esse dado dentro da lista
            caso a lista esteja vazia, retorna None"""
        if self.is_empty():
            return None
        node = self.head
        while node.data != data:
            node = node.next
        return node


class DoublyLinkedList:
    def __init__(self):
        self.head
