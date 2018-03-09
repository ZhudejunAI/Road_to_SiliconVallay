from __future__ import print_function


def min_string_window(s, t):
    if t is None or len(t) == 0:
        return ''

    s_len = len(s)
    t_len = len(t)
    t_hash_map = {}
    s_hash_map = {}

    for i in range(0, t_len):
        c = t[i]
        if c in t_hash_map.keys():
            t_hash_map[c] = t_hash_map[c] + 1
        else:
            t_hash_map[c] = 1

    start = 0
    count = 0
    min_start = -1
    min_length = 100

    for i in range(0, s_len):
        c = s[i]
        if c not in t_hash_map.keys():
            continue

        if c not in s_hash_map.keys():
            s_hash_map[c] = 1
        else:
            s_hash_map[c] = s_hash_map[c] + 1

        if s_hash_map[c] <= t_hash_map[c]:
            count = count + 1

        if count >= t_len:
            c_start = s[start]
            while c_start not in s_hash_map.keys() or s_hash_map[c_start] > t_hash_map[c_start]:
                if c_start in s_hash_map.keys():
                    s_hash_map[c_start] = s_hash_map[c_start] - 1
                start = start + 1
                c_start = s[start]

            temp_len = i - start + 1
            if temp_len < min_length:
                min_length = temp_len
                min_start = start

    if min_start >= 0:
        return s[min_start:min_start + min_length]
    else:
        return ''


def main():
    s = 'AFEGCABC'
    t = 'FACE'
    result = min_string_window(s, t)
    print(result)


if __name__ == '__main__':
    main()
