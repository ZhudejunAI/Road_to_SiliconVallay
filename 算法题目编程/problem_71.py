from __future__ import print_function
import numpy as np


def max_array_sum(a):
    current_max_sum = 0
    temp_sum = 0
    length = len(a)
    for i in range(0, length):
        temp_sum += a[i]
        if temp_sum < 0:
            temp_sum = 0
        if temp_sum > current_max_sum:
            current_max_sum = temp_sum

    return current_max_sum


def main():
    a = [-3, 1, -3, 4, -1, 2, 1]
    result = max_array_sum(a)
    print(result)

if __name__ == '__main__':
    main()
