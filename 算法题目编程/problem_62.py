from __future__ import print_function
import numpy as np


def get_max_profit(price):
    if price is None or len(price) == 0:
        return 0

    max_profit = 0
    min_price = price[0]
    length = len(price)
    for i in range(1, length):
        min_price = np.minimum(min_price, price[i])
        max_profit = np.maximum(max_profit, price[i] - min_price)

    return max_profit


def main():
    price = [68, 72, 59, 73, 66, 63, 59, 72, 65, 70, 64, 75, 71, 70, 67, 70, 72, 66, 63, 59, 68, 73, 74]
    result = get_max_profit(price)
    print(result)


if __name__ == '__main__':
    main()
