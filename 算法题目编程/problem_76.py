from __future__ import print_function
import numpy as np


def min_cost_house(h, color):
    if h == 0 or len(color) == 0:
        return 0

    length = len(color)
    dp = np.zeros((h, length))
    for i in range(0, h):
        for j in range(0, length):
            if i == 0:
                dp[i][j] = color[j]
            else:
                min_cost = 100
                for k in range(0, length):
                    if k == j:
                        continue
                    else:
                        min_cost = np.minimum(min_cost, dp[i - 1][k])

                dp[i][j] = min_cost + color[j]

    min_cost = 100
    for i in range(0, length):
        min_cost = np.minimum(min_cost, dp[h - 1][i])

    return min_cost


def main():
    h = 10
    color = [8, 12, 9, 10, 7, 11]
    result = min_cost_house(h, color)
    print(result)


if __name__ == '__main__':
    main()
