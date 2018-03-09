# coding=utf-8

import numpy as np


def getclosenumber(x, y):
    sorted_x = sorted(x)
    length = len(x)
    result = []
    used = [False] * length
    for i in range(length):
        j = 0
        while j < length and (used[j] or sorted_x[j] < y[i]):
            j += 1

        used[j] = True
        result.append(sorted_x[j])

        if j == length:
            break

        if sorted_x[j] > y[i]:
            for k in range(length):
                if not used[k]:
                    result.append(sorted_x[k])
            break

    return result


def main():
    x = [4, 6, 2, 0, 3, 5]
    y = [5, 3, 2, 4, 1, 0]
    res = getclosenumber(x, y)
    print("res=%s" % res)


if __name__ == '__main__':
    main()
