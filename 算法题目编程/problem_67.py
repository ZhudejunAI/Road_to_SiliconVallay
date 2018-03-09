from __future__ import print_function


def get_point_number(a):
    length = len(a)
    result = []
    flag = [0] * length
    first_max = a[0]
    for i in range(0, length):
        if a[i] >= first_max:
            first_max = a[i]
            flag[i] = 1
    second_min = a[-1]
    for i in range(length - 1, -1, -1):
        if a[i] <= second_min:
            second_min = a[i]
            if flag[i] == 1:
                result.append(i)

    return result


def main():
    a = [1, 0, 1, 0, 1, 2, 3]
    res = get_point_number(a)
    print(res)


if __name__ == '__main__':
    main()
