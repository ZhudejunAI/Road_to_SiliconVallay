from __future__ import print_function
import numpy as np
from TreeModel import TreeNode


def get_height(root):
    if root is None:
        return 0

    left_height = get_height(root.left)
    if left_height == -1:
        return -1

    right_height = get_height(root.right)
    if right_height == -1:
        return -1

    if np.abs(right_height - left_height) > 1:
        return -1

    if right_height >= left_height:
        return 1 + right_height
    else:
        return 1 + left_height


def is_balanced_tree(root):
    return get_height(root)


def main():
    a1 = TreeNode(5)
    a2 = TreeNode(3)
    a3 = TreeNode(7)
    a4 = TreeNode(1)
    a5 = TreeNode(4)
    a6 = TreeNode(9)
    a7 = TreeNode(6)
    a8 = TreeNode(2)
    a1.left = a2
    a1.right = a3
    a2.left = a4
    a2.right = a5
    a3.right = a6
    a5.left = a7
    a5.right = a8
    res = is_balanced_tree(a1)
    if res == -1:
        print('No balance tree.')
    else:
        print('YES')


if __name__ == '__main__':
    main()
