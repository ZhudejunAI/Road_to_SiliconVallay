from __future__ import print_function


def print_interleaving(s1, s2, current):
    if (s1 is None or len(s1) == 0) and (s2 is None or len(s2) == 0):
        return

    if s1 is None or len(s1) == 0:
        res = current + s2
        print(res)
        return

    if s2 is None or len(s2) == 0:
        res = current + s1
        print(res)
        return

    print_interleaving(s1[1:], s2, current + s1[0])
    print_interleaving(s1, s2[1:], current + s2[0])


def main():
    s1 = 'AB'
    s2 = 'CD'
    print_interleaving(s1, s2, '')

if __name__ == '__main__':
    main()
