"""CSC108 Assignment 2 functions"""

from typing import List

# Used to determine whether to encrypt or decrypt
ENCRYPT = 'e'
DECRYPT = 'd'


def clean_message(message: str) -> str:
    """Return a string with only uppercase letters from message with non-
    alphabetic characters removed.
    
    >>> clean_message('Hello world!')
    'HELLOWORLD'
    >>> clean_message("Python? It's my favourite language.")
    'PYTHONITSMYFAVOURITELANGUAGE'
    >>> clean_message('88test')
    'TEST'
    """
    # WRITE THE BODY OF clean_message HERE
    clean = ''
    for char in message:
        if char.isalpha():
            clean += char
    return clean.upper()


# WRITE THE REST OF YOUR A2 FUNCTIONS HERE

def encrypt_letter(letter: str, keystream: int) -> str:
    ''' Return the result encryption by applying the keystream value 
    to the letter.
    
    Precondition: the letter is all uppercase & alphabet has 26 characters
    
    >>> encrypt_letter('B', 4)
    'F'
    >>> encrypt_letter('G', 20)
    'A'
    >>> encrypt_letter('L', 14)
    'Z'
    '''
    result = (ord(letter) - 64) + keystream
    if result > 26:
        result = result - 26
    return chr(result + 64)


def decrypt_letter(letter: str, keystream: int) -> str:
    ''' Return the result of decryption by applying the keystream value
    to the letter
    
    Precondition: the letter is all uppercase & the alpabet has 26 characters
    
    >>> decrypt_letter('Z', 24) 
    'B'
    >>> decrypt_letter('A', 20)
    'G'
    >>> decrypt_letter('F', 4)
    'B'
    '''
    result = (ord(letter) - 64) - keystream
    if result <= 0:
        result = result + 26
    return chr(result + 64) 


def is_valid_deck(deck1: List[int]) -> bool:
    ''' Return True iff the candidate deck is a valid deck of cards
    
    >>> lists = [1, 2, 3, 4, 5, 6, 7, 8]
    >>> is_valid_deck(lists)
    True
    >>> cards = [34, 1, 46, 12]
    >>> is_valid_deck(cards)
    False
    '''
    deck = deck1[:]
    deck.sort()
    if len(deck) < 3:
        return False
    return deck == list(range(1, len(deck)+1))
        


def swap_cards(deck: List[int], i: int) -> None:
    ''' Swap the the card in deck at index i with the card that follows it,
    if the card is the last in the list, swap it with the first card of the list
    
    >>> deck = [1, 2, 3, 7, 8, 9]
    >>> swap_cards(deck, 0)
    >>> deck
    [2, 1, 3, 7, 8, 9]
    
    >>> swap_cards(deck, 5)
    >>> deck
    [9, 1, 3, 7, 8, 2]
    
    '''
    deck1 = deck[:]
    if i < len(deck) - 1:
        deck[i] = deck1[i+1]
        deck[i+1] = deck1[i]
    elif i == len(deck) -1:
        deck[-1] = deck1[0]
        deck[0] = deck1[-1]
    
    
def get_small_joker_value(deck: List[int]) -> int:
    ''' Return the value of the small joker for the given deck of cards.
    Small joker is the second highers card.
    
    >>> deck = [2, 4, 9, 3, 15, 18]
    >>> get_small_joker_value(deck)
    15
    >>> deck = [3, 6, 1, 7, 8, 9]
    >>> get_small_joker_value(deck)
    8
    '''
    maximum = 0
    second_max = 0
    for num in deck:
        if num > maximum:
            maximum = num
    for num in deck:
        if second_max < num < maximum:
            second_max = num
    return second_max


def get_big_joker_value(deck: List[int]) -> int:
    ''' Return the value of the big joker for the given deck of cards.
    Big joker is the highest card
    
    >>> deck = [2, 6, 4, 8, 3, 12, 18, 28]
    >>> get_big_joker_value(deck)
    28
    
    >>> deck = [1, 2, 4, 6, 7, 8]
    >>> get_big_joker_value(deck)
    8
    '''
    maximum = 0
    for num in deck:
        if num > maximum:
            maximum = num
    return maximum


def move_small_joker(deck: List[int]) -> None:
    ''' Swap the small joker with the card that follows it. 
    Treat deck as circular.
    
    >>> deck = [3, 5, 6, 2, 7, 28, 12, 25, 27, 1, 4, 8]
    >>> move_small_joker(deck)
    >>> deck
    [3, 5, 6, 2, 7, 28, 12, 25, 1, 27, 4, 8]
    
    >>> deck = [2, 4, 6, 7, 8]
    >>> move_small_joker(deck)
    >>> deck
    [2, 4, 6, 8, 7]
    '''
    value = get_small_joker_value(deck)
    i = deck.index(value)
    swap_cards(deck, i)
    
    
def move_big_joker(deck: List[int]) -> None:
    ''' Move big joker two cards down in the deck.
    Treat the deck as circular
    
    >>> deck = [3, 5, 6, 2, 7, 12, 25, 27, 1, 4, 28]
    >>> move_big_joker(deck)
    >>> deck
    [5, 28, 6, 2, 7, 12, 25, 27, 1, 4, 3]
    
    >>> deck = [2, 1, 3, 5, 4]
    >>> move_big_joker(deck)
    >>> deck
    [5, 1, 3, 4, 2]
    '''
    value = get_big_joker_value(deck)
    i = deck.index(value)
    swap_cards(deck, i)
    if i + 1 != len(deck):
        swap_cards(deck, i + 1)
    elif i + 1 == len(deck):
        swap_cards(deck, 0)


