from __future__ import print_function
import numpy as np


def get_max_profit(price):
    length = len(price)
    current_profit = [0] * length
    future_profit = [0] * length
    low = price[0]
    for i in range(1, length):
        low = np.minimum(low, price[i])
        current_profit[i] = np.maximum(current_profit[i - 1], price[i] - low)

    high = price[length - 1]
    for i in range(length - 2, -1, -1):
        high = np.maximum(high, price[i])
        future_profit[i] = np.maximum(future_profit[i + 1], high - price[i])

    max_profit = 0
    for i in range(0, length):
        max_profit = np.maximum(max_profit, current_profit[i] + future_profit[i])

    return max_profit


def main():
    price = [68, 72, 59, 73, 66, 63, 59, 72, 65, 70, 64, 75, 71, 70, 67, 70, 72, 66, 63, 59, 68, 73, 74]
    result = get_max_profit(price)
    print(result)


if __name__ == '__main__':
    main()
