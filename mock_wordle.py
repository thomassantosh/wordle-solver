"""Mock wordle script"""
import random
import logging
#logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk),end="")
def prYellow(skk): print("\033[93m{}\033[00m" .format(skk),end="")
def prLightGray(skk): print("\033[97m{}\033[00m" .format(skk),end="")

def load_dictionary(source=None):
    """Dictionary of values"""
    dictionary_list = []
    with open(source, 'r') as f:
        words = f.readlines()
        for word in words:
            word = word.replace('\n','')
            dictionary_list.append(word)
    return dictionary_list

def wordle_word(dictionary=None):
    """Select wordle word, which is a five-letter word"""
    logging.info(f"Length of dictionary: {len(dictionary)}")
    wordle_words = [word for word in dictionary if len(word)==5]
    logging.info(f"Length of five-letter words in dictionary: {len(wordle_words)}")
    selected_word = random.choice(wordle_words).upper()
    return selected_word

def guess_word(word=None):
    """Iteration through six guesses for five-letter words."""
    for val in range(6):
        guess = str( input("\nGuess the word: ") ).upper()

        # Check if a five-letter word and alphanumeric
        if guess.isalpha() and len(guess)==5:
            logging.info(f"Submitted guess is: {guess}")
            pass
        else:
            logging.info(f"Submitted guess is: {guess} but not five letters, or alphanumeric.")
            break

        # Absolute test
        if word == guess:
            print("Got the word. Great guess!")
            break
        else:
            for i,letter in enumerate(guess):
                if guess[i] == word[i]:
                    prGreen(f"{letter}")
                elif letter in word:
                    prYellow(f"{letter}")
                else:
                    prLightGray(f"{letter}")

        # Exhausted attempts
        if val == 5:
            print(f"""
            {50*'-'}
            Guess limit reached. 
            Six tries over! Correct word is {word}.
            {50*'-'}
            """
            )

def main():
    """Main operational flow"""
    dictionary_list = load_dictionary(source='dictionary.txt')
    word = wordle_word(dictionary_list)
    guess_word(word)

if __name__ == "__main__":
    main()
