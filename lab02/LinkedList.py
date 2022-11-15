from typing import Any

class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = Node()

    def pop(self):
        temp = self.head
        if temp is not None:
            self.head = temp.next
            temp = None
            return


    def push(self, value: Any) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.head.data is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node


    def node(self, at: int) -> Node:
        temp = self.head
        for x in range(at):
            temp = temp.next
        return temp


    def insert(self, prev_node, new_data):
        if prev_node is None:
            print("Index jest zły")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node


    def len(self):
        temp = self.head
        wynik = 1
        if temp.data == None:
            return 0
            return
        while temp.next != None:
            temp = temp.next
            wynik += 1
        return wynik


    def remove(self, i):
        if self.head.date is None:
            print("zly indeks")
            return
        if i>self.head.data or i<0:
            print("nie miesci sie w skali index")
            return
        if i == 0:
            self.head = self.head.next
            return

        temp = self.head
        ind = 1
        while temp.next != None:
            prev = temp
            temp = temp.next
            if ind == i:
                prev.next = temp.next
                return


    def remove_last(self):
        temp = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        prev.next = None


    def print(self):
        temp = self.head
        while temp:
            if temp.next is None:
                print(temp.data)
            else:
                print(temp.data,"-> ", end="")
            temp = temp.next


class Stack():
    def __init__(self):
        self._storage = LinkedList()
        self.size = 0

    def push(self, element: Any) -> None:
        self._storage.append(element)

    def pop(self) -> Any:
        self._storage.remove_last()

    def print(self):
        temp = self._storage.head
        while temp:
            if temp is None:
                print(temp.data)
            else:
                print(temp.data)
            temp = temp.next


class Queue:
    def __init__(self):
        self._storage = LinkedList()

    def peek(self) -> Any:
        return self._storage.head.data

    def enqueue(self, element: Any) -> None:
        return self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop()

    def print(self):
        temp = self._storage.head
        while (temp):
            if temp.next is None:
                print(temp.data)
            else:
                print(temp.data, ", ", end="")
            temp = temp.next

l = LinkedList()
l2 = LinkedList()
l3 = LinkedList()
for i in range(10):
    l3.append(i)
# dodanie na koniec
l.append(6)
l.append(4)
# dodanie na poczatek
l.push(3)
l.push(7)
l.push(5)
# insertowanie w środek
l.insert(l.head.next, 8)
# wyswietlenie listy 1
l.print()
#wyswietlenie dlugosci list
print(l.len())
print(l2.len())
print(l3.len())
#remove
print("list before removed index ")
l.print()
l.remove_last()
print("list after removed index ")
l.print()

#stos
print("Stos:")
stack = Stack()
stack.push(4)
stack.push(20)
stack.push(5)
stack.print()
print("----")
stack.pop()
stack.push(19)
stack.print()

#kolejka
print("Kolejka:")
queue = Queue()
queue.enqueue("Pierwszy Klient")
queue.enqueue("Drugi Klient")
queue.enqueue("Trzeci Klient")
queue.print()
print(queue.peek())
queue.dequeue()
queue.print()
