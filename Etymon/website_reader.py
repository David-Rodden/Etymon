from wiktionaryparser import WiktionaryParser


class Website_Reader:
    def __init__(self, name: str):
        self.etymological_sentence = WiktionaryParser().fetch(name)[0]["etymology"]

    def __repr__(self):
        return self.etymological_sentence


print(Website_Reader("cool"))
