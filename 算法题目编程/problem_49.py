from __future__ import print_function
import numpy as np
from TreeModel import TreeNode


def get_max_sum(root, max_sum):
    if root is None:
        return 0
    left_sum = get_max_sum(root.left, max_sum)
    right_sum = get_max_sum(root.right, max_sum)
    current_sum = np.maximum(root.value, np.maximum(root.value + left_sum, root.value + right_sum))

    max_sum[0] = np.maximum(max_sum[0], np.maximum(current_sum, root.value + left_sum + right_sum))
    return current_sum


def max_path_sum(root):
    max_sum = []
    max_sum.append(-100)
    res = get_max_sum(root, max_sum)
    return max_sum[0]


def main():
    a1 = TreeNode(1)
    a2 = TreeNode(-2)
    a3 = TreeNode(7)
    a4 = TreeNode(3)
    a5 = TreeNode(4)
    a6 = TreeNode(9)
    a1.left = a2
    a1.right = a3
    a2.left = a4
    a2.right = a5
    a3.right = a6
    max_sum = max_path_sum(a1)
    print(max_sum)


if __name__ == '__main__':
    main()
