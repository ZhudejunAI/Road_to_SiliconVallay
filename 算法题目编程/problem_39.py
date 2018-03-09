from __future__ import print_function
import numpy as np
from TreeModel import TreeNode


def find_path_sum(root, number, path, total_path, level):
    if root is None:
        return
    path.append(root.value)

    if root.left is None and root.right is None:
        temp = number
        for i in range(level, -1, -1):
            temp -= path[i]
            if temp == 0:
                copy_path(path, i, level, total_path)
    else:
        find_path_sum(root.left, number, path, total_path, level + 1)
        find_path_sum(root.right, number, path, total_path, level + 1)

    path.remove(path[-1])


def copy_path(path, start, end, total_path):
    sub_path = []
    for i in range(start, end + 1):
        sub_path.append(path[i])
    total_path.append(sub_path)


def path_sum(root, number):
    path = []
    total_path = []
    find_path_sum(root, number, path, total_path, 0)
    return total_path


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
    res_path = path_sum(a1, 10)
    for sub_path in res_path:
        for node in sub_path:
            print(str(node)+'+', end='')
        print()


if __name__ == '__main__':
    main()
