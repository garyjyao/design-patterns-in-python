class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class InorderBinaryTreeIterator:
    def __init__(self, root):
        self.root = root
        self.stack = []
        self.current = root

    def has_next(self):
        return self.current is not None or len(self.stack) > 0

    def next(self):
        while self.current is not None:
            self.stack.append(self.current)
            self.current = self.current.left

        self.current = self.stack.pop()
        node = self.current
        self.current = self.current.right

        return node.value


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def get_inorder_iterator(self):
        return InorderBinaryTreeIterator(self.root)


# Example usage commented out, see unit test instead
# Construct a binary tree
#       1
#      / \
#     2   3
#    / \
#   4   5
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
#
# binary_tree = BinaryTree(root)
# iterator = binary_tree.get_inorder_iterator()
#
# while iterator.has_next():
#     print(iterator.next(), end=" ")  # Outputs: 4 2 5 1 3
