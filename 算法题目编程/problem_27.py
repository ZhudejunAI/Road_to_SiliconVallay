from __future__ import print_function
import numpy as np
from ListModel import ListNode


def lengthOfCircle(list1):
    first = ListNode(0)
    second = ListNode(0)
    first.next_node = list1
    second.next_node = list1
    while first is not None and second is not None:
        if first == second:
            return 1, first
        first = first.next_node
        second = second.next_node
        second = second.next_node

    if first is None or second is None:
        return 0, first


def main():
    a1 = ListNode(3)
    a2 = ListNode(8)
    a3 = ListNode(7)
    a4 = ListNode(1)
    a5 = ListNode(2)
    a6 = ListNode(3)
    a7 = ListNode(4)
    a8 = ListNode(5)
    a1.next_node = a2
    a2.next_node = a3
    a3.next_node = a4
    a4.next_node = a5
    a5.next_node = a6
    a6.next_node = a7
    a7.next_node = a8
    a8.next_node = a4
    res, keynode = lengthOfCircle(a1)
    if res == 1:
        print('YES!')
        count_node = keynode.next_node
        num = 1
        while keynode is not count_node:
            count_node = count_node.next_node
            num += 1
        print('The length of circle is %d' % num)
    else:
        print('NO!')


if __name__ == '__main__':
    main()
