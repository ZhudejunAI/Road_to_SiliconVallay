from __future__ import print_function
import numpy as np


def number_of_substring(s, t):
    length1 = len(s)
    length2 = len(t)
    if length1 < length2:
        return -1

    dp = np.zeros((length1 + 1, length2 + 1))
    for i in range(0, length1 + 1):
        dp[i][0] = 1

    for i in range(1, length1 + 1):
        for j in range(1, length2 + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[length1][length2]


def main():
    s = 'exxampple'
    t = 'example'
    result = number_of_substring(s, t)
    print(int(result))


if __name__ == '__main__':
    main()