def triple_cut(deck: List[int]) -> None:
    ''' Do a triple cut on the deck. 
    Triple cut: cards above the first joker are swapped with the cards below
    the second joker
    
    >>> deck = [3, 5, 6, 2, 7, 28, 12, 25, 27, 1, 4]
    >>> triple_cut(deck)
    >>> deck
    [1, 4, 28, 12, 25, 27, 3, 5, 6, 2, 7]
    
    >>> deck = [1, 2, 5, 8, 3, 4, 9, 6, 7]
    >>> triple_cut(deck)
    >>> deck
    [6, 7, 8, 3, 4, 9, 1, 2, 5]
    '''
    if deck.index(get_big_joker_value(deck)) < \
       deck.index(get_small_joker_value(deck)):
        first_joker = deck.index(get_big_joker_value(deck))
        second_joker = deck.index(get_small_joker_value(deck))
    else:
        first_joker = deck.index(get_small_joker_value(deck))
        second_joker = deck.index(get_big_joker_value(deck))
    
    deck0 = deck[:]
    deck.clear()
    deck += deck0[second_joker + 1:] + deck0[first_joker:second_joker + 1] + \
        deck0[:first_joker]


def insert_top_to_bottom(deck: List[int]) -> None:
    ''' Examine the value of the bottom card of the deck;
    move that many cards from the top of the deck to the bottom,
    inserting them just above the bottom card.
    
    Special case: if the bottom card is big joker, use the value of small joker
    as the number of cards
    
    >>> deck = [1, 2, 3, 4, 5, 12, 6, 11, 7, 8, 10, 9]
    >>> insert_top_to_bottom(deck)
    >>> deck
    [8, 10, 1, 2, 3, 4, 5, 12, 6, 11, 7, 9]
    
    >>> deck = [1, 4, 2, 5, 6, 7, 3]
    >>> insert_top_to_bottom(deck)
    >>> deck
    [5, 6, 7, 1, 4, 2, 3]
    '''
    if deck[-1] != get_big_joker_value(deck):
        value = deck[-1]
        deck0 = deck[:]
        deck.clear()
        deck += deck0[value : -1] + deck0[:value] + [value]
    else:
        value = get_small_joker_value(deck)
        deck0 = deck[:]
        deck.clear()
        deck += deck0[value : -1] + deck0[:value] + [deck0[-1]]        


def get_card_at_top_index(deck: List[int]) -> int:
    ''' Return the card in the deck at an index of the value of the top card.
    This will be our keystream value.
    
    >>> deck = [8, 10, 1, 2, 3, 4, 5, 12, 6, 11, 7, 9]
    >>> get_card_at_top_index(deck)
    6
    
    >>> deck = [1, 4, 2, 5, 6, 7, 3]
    >>> get_card_at_top_index(deck)
    4
    '''
    i = deck[0]
    if i != get_big_joker_value(deck):
        if deck[i] in [get_big_joker_value(deck), get_small_joker_value(deck)]:
            return get_next_keystream_value(deck)
        return deck[i]
    else:
        i = get_small_joker_value(deck)
        if deck[i] in [get_big_joker_value(deck), get_small_joker_value(deck)]:
            return get_next_keystream_value(deck)
        return deck[i]
        
            


def get_next_keystream_value(deck: List[int]) -> int:
    ''' Return the next valid keystream value by repeating the 5 steps of 
    the algorithm
    
    >>> deck = [8, 10, 1, 2, 3, 4, 5, 12, 6, 11, 7, 9]
    >>> get_next_keystream_value(deck)
    6
    
    >>> deck = [1, 4, 2, 5, 6, 7, 3]
    >>> get_next_keystream_value(deck)
    3
    '''
    move_small_joker(deck)
    move_big_joker(deck)
    triple_cut(deck)
    insert_top_to_bottom(deck)
    card = get_card_at_top_index(deck)
    return card
    

def process_messages(deck: List[int], messages: List[str], act: str) -> \
    List[str]:
    ''' Return a list of encrypted or decrypted messages using the deck
    depending on the act
    
    >>> deck = [8, 10, 1, 2, 3, 4, 5, 12, 6, 11, 7, 9]
    >>> messages = ['Hello', 'Is this correct?', 'Help, if no']
    >>> process_messages(deck, messages, ENCRYPT)
    ['NGQPU', 'KTZQKXHWSTIFU', 'RJOWLKXV']
    
    >>> deck = [2, 5, 1, 6, 8, 9, 7, 4, 3, 10, 11, 14, 12, 13]
    >>> messages = ['OUHUWSY']
    >>> process_messages(deck, messages, DECRYPT)
    ['ITWORKS']
    '''
    words = []
    for message in messages:
        message = clean_message(message)
        word = ''
        for char in message:
            key = get_next_keystream_value(deck)
            if act == ENCRYPT:
                word += encrypt_letter(char, key)
            else:
                res = decrypt_letter(char, key)
                word += res
        words += [word]
    return words
    
    
    



# This if statement should always be the last thing in the file, below all of
# your functions:
if __name__ == '__main__':
    """Did you know that you can get Python to automatically run and check
    your docstring examples? These examples are called "doctests".

    To make this happen, just run this file! The two lines below do all
    the work.

    For each doctest, Python does the function call and then compares the
    output to your expected result.
    
    NOTE: your docstrings MUST be properly formatted for this to work!
    In particular, you need a space after each >>>. Otherwise Python won't
    be able to detect the example.
    """

    import doctest
    doctest.testmod()