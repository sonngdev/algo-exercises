from typing import Generator
from .tree import Tree

class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure"""

    def left(self, p):
        raise NotImplementedError('Must be implemented by subclass')

    def right(self, p):
        raise NotImplementedError('Must be implemented by subclass')

    def sibling(self, p):
        parent = self.parent(p)

        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def position(self):
        return self.inorder()

    # Private

    def _subtree_inorder(self, p) -> Generator[Tree.Position]:
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other
