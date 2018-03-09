# coding=utf-8

import numpy as np


def hasSum(array, target):
    sorted_array = sorted(array)
    length = len(sorted_array)
    i, j = (0, length - 1)
    while i < j:
        if sorted_array[i] + sorted_array[j] > target:
            j -= 1
        elif sorted_array[i] + sorted_array[j] < target:
            i += 1
        else:
            break

    if i < j:
        return 1, sorted_array[i], sorted_array[j]
    else:
        return 0, 0, 0


def main():
    array = [11, 7, 45, 67, 134, 5, 83, 55, 106, 33, 57, 82, 6, 24, 87, 61, 3, 39, 6, 26]
    target_number = 46
    result, a, b = hasSum(array, target_number)
    if result == 1:
        print('YES, %d + %d = %d' % (a, b, target_number))
    else:
        print('NO')


if __name__ == '__main__':
    main()
