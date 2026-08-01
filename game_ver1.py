#!/usr/bin/env python3
import json

USED_WORDS = set()
LAST_LETTER = ''

def load_words():
    with open('words_dictionary.json') as word_file:
        data = json.load(word_file)
    keys = set(data.keys())
    return keys

def game():
    wordBank = load_words()

    while True:
        word = input("Word: ")
        if word == "Safe Word":
            print("Safe word employed! Exiting game.")
            break
        
        first_letter = word[0]
        global LAST_LETTER

        if LAST_LETTER == '':
            LAST_LETTER = word[-1]
        else:
            if LAST_LETTER != first_letter:
                print("The first letter does not match the previous word's last letter." 
                    + f"Try again. Last letter is {LAST_LETTER}.")
                continue

        
        
        # First word
        if not USED_WORDS:
            USED_WORDS.add(word)
            continue

        if word not in USED_WORDS:
            if word in wordBank:
                USED_WORDS.add(word)
                LAST_LETTER = word[-1]
            else:
                print(f"The word {word} does not exist.")
        else:
            print(f"The word: {word} has already been used. Think of another one.")
    return




if __name__ == "__main__":
    # user_name = input("Enter your name: ")
    # print(f"Hello, {user_name}! Launching word game.")
    game()
