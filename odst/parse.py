import os
from nltk.parse.corenlp import CoreNLPParser

class Parser:

    def __init__(self):
        self.parser = CoreNLPParser()
        self.parser.session.trust_env = False

    def parse(self, sentence):
        return self.parser.raw_parse(sentence)

# parser = Parser()
# sentences = parser.parse(("Hello, My name is Melroy."))
# print(sentences)

# # GUI
# for line in sentences:
#     for sentence in line:
#         sentence.draw()