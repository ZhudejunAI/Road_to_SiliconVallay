from __future__ import print_function
import numpy as np
from ListModel import ListNode


def mergeList(list1, list2):
    dummy = ListNode(0)
    current = ListNode(0)
    dummy.next_node = current
    while list1 is not None and list2 is not None:
        if list1.value <= list2.value:
            current.next_node = list1
            list1 = list1.next_node
        else:
            current.next_node = list2
            list2 = list2.next_node
        current = current.next_node

    if list1 is not None:
        current.next_node = list1
    elif list2 is not None:
        current.next_node = list2

    return dummy.next_node


def main():
    a1 = ListNode(5)
    a2 = ListNode(15)
    a1.next_node = a2
    b1 = ListNode(10)
    b2 = ListNode(15)
    b3 = ListNode(20)
    b1.next_node = b2
    b2.next_node = b3
    res = mergeList(a1, b1)
    res = res.next_node
    while res is not None:
        print(str(res.value) + ' -> ', end='')
        res = res.next_node


if __name__ == '__main__':
    main()
