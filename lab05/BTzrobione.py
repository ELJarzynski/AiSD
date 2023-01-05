from typing import Any, Callable
import graphviz


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def is_leaf(self) -> bool:
        if len(self.left_child) == 0 or len(self.right_child) == 0:
            return False
        return True

    def add_left_child(self, value: Any) -> None:
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any) -> None:
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)

        visit(self)

        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)

        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)

        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        visit(self)

        if self.left_child is not None:
            for left_child in self.left_child:
                left_child.traverse_pre_order(visit)

        if self.right_child is not None:
            for right_child in self.right_child:
                right_child.traverse_pre_order(visit)


class BinaryTree:
    root: 'BinaryNode'

    def __init__(self, tree: 'BinaryNode') -> None:
        self.root = tree

    # od lewej na maksa leci
    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    # od korzenia z lewej do prawej
    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_post_order(visit)

    # od lewej do prawej korzen na koncu
    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)


f = print


def print(adres: 'TreeNode') -> None:
    if isinstance(adres, BinaryNode):
        f(adres.value)
    else:
        f(adres)


def main():
    tree_binarne = BinaryNode(10)
    tree_binarne.add_left_child(9)
    tree_binarne.add_right_child(2)
    tree_binarne.left_child.add_left_child(1)
    tree_binarne.left_child.add_right_child(3)
    tree_binarne.right_child.add_right_child(6)
    tree_binarne.right_child.add_left_child(4)

    tree_binarne.traverse_in_order(print)
    print("---------------")

if __name__ == "__main__":
    main()

