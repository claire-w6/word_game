#!/usr/bin/env python3
import json

USED_WORDS = set()
SCORE = 0
LAST_LETTER = ''

def load_words():
    with open('words_dictionary.json') as word_file:
        data = json.load(word_file)
    keys = set(data.keys())
    return keys

def checkWord(wordBank: set, word: str) -> bool:
    first_letter = word[0]
    global LAST_LETTER
    global SCORE

    if LAST_LETTER == '':
        LAST_LETTER = word[-1]
    else:
        if LAST_LETTER != first_letter:
            raise ValueError("The first letter does not match the previous word's last letter. " 
                + f"Try again. Last letter is {LAST_LETTER}.")
    
    # First word
    if not USED_WORDS:
        USED_WORDS.add(word)
        SCORE += 1
        return

    if word not in USED_WORDS:
        if word in wordBank:
            USED_WORDS.add(word)
            SCORE += 1
            LAST_LETTER = word[-1]
        else:
            raise ValueError(f"The word {word} does not exist.")
    else:
        raise ValueError(f"The word {word} has already been used. Think of another one.")

def game():
    wordBank = load_words()

    while True:
        word = input("Word: ")
        if word == "Safe Word":
            print(f"Safe word employed... Exiting game. Game score: {SCORE}")
            break
        try:
            checkWord(wordBank, word)
            print(f"Current score: {SCORE}")
        except ValueError as e:
            print(e)
            continue
        
    return




if __name__ == "__main__":
    game()
