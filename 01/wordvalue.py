from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    file = open(DICTIONARY, 'r')
    lines = file.readlines()
    results = []
    for line in lines:
        results.append(line.strip())
    return results


def calc_word_value2(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in list(word):
        if letter not in ['-']:
            score += LETTER_SCORES[letter.upper()]
    return score


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = sum([LETTER_SCORES[l.upper()]
                 for l in list(word) if l not in ['-']])
    return score


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_value = 0
    max_word = ''
    if words == None:
        words = load_words()
    # max_word = [word for word in words if calc_word_value(word) > max_value]
    for word in words:
        if calc_word_value(word) > max_value:
            max_value = calc_word_value(word)
            max_word = word
    return max_word


def max_test(x, m): return x if x > m else m


# def new_value(words):
#     max_value = 0
#     return(list[lambda x: max_test(calc_word_value(x), max_value), words])


if __name__ == "__main__":
    # print(calc_word_value2("Doug"))
    lll = ['Doug', "sara", "Dianna"]
    # print(new_value(lll))
