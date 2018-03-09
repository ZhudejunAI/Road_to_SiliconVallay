from __future__ import print_function


def compute_perm(signature, n, level, str_perm, used):
    if level == n - 1:
        print(str_perm)
        return True

    i = str_perm[-1]
    if signature[level] == 'I':
        for j in range(i + 1, n + 1):
            if used[j] == 1:
                continue
            used[j] = 1
            str_perm.append(j)
            compute_perm(signature, n, level + 1, str_perm, used)
            str_perm = str_perm[:-1]
            used[j] = 0
    else:
        for j in range(1, i):
            if used[j] == 1:
                continue
            used[j] = 1
            str_perm.append(j)
            compute_perm(signature, n, level + 1, str_perm, used)
            str_perm = str_perm[:-1]
            used[j] = 0

    return False


def main():
    signature = 'DDIIDI'
    n = len(signature)
    used = [0] * (n + 2)
    res = compute_perm(signature, n + 1, 0, [3], used)


if __name__ == '__main__':
    main()
