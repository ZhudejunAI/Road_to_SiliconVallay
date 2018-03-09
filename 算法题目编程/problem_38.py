from __future__ import print_function
import numpy as np
from TreeModel import TreeNode


def path_sum(root, number):
    if root is None:
        return False
    if root.value == number and root.left is None and root.right is None:
        return True

    left_flag = False
    right_flag = False
    if root.left is not None:
        left_flag = path_sum(root.left, number - root.value)
    if root.right is not None:
        right_flag = path_sum(root.right, number - root.value)

    return left_flag or right_flag


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
    res = path_sum(a1, 21)
    print(res)


if __name__ == '__main__':
    main()
