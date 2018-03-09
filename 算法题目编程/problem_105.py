from __future__ import print_function


def create_rp_notation(s):
    length = len(s)
    if length == 0:
        return ''
    result = ''
    stack_s = []

    for i in range(0, length):
        c = s[i]
        if c == '+' or c == '-' or c == '*' or c == '/':
            if result == '':
                result += stack_s[-1]
                stack_s = stack_s[:-1]
            first = stack_s[-1]
            stack_s = stack_s[:-1]
            result = '(' + first + s[i] + result + ')'
        else:
            stack_s.append(c)

    return result


def main():
    s = ['5', '8', '4', '/', '+']
    res = create_rp_notation(s)
    print(res)


if __name__ == '__main__':
    main()
