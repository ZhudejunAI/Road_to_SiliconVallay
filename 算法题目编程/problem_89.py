from __future__ import print_function


def get_transform(word, end, used, dictionary):
    letters = list(word)
    length = len(letters)
    result = []
    letter_list = [chr(i) for i in range(97, 123)]
    for i in range(0, length):
        origin = letters[i]
        for c in letter_list:
            if origin != c:
                letters[i] = c
                trans = ''.join(letters)
                if trans == end or (trans not in used and trans in dictionary):
                    used.add(trans)
                    result.append(trans)
        letters[i] = origin

    return result


def word_ladder(start, end, dictionary):
    used = set()
    current_level = []

    current_level.append(start)
    count = 1
    while len(current_level) > 0:
        next_level = []
        count += 1
        while len(current_level) > 0:
            cur_word = current_level[0]
            current_level = current_level[1:]

            trans_words = get_transform(cur_word, end, used, dictionary)
            for trans_word in trans_words:
                if trans_word == end:
                    return count
                next_level.append(trans_word)

        current_level = next_level

    return 0


def main():
    start = 'hit'
    end = 'cog'
    dictionary = ['hot', 'dot', 'dog', 'lot', 'log']
    res = word_ladder(start, end, dictionary)
    print(res)


if __name__ == '__main__':
    main()
