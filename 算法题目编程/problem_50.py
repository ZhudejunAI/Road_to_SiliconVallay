from __future__ import print_function
import numpy as np
from TreeModel import TreeNode


def check_unique_char(str):
    check_str = 0
    for i in str:
        char_to_id = ord(i)
        res_id = 0
        if 65 <= char_to_id <= 90:
            res_id = char_to_id - 65
        elif 97 <= char_to_id <= 122:
            res_id = char_to_id - 97
        if check_str & (1 << res_id) > 0:
            return False
        check_str |= (1 << res_id)

    return True


def main():
    str = 'afUKgnedFo'
    result = check_unique_char(str)
    print(result)


if __name__ == '__main__':
    main()
