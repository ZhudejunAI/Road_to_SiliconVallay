from __future__ import print_function


def color_sort(a):
    length = len(a)
    p = 0
    q = length
    i = 0
    while i < q:
        if a[i] == 0:
            temp = a[p]
            a[p] = a[i]
            a[i] = temp
            p += 1
        elif a[i] == 2:
            q -= 1
            temp = a[q]
            a[q] = a[i]
            a[i] = temp
            i -= 1
        i += 1

    print(a)


def main():
    color_array = [2, 1, 0, 2, 0]
    color_sort(color_array)


if __name__ == '__main__':
    main()
