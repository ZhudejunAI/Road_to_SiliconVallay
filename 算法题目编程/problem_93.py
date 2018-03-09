from __future__ import print_function


def anagram(string_array):
    hash_map_str = {}
    for s in string_array:
        sort_s = sorted(s)
        ana_s = ''.join(sort_s)
        if ana_s not in hash_map_str.keys():
            hash_map_str[ana_s] = [s]
        else:
            hash_map_str[ana_s].append(s)

    return hash_map_str


def main():
    str_arr = ['boy', 'blue', 'yob', 'red', 'girl', 'hunter', 'lube']
    res = anagram(str_arr)
    for r in res.keys():
        res_str = res[r]
        if len(res_str) > 1:
            print(res_str)


if __name__ == '__main__':
    main()
