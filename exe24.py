def break_words(stuf):
    #This function returns broken break_words
    words = stuf.split(" ")
    return words

def sort_words(words):
    """This function returns sorted words"""
    return sorted(words)

def print_first_word(stuff):
    """prints the first words of a sentence after poping it coffee"""
    wordss = stuff.pop(0)
    print(wordss)

def print_last_word(words):
    """ print the last words of a sentence"""
    word = words.pop(-1)
    print(word)

def sort_sentences(sentence):
    """this one sorts words in a sentence"""
    word = break_words(sentence)
    sort_words(word)

def print_first_and_last(sentence):
    """this prints the first word and the last word of a sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def pritn_first_and_lastsorted_sentence(sentence):
    """prints the first and last sorted words of a sentence"""
    words = sort_sentences(sentence)
    print_first_and_lastwords(words)

def print_first_and_lastwords(words):
    print_first_word(words)
    print_last_word(words)


def print_first_and_lastsorted_words(sentence):
    words = sort_words(sentence)
    print_first_word(words)
    print_last_word(words)


def sort_words(words):
    return sorted(words)
