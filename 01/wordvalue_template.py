from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as infile:
        return [item.replace("\n", "") for item in list(infile)]


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    total_score = 0
    for letter in word.upper():
        total_score += LETTER_SCORES.get(letter, 0)
    return total_score

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if not words:
        words = load_words()
    highest_score = 0
    highest_name = ""
    for word in words:
        temp_highest = calc_word_value(word)
        if temp_highest > highest_score:
            highest_score = temp_highest
            highest_name = word
    return highest_name



if __name__ == "__main__":
    print(max_word_value(('bob', 'julian', 'pybites', 'quit', 'barbeque')))
