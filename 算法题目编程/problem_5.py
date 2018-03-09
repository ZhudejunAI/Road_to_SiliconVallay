# coding=utf-8

import numpy as np


def maxDistance(array):
    descent_array = []
    max_number = array[0]
    for i in range(len(array)):
        if i == 0:
            descent_array.append('O')
        else:
            if array[i] < max_number:
                descent_array.append('O')
                max_number = array[i]
            else:
                descent_array.append('X')

    print(descent_array)

    i = j = len(descent_array) - 1
    max_distance = 0
    max_i = -1
    max_j = -1
    while i >= 0:
        if descent_array[i] == 'X':
            i -= 1
            continue

        while array[j] <= array[i] and i < j:
            j -= 1

        if i < j and j - i > max_distance:
            max_distance = j - i
            max_i = i
            max_j = j

        i -= 1

    return max_distance, max_i, max_j



def main():
    array = [5, 3, 4, 0 ,1, 4, 1]
    dis, a, b = maxDistance(array)
    print("dis=%d, start=%d, end=%d" % (dis, a, b))


if __name__ == '__main__':
    main()
