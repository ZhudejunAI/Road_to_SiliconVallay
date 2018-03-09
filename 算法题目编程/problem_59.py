from __future__ import print_function


def is_match_all(s, p, i, j):
    if j == len(p):
        return i == len(s)

    if j == len(p) - 1 or p[j + 1] != '*':
        if i == len(s):
            return False
        return (p[j] == '.' or s[i] == p[j]) and is_match_all(s, p, i + 1, j + 1)

    while i < len(s) and (p[j] == '.' or s[i] == p[j]):
        if is_match_all(s, p, i, j + 2):
            return True
        i += 1

    return is_match_all(s, p, i, j + 2)


def is_match(s, p):
    if s is None:
        return p is None
    if p is None:
        return False
    return is_match_all(s, p, 0, 0)


def main():
    s = 'aabcbcc'
    p = 'a*.cbc..*'
    res = is_match(s, p)
    print(res)


if __name__ == '__main__':
    main()
