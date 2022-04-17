"""Script to generate wordle suggestions. This is to provide suggestions
while playing the real game."""
import random
import logging
from collections import Counter
logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))

def load_dictionary(source=None):
    """Dictionary of values"""
    dictionary_list = []
    with open(source, 'r') as f:
        words = f.readlines()
        for word in words:
            word = word.replace('\n','')
            dictionary_list.append(word)
    wordle_words = [word.upper() for word in dictionary_list if len(word)==5]
    logging.info(f"Number of five-letter words in dictionary: {len(wordle_words)}")
    return wordle_words

def wordle_solver(word_list=None):
    """Dictionary filtering mechanism"""
    logging.info(prYellow(f"""
    {100*'-'}

    Note the following:
     Enter 'c' if the letter is in the correct position, i.e. green.
     Enter 'l' if the letter is in the word, but not the correct position, i.e. yellow.
     Enter 'n' if the letter is not in the word.

     As an example, if the word is 'SCARE', and none of the words are in the word, enter 'nnnnn'.
     Alternatively, if the word is correct, enter 'ccccc'.
    {100*'-'}
            """))
    for i in range(6):
        guess = str(input(f"What is guess number {i}:")).upper()
        logging.info(f"Inputted guess: {guess}")

        # Logic to account for when a letter in a word can duplicate, and have >1 response
        # For ex, "WHICH" has 2 Hs. "CHEEK" has only 1. Wordle response: NCNLN. H has 2 responses.
        # The specific case that came up included the following process:
            # NYMPH : nnnnl
            # GOURD : nnnnn
            # BLAST : nnnnn
            # WHICH : ncnln
            # CHEEK : ccccc (lucky guess)

        # Identify the letters that have duplicates
        duplicate_list = []
        test_for_counter = dict(Counter(guess))
        for key,val in test_for_counter.items():
            if val > 1:
                duplicate_list.append(key)
                logging.info(f"Duplicate values found. See list: {duplicate_list}")

        # Get wordle feedback
        guess_result = str(input(f"What is the wordle feedback for {i}?")).upper()
        logging.info(f"Inputted guess result: {guess_result}")

        # Break if the right word
        if guess_result == 'CCCCC':
            logging.info(prGreen(f"Congrats! Word is {guess}."))
            break

        # If duplicate list exists, substitute any Ns for duplicate with Ls
        if len(duplicate_list) != 0:
            guess_result_list = list(guess_result)
            for pos,letter in enumerate(guess):
                if letter in duplicate_list:
                    if guess_result[pos] == 'N':
                        guess_result_list[pos] = 'L'
            guess_result = ''.join(guess_result_list)
            logging.info(f"Revised guess result: {guess_result}")

        # Filter word list
        for j,val in enumerate(guess_result):
            match val:
                case "C":
                    word_list = [word for word in word_list if word[j]==guess[j]]
                case "N":
                    word_list= [word for word in word_list if guess[j] not in word]
                case "L":
                    word_list = [word for word in word_list if guess[j] in word]
        logging.info(f"Length of dictionary: {len(word_list)}")

        # Show dense words to increase letter coverage
        dense_list = []
        for word in word_list:
            if len(set(word)) == 5:
                dense_list.append(word)

        logging.info(f"Dense words to try: {dense_list}")

        # Take out the actual guess from word list if proceeding
        if guess in word_list:
            word_list.remove(guess)

        # Show word list if less than or equal to five words
        if len(word_list) <= 5:
            logging.info(prCyan(f"Current word list: {word_list}"))

        logging.info(prCyan(f"Final suggested word list: {word_list}"))


def main():
    """Main operational flow"""
    words = load_dictionary(source='dictionary.txt')
    suggested_words = wordle_solver(words)

if __name__ == "__main__":
    main()
