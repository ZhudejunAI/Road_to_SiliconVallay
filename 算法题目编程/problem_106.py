from __future__ import print_function


def cal_rp_notation(s):
    length = len(s)
    if length == 0:
        return ''
    result = ''
    stack_s = []

    for i in range(0, length):
        c = s[i]
        if c == '+' or c == '-' or c == '*' or c == '/':
            if result == '':
                result = stack_s[-1] * 1.0
                stack_s = stack_s[:-1]
            first = stack_s[-1]
            stack_s = stack_s[:-1]

            if c == '+':
                result = first + result
            elif c == '-':
                result = first - result
            elif c == '*':
                result = first * result
            else:
                result = first / result
        else:
            stack_s.append(int(s[i]))

    return result


def main():
    s = ['5', '8', '3', '/', '+']
    res = cal_rp_notation(s)
    print(res)


if __name__ == '__main__':
    main()
