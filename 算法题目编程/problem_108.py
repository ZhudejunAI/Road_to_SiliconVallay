from __future__ import print_function


def is_bracket_valid(s):
    length = len(s)
    if length % 2 != 0:
        return False
    stack_s = []
    char_map = {'(': ')', '[': ']', '{': '}'}

    for i in range(0, length):
        c = s[i]
        if len(stack_s) > 0 and stack_s[-1] in char_map.keys() and char_map[stack_s[-1]] == c:
            stack_s = stack_s[:-1]
        else:
            stack_s.append(c)

    if len(stack_s) == 0:
        return True
    else:
        return False


def main():
    s = '()[(){}]'
    res = is_bracket_valid(s)
    print(res)


if __name__ == '__main__':
    main()
