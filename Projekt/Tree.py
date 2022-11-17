from typing import Any, List, Callable, Union
from Queue import Queue
import graphviz

d = graphviz.Digraph('Tree')

class TreeNode:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.children: List['TreeNode'] = []

    def visited(self, node: 'TreeNode'):
        print(node.value)


    def is_leaf(self) -> bool:
        if len(self.children) == 0:
            return False
        return True


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
            temp = que.dequeue().data
            visit(temp)
            for child in temp.children:
                que.enqueue(child)


    def search(self, value: Any) -> Union['TreeNode', None]:
        if self.value == value:
            return self

        if len(self.children) != 0:
            for child in self.children:
                if child.search(value) != 0:
                    return child.search(value)


    def print(self)->None:
        print(self.value)

        if len(self.children) != 0:
            for child in self.children:
                child.print()


    def show(self, d):
        d.node(str(self), str(self.value))
        for child in self.children:
            d.edge(str(self), str(child))
            child.show(d)
        return d


class Tree:
    def __init__(self, value: Any):
        self.root = TreeNode(value)


    def add(self, value: Any, parent_name: Any) -> None:
        parent_name.children.append(TreeNode(value))


    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
            self.root.for_each_level_order(visit)


    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        if self.root != None:
            self.root.for_each_deep_first(visit)

root = TreeNode("F")
root.add(TreeNode("B"))
root.add(TreeNode("G"))
root.children[0].add(TreeNode("A"))
root.children[0].add(TreeNode("D"))
root.children[1].add(TreeNode("I"))
root.children[0].children[1].add(TreeNode("C"))
root.children[0].children[1].add(TreeNode("E"))
root.children[1].children[0].add(TreeNode("H"))

root.for_each_deep_first(root.visited)
print("---------")
root.for_each_level_order(root.visited)
print("---------")

print(root.children[1].children[0].children[0].is_leaf())#False
print(root.children[1].children[0].is_leaf())#True
#graphviz
root.show(d).render(directory='doctest-output', view=True).replace('\\', '/')
