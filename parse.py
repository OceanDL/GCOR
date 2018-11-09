import os
os.environ['CLASSPATH'] = "/usr/local/Cellar/stanford-parser/3.9.1/libexec"
from nltk.parse import stanford

class Parser:

    def __init__(self, parser):
        self.parser = stanford.StanfordParser()

    def parse(self, sentence):
        return self.parser.raw_parse_sents(sentence)