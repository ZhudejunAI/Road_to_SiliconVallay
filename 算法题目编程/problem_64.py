from __future__ import print_function


def frog_jump(a):
    i = 0
    length = len(a)
    current_max = 0
    while i < length - 1:
        if a[i] == 0 and current_max < i + 1:
            return False
        if a[i] + i > current_max and a[i] > 0:
            current_max = a[i] + i
            if current_max >= length - 1:
                return True
        i += 1

    return False


def main():
    a = [2, 1, 3, 1, 1]
    b = [3, 2, 1, 0, 1]
    res = frog_jump(b)
    print(res)
    res = frog_jump(a)
    print(res)


if __name__ == '__main__':
    main()
