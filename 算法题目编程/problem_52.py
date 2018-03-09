from __future__ import print_function


def get_word(input_string, dict_word, memory_result):
    res = []
    if input_string is None or len(input_string) == 0:
        return res

    if input_string in memory_result.keys():
        return memory_result[input_string]

    if input_string in dict_word:
        res.append(input_string)

    length = len(input_string)
    for i in range(1, length):
        prefix = input_string[0:i]
        if prefix in dict_word:
            postfix = get_word(input_string[i:length], dict_word, memory_result)
            if postfix is not None:
                for seg_postfix in postfix:
                    res.append(prefix + ' ' + seg_postfix)

    memory_result[input_string] = res
    return res
    

def get_dict():
    d = set()
    d.add('is')
    d.add('a')
    d.add('t')
    d.add('an')
    d.add('example')
    d.add('blue')
    d.add('boy')
    d.add('his')
    d.add('this')
    d.add('apple')
    d.add('isan')
    d.add('sane')
    d.add('apple')
    return d


def main():
    input_str = 'thisisanapple'
    dict_w = get_dict()
    memory_res = {}
    result = get_word(input_str, dict_w, memory_res)
    for res in result:
        print(res)


if __name__ == '__main__':
    main()
