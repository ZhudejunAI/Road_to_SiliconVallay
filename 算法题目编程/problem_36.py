from __future__ import print_function
import numpy as np
from TreeModel import TreeNode


def nearest_common_parent(root, p, q):
    if root is None or p is None or q is None:
        return None

    if root == p or root == q:
        return root

    left_node = nearest_common_parent(root.left, p, q)
    right_node = nearest_common_parent(root.right, p, q)
    if left_node is not None and right_node is not None:
        return root
    elif left_node is not None:
        return left_node
    else:
        return right_node


def main():
    a1 = TreeNode(3)
    a2 = TreeNode(1)
    a3 = TreeNode(9)
    a4 = TreeNode(5)
    a5 = TreeNode(4)
    a6 = TreeNode(7)
    a1.left = a2
    a1.right = a3
    a2.left = a4
    a2.right = a5
    a3.right = a6
    common_parent = nearest_common_parent(a1, a1, a6)
    print(common_parent.value)


if __name__ == '__main__':
    main()
