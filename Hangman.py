import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)    # Get the letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()        # Letters the user have guessed
    lives = 6

    while len(word_letters) > 0 and lives > 0:

        # Display the letters already used by the user
        print('You have',lives,'lives left and you used letters: ',' '.join(used_letters))

        # Display word (W _ R D)
        wordlist = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ',' '.join(wordlist))

        # Get the letter from the user
        user_letter = input('Guess a letter: ').upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                print('\nYour letter is not in the word')
                lives = lives - 1
        elif user_letter in used_letters:
            print('\nYou have already used the letter',user_letter,'.Guess another letter')
        else:
            print('\nThis is not a valid input. Please provide a letter between alphabets : A to Z')

    # When the len(word_letters)> 0
    if lives == 0 :
        print('Sorry, you died. The word was',word)
    else:
        print('Hurrah! You have guessed the word:',word)

if __name__ == "__main__":
    hangman()