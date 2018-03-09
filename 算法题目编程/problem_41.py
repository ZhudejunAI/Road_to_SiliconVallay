from __future__ import print_function
import numpy as np
from TreeModel import TreeNode


def find_mirror_tree(root):
    left_queue = []
    right_queue = []
    left_queue.append(root)
    right_queue.append(root)
    while len(left_queue) > 0 and len(right_queue) > 0:
        left_node = left_queue[0]
        left_queue = left_queue[1:]
        right_node = right_queue[0]
        right_queue = right_queue[1:]
        if left_node is None and right_node is None:
            continue
        elif left_node is None or right_node is None:
            return False

        if left_node.value != right_node.value:
            return False

        left_queue.append(left_node.left)
        left_queue.append(left_node.right)
        right_queue.append(right_node.right)
        right_queue.append(right_node.left)

    if len(left_queue) == 0 and len(right_queue) == 0:
        return True
    else:
        return False


def main():
    a1 = TreeNode(5)
    a2 = TreeNode(3)
    a3 = TreeNode(3)
    a4 = TreeNode(1)
    a5 = TreeNode(1)
    a1.left = a2
    a1.right = a3
    a2.right = a4
    a3.right = a5
    res = find_mirror_tree(a1)
    if res is True:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
