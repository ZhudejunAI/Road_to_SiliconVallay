from __future__ import print_function
import numpy as np


def get_max_word(s, dict_word):
    length = len(s)
    dp = [0] * length

    for i in range(length):
        sub_string = s[0:i + 1]
        if sub_string in dict_word:
            dp[i] = 1

    for i in range(0, length - 1):
        for j in range(i + 1, length):
            if dp[i] > 0:
                sub_string = s[i + 1:j + 1]
                if sub_string in dict_word:
                    dp[j] = np.maximum(dp[j], dp[i] + 1)

    return dp[length - 1]


def get_dict():
    d = set()
    d.add('is')
    d.add('a')
    d.add('t')
    d.add('an')
    d.add('example')
    d.add('blue')
    d.add('boy')
    d.add('his')
    d.add('this')
    d.add('apple')
    d.add('isan')
    d.add('sane')
    d.add('apple')
    return d


def main():
    input_str = 'thisisanapple'
    dict_w = get_dict()
    result = get_max_word(input_str, dict_w)
    print(result)


if __name__ == '__main__':
    main()
