from __future__ import print_function
import numpy as np
from TreeModel import TreeNode


def nearest_common_parent(root, p1, p2):
    if root is None or p1 is None or p2 is None:
        return None
    if root.value > p1.value and root.value > p2.value:
        return nearest_common_parent(root.left, p1, p2)
    elif root.value < p1.value and root.value < p2.value:
        return nearest_common_parent(root.right, p1, p2)
    else:
        return root


def main():
    a1 = TreeNode(5)
    a2 = TreeNode(3)
    a3 = TreeNode(7)
    a4 = TreeNode(1)
    a5 = TreeNode(4)
    a6 = TreeNode(9)
    a1.left = a2
    a1.right = a3
    a2.left = a4
    a2.right = a5
    a3.right = a6
    common_parent = nearest_common_parent(a1, a1, a2)
    print(common_parent.value)


if __name__ == '__main__':
    main()
