from itertools import combinations

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k' ,'l', 'm', 'n', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']

LETTER_BANK = ['l','a','p','e','m','x','g']
MUST_USE = 'g'

WORDS = []

MEGAPLEX = False

def read_file():
    global WORDS

    f = open('wordlist.txt','r')
    contents  = f.read()
    f.close()
    contents_list = contents.split('\n')

    for word in contents_list:
        if len(word) > 3 and 's' not in word:
            WORDS.append(word)


def point_val_word(word):
    global MUST_USE
    global LETTER_BANK
    global MEGAPLEX

    # Does word have MUST_USE
    if MUST_USE not in word:
        return 0

    # Any letter not in bank
    for letter in word:
        if letter not in LETTER_BANK:
            return 0

    # Megaplex
    Mega = True
    for letter in LETTER_BANK:
        if letter not in word:
            Mega = False

    points = 0

    if Mega:
        MEGAPLEX = True
        points = 7

    if len(word) == 4:
        points += 1
    else:
        points += len(word)

    return points


def solve_all_words():
    global WORDS

    points = 0

    for word in WORDS:
        points += point_val_word(word)

    return points


def init(bank, mu):
    global LETTER_BANK
    global MUST_USE
    global MEGAPLEX

    LETTER_BANK = list(bank)
    MUST_USE = mu
    MEGAPLEX = False


def main():
    global letters
    global MEGAPLEX

    read_file()

    max_points = 0
    max_letters = None
    max_must = None

    comb = combinations(letters, 7)

    for c in list(comb):

        for i in range(7):
            init(c, c[i])
            points = solve_all_words()

            print c
            print c[i]
            print max_points

            if not MEGAPLEX:
                break

            if MEGAPLEX and points > max_points:
                max_points = points
                max_letters = c
                max_must = c[i]

            #print max_points

    print max_points
    print max_letters
    print max_must

    #get max point if megaplex reached

main()


























