from typing import Any

class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def node(self, at: int) -> Node:
        curr = self.head
        for i in range(at):
            if curr is None:
                raise IndexError("Linked list index out of range")
            curr = curr.next
        return curr

    def insert(self, value: Any, after: Node) -> None:
        new_node = Node(value)
        new_node.next = after.next
        after.next = new_node

    def pop(self):
        while self.head is not None:
            self.head = self.head.next
            return

    def remove_last(self):
        temp = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next
        prev.next = None

    def remove(self, after):
        temp = self.head
        i = 0
        while i < after:
            temp = temp.next
            i = i + 1
        temp.next = temp.next.next


    def print_list(self) -> None:
        lista = []
        temp = self.head
        while temp is not None:
            lista.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(lista))

    def len(self):
        temp = self.head
        dlu = 1
        if self.head is None:
            dlu = 0
            return dlu
        while temp.next is not None:
            temp = temp.next
            dlu += 1
        return dlu

l = LinkedList()
l.append(6)
l.append(7)
l.append(8)
l.append(30)
l.print_list()
print("Push: 20")
l.push(20)
l.print_list()
print("pop: usuwa 20")
l.pop()
l.print_list()
print("remove: usuwa po 0")
l.remove(0)
l.print_list()
print("insertuje 3 po wybranym nodzie")
node = l.node(1)
l.insert(3, node)
l.print_list()
print("remove last")
l.remove_last()
l.print_list()
print("dlugosc listy:", l.len())
