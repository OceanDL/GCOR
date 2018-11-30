import os
from nltk.parse.corenlp import CoreNLPParser

class Parser:

	class __Parser:
        """ Implementation of the singleton class Parser """
        def __init__(self):
            self.parser = CoreNLPParser()
        	self.parser.session.trust_env = False

    # storage for the instance reference
    __instance = None
    
    def __init__(self):
    	# Check whether we already have an instance
        if Parser.__instance is None:
            # Create and remember instance
            Parser.__instance = Parser.__Parser()
          
        # Store instance reference as the only member in the handle
        self.__dict__['_Parser__instance'] = Parser.__instance
        

    def parse(self, sentence):
        return self.parser.raw_parse(sentence)


if __name__ == '__main__':
    parser = Parser()
    sentences = parser.parse((input('Please provide a sentence to parse: ')))
    for line in sentences:
        for sentence in line:
            sentence.draw()

