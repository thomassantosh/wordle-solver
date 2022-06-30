"""
Goal is to find the most common words to initiate a Wordle session based on historical words.
By running the 2022 history through June 29, 2022 through the dictionary, and counting which
words and letters have the highest incidence, we can determine if there are a "better" set of words to
start with.
Results: CATER, SCARE & LAPSE have the highest incidence.
"""
import logging
from collections import Counter
logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

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

def load_wordle_history(source=None):
    wordle_history=[]
    with open(source, 'r') as f:
        words = f.readlines()
        words = [x.replace('\n','') for x in words]
    return words

if __name__ == "__main__":
    wordle_history = load_wordle_history('./wordle_history.txt')
    dictionary_list = load_dictionary('./../dictionary.txt')
    frequency_dict = {}
    for wordle in wordle_history:
        counter = 0
        for word in dictionary_list:
            # Check for same combination of words and letters
            if Counter(word) == Counter(wordle.upper()):
                counter += 1
        frequency_dict[wordle] = counter
    print(f"So far, there are {len(wordle_history)} words in 2022 through 6/29/22...")
    # Order the dictionary
    fd = sorted(frequency_dict.items(), key=lambda x:x[1])
    print(f"Wordle words and their letter commonality with other words:\n {dict(fd)}")
