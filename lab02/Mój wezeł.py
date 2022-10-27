from typing import Any

class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def push(self, value: Any) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    
    def insert(self, value: Any, after):
        if after is None:
            print("Index jest zły")
            return

        new_node = Node(value)
        pom = self.head
        i = 0
        while (i < after):
            pom = pom.next
            i = i + 1

        temp = pom.next
        pom.next = new_node
        pom = pom.next
        pom.next = temp


    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return
        last = self.head
        while last.next != None:
            last = last.next
        last.next = new_node


    def len(self):
        if self.head == None:
            return 0
        temp = 1
        while self.head.next != None:
            self.head = self.head.next
            temp += 1
        return temp


    def print(self):
        temp = self.head
        while temp:
            if temp.next is None:
                print(temp.data)
            else:
                print(temp.data, "-> ", end="")
            temp = temp.next



lista = LinkedList()
lista.append(4)
lista.append(11)
lista.append(12)
lista.append(13)
lista.insert(2, 0)
lista.push(3)
lista.print()
print(lista.len())
