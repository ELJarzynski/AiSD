from linkedlist import *
from typing import Any


class Queue:
    def __init__(self) -> None:
        self.storage = LinkedList()

    def peek(self) -> Any:
        return self.storage.head

    def enqueue(self, element: Any) -> None:
        self.storage.append(element)

    def dequeue(self) -> Any:
        self.storage.pop()

    def print(self) -> None:
        temp = self.storage.head
        while temp:
            if temp.next is not None:
                print(temp.data)
            else:
                print(temp.data)
            temp = temp.next

    def len(self) -> int:
        temp = self.storage.head
        leng = 0
        while temp is not None:
            temp = temp.next
            leng += 1
        return leng


q = Queue()
q.enqueue('klient 1')
q.enqueue('klient 2')
q.enqueue('klient 3')
q.print()
print("Długość stosu: ", q.len())
q.dequeue()
q.print()
print("Długość stosu: ", q.len())
q.dequeue()
q.print()
print("Długość stosu: ", q.len())
q.dequeue()
q.print()
print("Długość stosu: ", q.len())
