import re
from difflib import SequenceMatcher

from wiktionaryparser import WiktionaryParser


class WordNode:
    def __init__(self, word: str, child):
        self.word = word
        self.child = child

    def set_child(self, word: str):
        self.child = WordNode(word)


class Website_Reader:
    def __init__(self, name: str):
        self.name = name
        self.etymological_sentence = WiktionaryParser().fetch(name)

    def __repr__(self):
        return "this -> " + str(len(self.etymological_sentence))

    def __get_first_type(self):
        return self.etymological_sentence[0]["definitions"][0]["partOfSpeech"][0]

    def __get_first_etymology(self):
        return self.etymological_sentence[0]["etymology"] if self.etymological_sentence else None

    def get_sorted_etymological_background(self):
        return sorted(re.split("\s+", re.sub("([^\s\w]|_)+", "", self.__get_first_etymology())),
                      key=lambda x: SequenceMatcher(None, self.name, x).ratio(), reverse=True)


print(Website_Reader("wolf").get_sorted_etymological_background())
