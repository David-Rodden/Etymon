from wiktionaryparser import WiktionaryParser


class Website_Reader:
    def __init__(self, name: str):
        self.etymological_sentence = WiktionaryParser().fetch(name)

    def __repr__(self):
        return self.etymological_sentence

    def get_first_etymology(self):
        return self.etymological_sentence[0]["etymology"]


print(Website_Reader("first").get_first_etymology())
