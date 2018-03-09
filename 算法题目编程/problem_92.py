from __future__ import print_function
import numpy as np


def merge_sequence(seq_map, left, right):
    upper = right + seq_map[right] - 1
    lower = left - seq_map[left] + 1
    length_max = upper - lower + 1
    seq_map[upper] = length_max
    seq_map[lower] = length_max
    return length_max


def longest_consequence(s):
    seq_map = {}
    max_sequence = 1
    for i in s:
        if i in seq_map.keys():
            continue
        seq_map[i] = 1

        if i - 1 in seq_map.keys():
            temp = merge_sequence(seq_map, i-1, i)
            max_sequence = np.maximum(max_sequence, temp)

        if i + 1 in seq_map.keys():
            temp = merge_sequence(seq_map, i, i+1)
            max_sequence = np.maximum(max_sequence, temp)

    return max_sequence


def main():
    s = [8, 1, 9, 3, 7, 2, 4, 11, 10]
    result = longest_consequence(s)
    print(result)


if __name__ == '__main__':
    main()
