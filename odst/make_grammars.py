from parse import Parser
from nltk.tree import Tree
from nltk.tbl.rule import Rule

parser = Parser()
parsedSents = set()
corpusFile = open("../corpus.txt", "r")

for line in corpusFile.readlines():
    tree = parser.parse(line)
    parsedSents.add(tree)

ruleset = set()

tree: Tree
rule: Rule
for iterable in parsedSents:
    for tree in iterable:
        for rule in tree.productions():
            ruleset.add(rule)

grammars = open("../grammars.txt", mode = "r+", encoding = "utf-8")

for rule in ruleset:
    grammars.write(rule.__str__() + "\n")