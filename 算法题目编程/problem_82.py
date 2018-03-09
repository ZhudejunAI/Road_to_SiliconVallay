from __future__ import print_function
import numpy as np


def min_palin_cut(s):
    length = len(s)
    dp = [0] * (length + 1)
    isPa = np.zeros((length, length))

    for i in range(0, length + 1):
        dp[i] = length - i - 1

    for i in range(length - 1, -1, -1):
        for j in range(i, length):
            if s[i] == s[j] and (j - i < 2 or isPa[i + 1][j - 1] == 1):
                isPa[i][j] = 1
                dp[i] = np.minimum(dp[i], dp[j + 1] + 1)

    return dp[0]


def main():
    s = 'ababcbc'
    result = min_palin_cut(s)
    print(result)


if __name__ == '__main__':
    main()
