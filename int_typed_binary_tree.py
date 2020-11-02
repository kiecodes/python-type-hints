from typing import Optional, Callable

class BinaryTree:
    value: int

    left: 'Optional[BinaryTree]' = None
    right: 'Optional[BinaryTree]' = None

    def __init__(self, value: int):
        self.value = value

    def add(self, value: int):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTree(value)
            else:
                self.left.add(value)
        else:
            if self.right is None:
                self.right = BinaryTree(value)
            else:
                self.right.add(value)

    def find(self, value: int) -> 'Optional[int]':
        if self.value == value:
            return value
        elif value < self.value and self.left is not None:
            return self.left.find(value)
        elif value > self.value and self.right is not None:
            return self.right.find(value)
        return None

    def traverse(self, func: Callable[[int], bool]):
        if self.left is not None:
            if not self.left.traverse(func):
                return False

        done = not func(self.value)
        if done:
            return False

        if self.right is not None:
            if not self.right.traverse(func):
                return False

        return True


def printer(n: int):
    print(n)
    return True


tree = BinaryTree(5)
print(tree.find(5))
print(tree.find(4))

tree.add(4)
print(tree.find(4))

tree.add(7)
tree.add(3)
# tree.add(0.5) <- type error

print("\nPrint Tree:")
tree.traverse(printer)