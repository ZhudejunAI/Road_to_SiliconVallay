from __future__ import print_function
from copy import deepcopy


def combine_words(s, t):
    length_s = len(s)
    word_num = len(t)
    word_length = len(t[0])
    s_search_length = word_length * word_num

    t_hash_map = {}
    res = []

    for word in t:
        if word not in t_hash_map.keys():
            t_hash_map[word] = 1
        else:
            t_hash_map[word] = t_hash_map[word] + 1

    for i in range(0, length_s - s_search_length + 1):
        sub_string = s[i:i + s_search_length]
        count = 0
        s_hash_map = deepcopy(t_hash_map)
        for j in range(0, word_num):
            sub_word = sub_string[j * word_length:(j + 1) * word_length]
            if sub_word not in s_hash_map.keys():
                break
            else:
                s_hash_map[sub_word] = s_hash_map[sub_word] - 1
                if s_hash_map[sub_word] >= 0:
                    count += 1
                else:
                    break

        if count == word_num:
            res.append(sub_string)

    return res


def main():
    s = 'barfoothefoobarman'
    t = ['foo', 'bar']
    result = combine_words(s, t)
    for r in result:
        print(r)


if __name__ == '__main__':
    main()
