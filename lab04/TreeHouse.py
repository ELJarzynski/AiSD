from typing import Any, List, Callable, Union
from Queue import Queue
import graphviz

dot = graphviz.Digraph('Tree')

class TreeNode:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.children: List['TreeNode'] = []

    def visited(self, data):
        print(data.value)

    def is_leaf(self):
        if len(self.children) > 0:
            return False
        return True

    def min(self) -> Any:
        if not self.children:
            return self.value
        return min(child.min() for child in self.children)

    def add(self, child: 'TreeNode') -> None:
        return self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)

        if len(self.children) > 0:
            for child in self.children:
                child.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]):
        que = Queue()
        que.enqueue(self)

        while len(que) > 0:
            p = que.dequeue()
            visit(p)
            for child in p.children:
                que.enqueue(child)

    def for_each_s_level_order(self, visit: Callable[['TreeNode'], None]):
            quee = Queue()
            quee.enqueue(self)

            while len(quee) > 0:
                p = quee.dequeue()
                visit(p)
                if p.value % 2 == 0:
                    for child in reversed(p.children):
                        quee.enqueue(child)

    def search(self, value: Any) -> Union['TreeNode', None]:
        if self.value == value:
            return self

        for child in self.children:
            result = child.search(value)
            if result is not None:
                return result

    def print(self):
        print(self.value)
        if len(self.children) > 0:
            for child in self.children:
                child.print()

    def show(self, dot):
        dot.node(str(self), str(self.value))
        for x in self.children:
            dot.edge(str(self), str(x))
            x.show(dot)
        return dot


class Tree:
    def __init__(self, value):
        self.root = TreeNode(value)

    def add(self, value: Any, parent_name: Any) -> None:
        parent_name.children(TreeNode(value))

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)


root = TreeNode(10)
root.add(TreeNode(9))
root.add(TreeNode(8))
root.children[0].add(TreeNode(7))
root.children[0].add(TreeNode(6))
root.children[1].add(TreeNode(5))
root.children[0].children[1].add(TreeNode(4))
root.children[0].children[1].add(TreeNode(3))
root.children[1].children[0].add(TreeNode(2))

# root.print()
print("----first-----")
root.for_each_deep_first(root.visited)
print("---------")
root.for_each_s_level_order(root.visited)
# print("----second-----")
print("---------")
val = root.min()
print(val)
# root.for_each_deep_second(root.visited)
# print("----third-----")
# root.for_each_deep_third(root.visited)
# print("---------")
# print(root.children[1].children[0].children[0].is_leaf())#False
# print(root.children[1].children[0].is_leaf())#True
#graphviz
# root.show(dot).render(directory='doctest-output', view=True).replace('\\', '/')
