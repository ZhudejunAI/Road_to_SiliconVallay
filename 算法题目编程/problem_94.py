from __future__ import print_function


def length_of_longest_substring(s):
    if s is None or len(s) == 0:
        return 0, -1
    length = len(s)
    hash_map_str = {}
    start = 0
    max_len = 0
    begin = 0

    for i in range(0, length):
        c = s[i]
        if c in hash_map_str.keys() and hash_map_str[c] >= start:
            start = hash_map_str[c] + 1
        hash_map_str[c] = i
        if i - start + 1 > max_len:
            max_len = i - start + 1
            begin = start

    return max_len, begin


def main():
    s = 'aabrfatbopbrsb'
    result_len, begin = length_of_longest_substring(s)
    print(result_len)
    print(s[begin:begin + result_len])


if __name__ == '__main__':
    main()
