from __future__ import print_function
import numpy as np
from TreeModel import TreeNode


def tree_append(node1, node2):
    if node1 is None:
        return node2
    if node2 is None:
        return node1

    tail = node1
    while tail.right is not None:
        tail = tail.right

    tail.right = node2
    node2.left = tail
    return node1


def tree_to_double_list(p):
    if p is None:
        return None
    left_tree = tree_to_double_list(p.left)
    right_tree = tree_to_double_list(p.right)
    p.left = None
    p.right = None
    left_tree = tree_append(left_tree, p)
    left_tree = tree_append(left_tree, right_tree)
    return left_tree


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
    new_Head = tree_to_double_list(a1)
    cur = new_Head
    parent = new_Head
    while cur is not None:
        print(str(cur.value) + ',', end='')
        parent = cur
        cur = cur.right
    print()
    while parent is not None:
        print(str(parent.value) + ',', end='')
        parent = parent.left


if __name__ == '__main__':
    main()
