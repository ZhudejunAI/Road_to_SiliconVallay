from __future__ import print_function
from TreeModel import TreeNode
count = 0


def recover_tree(root, n1, n2, prev, result):
    if root.left is not None:
        recover_tree(root.left, n1, n2, prev, result)

    if prev.value != 0 and prev.value > root.value:
        n2 = root
        result.append(n2.value)
        if n1.value == 0:
            n1 = prev
            result.append(n1.value)

    prev = root

    if root.right is not None:
        recover_tree(root.right, n1, n2, prev, result)


def recover_tree_prime(root):
    n1 = TreeNode(0)
    n2 = TreeNode(0)
    prev = TreeNode(0)
    result = []
    recover_tree(root, n1, n2, prev, result)

    if len(result) == 4:
        print('YES2')
        print('%d --- %d' % (result[1], result[2]))
    elif len(result) == 2:
        print('YES1')
        print('%d --- %d' % (result[0], result[1]))
    else:
        print('NO')


def main():
    a1 = TreeNode(5)
    a2 = TreeNode(7)
    a3 = TreeNode(3)
    a4 = TreeNode(1)
    a5 = TreeNode(4)
    a6 = TreeNode(9)
    a1.left = a2
    a1.right = a3
    a2.left = a4
    a2.right = a5
    a3.right = a6
    recover_tree_prime(a1)


if __name__ == '__main__':
    main()
