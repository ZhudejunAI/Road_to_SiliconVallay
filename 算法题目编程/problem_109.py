from __future__ import print_function
import numpy as np


def longest_valid_bracket(s):
    stack_s = []
    length = len(s)
    left = 0
    max_len = 0
    begin = 0

    for i in range(0, length):
        c = s[i]
        if c == '(':
            stack_s.append(i)
        else:
            if len(stack_s) == 0:
                left = i + 1
            else:
                stack_s = stack_s[:-1]
                if len(stack_s) == 0:
                    max_len = np.maximum(max_len, i - left + 1)
                    begin = left
                else:
                    max_len = np.maximum(max_len, i - stack_s[-1])
                    begin = stack_s[-1] + 1

    res = s[begin:begin+max_len]
    return max_len, res


def main():
    s = ')()())'
    max_len, res = longest_valid_bracket(s)
    print(max_len)
    print(res)


if __name__ == '__main__':
    main()
