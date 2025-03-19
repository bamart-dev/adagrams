from random import randint

def draw_letters():
    # Borrowed from test_wave_01.py; used to build expanded letter pool list.
    LETTER_POOL_FREQUENCIES = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9,
    'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6,
    'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
    }
    letter_pool = []  # will hold expanded letter pool list.
    # iterates through dictionary, adding the appropriate number of letters to
    # 'letter_pool' based on frequency:
    for letter, frequency in LETTER_POOL_FREQUENCIES.items():
        letter_pool += letter * frequency
    hand = []  # will hold the player's drawn hand.

    past_indices = []  # keeps track of what indices have been prev. selected.
    while len(hand) < 10:  # loops until 'hand' is full.
        random_index = randint(0, len(letter_pool) - 1)  # selects random value
        # checks if current random_index has previously been selected:
        if random_index in past_indices:
            continue
        # if above check passes, adds letter to 'hand' and current index to
        # 'past_indices':
        hand += letter_pool[random_index]
        past_indices.append(random_index)

    return hand

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass
