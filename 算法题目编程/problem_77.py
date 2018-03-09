from __future__ import print_function


def decode_number(num):
    if len(num) == 0:
        return 0

    length = len(num)
    dp = [0] * (length + 1)
    dp[length] = 1
    for i in range(length - 1, -1, -1):
        if num[i] == '0':
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]

        if i + 1 < length and (num[i] == '1' or (num[i] == '2' and int(num[i + 1]) <= 6)):
            dp[i] += dp[i + 2]

    return dp[0]


def main():
    num = '2610122'
    result = decode_number(num)
    print(result)


if __name__ == '__main__':
    main()
