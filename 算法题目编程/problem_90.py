from __future__ import print_function


def gen_string_by_rule(s, dictionary, start, used, op):
    if start == len(s):
        if op not in used:
            used.add(op)
            print(op)
        return

    key_char = s[start]
    if key_char in dictionary.keys():
        mutation = dictionary[key_char]
        for c in mutation:
            gen_string_by_rule(s, dictionary, start + 1, used, op + c)

    gen_string_by_rule(s, dictionary, start + 1, used, op + key_char)


def gen_string(s, dictionary):
    used = set()
    used.add(s)
    gen_string_by_rule(s, dictionary, 0, used, '')


def main():
    dictionary = {'a': ['@'], 'e': ['3', 'E']}
    str = 'face'
    gen_string(str, dictionary)


if __name__ == '__main__':
    main()
