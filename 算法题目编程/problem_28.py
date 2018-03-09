from __future__ import print_function
import numpy as np
from ListModel import ListNode


def reversrlist(head, newHead):
    if head is None:
        return
    if head.next_node is None:
        newHead = head
        return newHead
    else:
        newHead = reversrlist(head.next_node, newHead)
        head.next_node.next_node = head
        head.next_node = None
        return newHead


def main():
    head = ListNode(0)
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(4)
    head.next_node = a1
    a1.next_node = a2
    a2.next_node = a3
    a3.next_node = a4
    res = reversrlist(a1, head)
    while res is not None:
        print(str(res.value) + ',', end='')
        res = res.next_node


if __name__ == '__main__':
    main()
