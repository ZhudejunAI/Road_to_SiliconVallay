from __future__ import print_function
import numpy as np


def get_all_ip(s, start, part, ip, result):
    length_s = len(s)
    if length_s - start > (4 - part) * 3:
        return

    if length_s - start < (4 - part):
        return

    if start == length_s and part == 4:
        result.append(ip[:-1])
        return

    num = 0
    max_i = np.minimum(start+3, length_s)
    for i in range(start, max_i):
        num = num * 10 + int(s[i])
        if num < 256:
            ip += s[i]
            get_all_ip(s, i+1, part+1, ip+'.', result)
        if num == 0:
            break


def get_ip(s):
    result = []
    ip = ''
    get_all_ip(s, 0, 0, ip, result)
    return result


def main():
    s = '10112'
    res = get_ip(s)
    for i in res:
        print(i)


if __name__ == '__main__':
    main()
