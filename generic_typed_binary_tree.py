from typing import Optional, Generic, TypeVar, Callable

class Role:
    name: str

    def __init__(self, name: str):
        self.name = name

    def __lt__(self, other: 'Role'):
        return self.name < other.name

    def __gt__(self, other: 'Role'):
        return self.name > other.name

class Admin(Role):
    pass


class User(Role):
    pass

T = TypeVar('T', bound=Role)

class BinaryTree(Generic[T]):
    value: T

    left: 'Optional[BinaryTree]' = None
    right: 'Optional[BinaryTree]' = None

    def __init__(self, value: T):
        self.value = value

    def add(self, value: T):
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

    def find(self, value: T) -> 'Optional[T]':
        if self.value == value:
            return value
        elif value < self.value and self.left is not None:
            return self.left.find(value)
        elif value > self.value and self.right is not None:
            return self.right.find(value)
        return None

    def traverse(self, func: Callable[[T], bool]):
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


def print_name(role: Role):
    print(role.name)
    return role.name != "Chris"


tree = BinaryTree[Role](Admin("Max"))
tree.add(User("Chris"))
tree.add(Admin("Alice"))

print("\nPrint Tree:")
tree.traverse(print_name)