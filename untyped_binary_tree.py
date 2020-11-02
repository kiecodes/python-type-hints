class BinaryTree:
    # value

    left = None
    right = None

    def __init__(self, value):
        self.value = value

    def add(self, value):
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

    def find(self, value):
        if self.value == value:
            return self.value
        elif value < self.value and self.left is not None:
            return self.left.find(value)
        elif value > self.value and self.right is not None:
            return self.right.find(value)
        return None

    def traverse(self, func):
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


def printer(n):
    print(n)
    return True


tree = BinaryTree(5)
print(tree.find(5))
print(tree.find(4))

tree.add(4)
print(tree.find(4))

tree.add(7)
tree.add(3)
tree.add(0.5)

print("\nPrint Tree:")
tree.traverse(printer)