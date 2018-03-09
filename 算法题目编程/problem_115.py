from __future__ import print_function
import numpy as np


def phone_number(s, phone_map):
    length = len(s)
    if length == 0:
        return ''
    result = ['']

    for i in range(0, length):
        number = int(s[i])
        char_number = phone_map[number]
        temp = []
        for j in range(0, len(char_number)):
            for k in range(0, len(result)):
                combine_number = result[k] + char_number[j]
                temp.append(combine_number)

        result = temp

    return result


def main():
    s = '23'
    phone_map = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    res = phone_number(s, phone_map)
    for i in res:
        print(i + ', ', end='')


if __name__ == '__main__':
    main()
