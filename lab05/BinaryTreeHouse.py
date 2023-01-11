from typing import Any, Callable
import graphviz


class BinaryNode:
    def __init__(self, value: Any):
        self.value = value
        self.left_child = None
        self.right_child = None

    def find_max(self) -> Any:
        if self.right_child is None:
            return self.value
        else:
            return self.right_child.find_min()

    def find_min(self) -> Any:
        if self.left_child is None:
            return self.value
        else:
            return self.left_child.find_min()

    def is_leaf(self) -> bool:
        if self.left_child is None and self.right_child is None:
            return True
        return False

    def add_child(self, value):
        if value == self.value:
            return

        if value < self.value:
            # dodanie do lewego
            if self.left_child:
                self.left_child.add_child(value)
            else:
                self.left_child = BinaryNode(value)
        else:
            # dodanie do prawego
            if self.right_child:
                self.right_child.add_child(value)
            else:
                self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)

        visit(self)

        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)

        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)

        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)

        if self.left_child is not None:
            self.left_child.traverse_pre_order(visit)

        if self.right_child is not None:
            self.right_child.traverse_pre_order(visit)

    def show(self, dot = None):
        if dot is None:
            dot = graphviz.Digraph("BinaryTree", format="png")

        dot.node(str(self),str(self.value))

        if self.left_child:
            dot.node(str(self.left_child),str(self.left_child.value))
            dot.edge(str(self),str(self.left_child))
            self.left_child.show(dot)

        if self.right_child:
            dot.node(str(self.right_child),str(self.right_child.value))
            dot.edge(str(self),str(self.right_child))
            self.right_child.show(dot)

        dot.render(directory='doctest-output').replace('\\', '/')


class BinaryTree:
    def __init__(self, value):
        self.root = value

    def find_min(self) -> Any:
        return self.root.find_min()

    def find_max(self) -> Any:
        return self.root.find_max()

    def traverse_in_order(self, visit: Callable[[Any], None]):
        return self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        return self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        return self.root.traverse_pre_order(visit)

    def show(self):
        self.root.show()


def print_value(node: BinaryNode):
    print(node.value)


tree = BinaryTree(BinaryNode(5))
tree.root.add_child(3)
tree.root.add_child(7)
tree.root.add_child(2)
tree.root.add_child(4)
tree.root.add_child(6)
tree.root.add_child(8)
print("---in---")
tree.traverse_in_order(print_value)
print("---post---")
tree.traverse_post_order(print_value)
print("---pre---")
tree.traverse_pre_order(print_value)

binary_tree = BinaryTree(tree)
binary_tree.show()
print("---min---")
print(tree.find_min())
print("---max---")
print(tree.find_max())
