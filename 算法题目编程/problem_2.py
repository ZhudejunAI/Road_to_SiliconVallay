# coding=utf-8

import numpy as np


def hasSum(array, target):
    dict_array = {}
    for i in xrange(0, len(array)):
        dict_array[array[i]] = i

    for i in xrange(0, len(array)):
        temp = target - array[i]
        if dict_array.get(temp, None) == None:
            continue
        else:
            return i, dict_array[temp]

    return -1, -1


def main():
    array = [11, 7, 45, 67, 134, 5, 83, 55, 106, 33, 57, 82, 6, 24, 87, 61, 3, 39, 6, 26]
    target_number = 7
    a, b = hasSum(array, target_number)
    if a != -1:
        print('YES, %d, %d' % (a, b))
    else:
        print('NO')


if __name__ == '__main__':
    main()
