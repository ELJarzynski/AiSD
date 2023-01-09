from typing import Any
from linkedlist import *

class Stack:
    def __init__(self) -> None:
        self.storage = LinkedList()

    def push(self, element: Any) -> None:
        self.storage.append(element)

    def pop(self) -> Any:
        self.storage.pop()

    def print_list(self) -> None:
        temp = self.storage.head
        while temp:
            if temp.next is not None:
                print(temp.data)
            else:
                print(temp.data)
            temp = temp.next

    def len(self):
        temp = self.storage.head
        leng = 0
        while temp is not None:
            temp = temp.next
            leng += 1
        return leng

# stos = Stack()
# stos.push(4)
# stos.push(5)
# stos.push(6)
# stos.print_list()
# print("Długość stosu: ", stos.len())
