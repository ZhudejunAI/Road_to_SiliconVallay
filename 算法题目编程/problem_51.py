from __future__ import print_function
import numpy as np
from TreeModel import TreeNode


def find_match(left, right, good_match, count):
    if left < 0 or right < left:
        return

    if left == 0 and right == 0:
        for i in good_match:
            print(i + ' ', end='')
        print()
    else:
        if left > 0:
            good_match[count] = '('
            find_match(left - 1, right, good_match, count + 1)
        if right > left:
            good_match[count] = ')'
            find_match(left, right - 1, good_match, count + 1)


def print_par(n):
    str_n = [0]*n*2
    find_match(n, n, str_n, 0)


def main():
    n = 3
    print_par(n)


if __name__ == '__main__':
    main()
