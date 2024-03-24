from design_patterns.behavioral.iterator_pattern.binarytree_iterator import Node, BinaryTree


def test_main():
    # Assign
    # Example usage
    # Construct a binary tree
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    binary_tree = BinaryTree(root)
    iterator = binary_tree.get_inorder_iterator()

    # Ace
    traversal = []
    while iterator.has_next():
        next_node_value = iterator.next()
        traversal.append(next_node_value)
        print(next_node_value, end=" ")  # Outputs: 4 2 5 1 3

    # Assert
    assert traversal == [4, 2, 5, 1, 3]