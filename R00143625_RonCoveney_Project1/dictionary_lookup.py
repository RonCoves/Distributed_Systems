import json
import random


class DictionaryLookup:
    # This class contain methods for creating pangram and checking validity of words

    def __init__(self):
        # initialize dictionaryLookup object with some instance variables

        # read and load all words from file words_dictionary.json to words attribute
        with open("words_dictionary.json") as f:
            self.words = json.load(f)

        # read and load all pangrams from file pangrams.json to pangrams attribute
        with open("pangrams.json") as f:
            self.pangrams = json.load(f)

        self.pangram = None
        self.pangram_chars = None

    def set_pangram(self):
        # this method will initialize attribute pangram and pangram_chars

        # selecting a random word as a pangram from pangrams list
        self.pangram = random.choice(list(self.pangrams.keys())).upper()
        # creating a list of unique characters in the pangram
        self.pangram_chars = list(set(self.pangram))

    def get_pangram(self):
        # this method return pangram in the format XXX[X]XXX where middle character is compulsory character for game
        pangram = ""

        for index, ch in enumerate(self.pangram_chars):
            if index == 3:
                pangram += "[{}] ".format(ch)
            else:
                pangram += "{} ".format(ch)

        return pangram

    def check_pangram_availability(self):
        # method to check if pangram is initialized or not
        if self.pangram:
            return True

    def check_word(self, word):
        # method to check the validity of word and return the message and score according to the rules of game
        if len(word) < 4:
            msg = "Word must be at least 4 characters"
            return msg, 0

        for ch in word.upper():
            if ch not in self.pangram_chars:
                msg = "Invalid word, {} is not in characters to select from".format(
                    ch)
                return msg, 0

        if self.pangram_chars[3] not in word.upper():
            msg = "Invalid word, missing centre letter {}.".format(
                self.pangram_chars[3])
            return msg, 0

        if word.lower() not in self.words:
            msg = "Sorry, that is not a valid word."
            return msg, 0

        if len(word) == 4:
            score = 1
            msg = "Valid word scoring {} points.".format(score)
            return msg, score

        elif len(set(word)) == 7:
            score = len(word) + 7
            msg = "Pandgram! {} points".format(score)
            return msg, score

        elif len(word) > 4:
            score = len(word)
            msg = "Valid word scoring {} points.".format(score)
            return msg, score


# dictionary = DictionaryLookup()
# if (dictionary.check_pangram_availability()):
#     print("there is pangram available")
# else:
#     print("no pangram")
# dictionary.set_pangram()
# if (dictionary.check_pangram_availability()):
#     print("there is pangram available")
# else:
#     print("no pangram")
# print(dictionary.get_pangram())

# word = input("Enter word: ")
# dictionary.check_word(word)
