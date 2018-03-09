from __future__ import print_function
import numpy as np


def judge_inter_leave_string(s1, s2, s3):
    length1 = len(s1)
    length2 = len(s2)
    length3 = len(s3)
    if length1 + length2 != length3:
        return False

    dp = np.zeros((length1 + 1, length2 + 1))
    dp[0][0] = 1
    for i in range(1, length1 + 1):
        for j in range(1, length2 + 1):
            if (dp[i][j] == 1 or (i >= 1 and s1[i - 1] == s3[i + j - 1] and dp[i - 1][j] == 1) or (
                                j >= 1 and s2[j - 1] == s3[i + j - 1] and dp[i][j - 1] == 1)):
                dp[i][j] = 1
            else:
                dp[i][j] = 0

    return dp[length1][length2]


def main():
    s1 = 'abc'
    s2 = 'def'
    s3 = 'adebbf'
    result = judge_inter_leave_string(s1, s2, s3)
    if int(result) == 1:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    main()
