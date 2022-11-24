from typing import Any, List, Callable

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value):
        self.value = value
        self.left_child= None
        self.right_child = None

    def is_leaf(self) -> bool:
        if len(self.left_child) == 0 or len(self.right_child) == 0:
            return False
        return True

    def add_left_child(self, value: Any):
        if value == self.value:
            return
        if value < self.value:
            if self.left_child:
                self.left_child(value)
            else:
                self.left_child = BinaryTree(value)

    def add_right_child(self, value: Any):
        if value == self.value:
            return
        if value > self.value:
            if self.right_child:
                self.right_child(value)
            else:
                self.right_child = BinaryTree(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child:
            self.left_child.traverse_in_order(visit)
        visit(self)

        if self.right_child:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child:
            self.left_child.traverse_in_order(visit)

        if self.right_child:
            self.right_child.traverse_in_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if len(self.left_child)>0:
            for left_child in self.left_child:
                left_child.traverse_in_order(visit)

        if len(self.right_child)>0:
            for right_child in self.right_child:
                right_child.traverse_in_order(visit)


    def print(self)->None:
        print(self.value)

        if len(self.children) != 0:
            for child in self.children:
                child.print()

class BinaryTree:
    root: BinaryNode

    def __init__(self, value: Any):
        self.root = BinaryTree(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_pre_order(self, visit: Callable[['TreeNode'], None]) -> None:
        if self.root != None:
            self.traverse_pre_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.root != None:
            self.traverse_post_order(visit)

    def show(self):
        print(self.root)
        if self.root.left_child is not None:
            print()

tree = BinaryTree(10)
tree.root.add.left_child(2)


