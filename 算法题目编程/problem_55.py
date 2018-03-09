from __future__ import print_function


def multiply(n1, n2):
    len1 = len(n1)
    len2 = len(n2)
    num = [0] * (len1 + len2)
    for i in range(len1 - 1, -1, -1):
        for j in range(len2 - 1, -1, -1):
            num[i + j + 1] += (int(n1[i]) * int(n2[j]))

    carry = 0
    len3 = len(num)
    for i in range(len3 - 1, -1, -1):
        num[i] += carry
        carry = num[i] / 10
        num[i] = num[i] % 10

    result = ''
    flag = False
    for i in range(0, len3):
        if flag is not True and num[i] == 0:
            continue
        else:
            result += str(num[i])
            flag = True

    if result is '':
        return '0'
    else:
        return result


def main():
    n1 = '1234'
    n2 = '5678'
    result = multiply(n1, n2)
    print(result)
    print(type(result))


if __name__ == '__main__':
    main()
