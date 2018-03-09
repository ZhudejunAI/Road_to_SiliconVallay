from __future__ import print_function
import numpy as np


def edit_distance(word1, word2):
    length1 = len(word1)
    length2 = len(word2)
    if length1 == 0:
        return length2
    if length2 == 0:
        return length1

    dp = np.zeros((length1+1, length2+1))
    for i in range(0, length1+1):
        dp[i][0] = i
    for j in range(0, length2+1):
        dp[0][j] = j

    for i in range(1, length1+1):
        for j in range(1, length2+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + np.minimum(dp[i-1][j-1], np.minimum(dp[i-1][j], dp[i][j-1]))

    return dp[length1][length2]


def main():
    word1 = 'helloworld'
    word2 = 'well_wordddd'
    result = edit_distance(word1, word2)
    print(int(result))


if __name__ == '__main__':
    main()
