import assembly
import parse
from nltk import CFG
from nltk.parse.generate import generate as sentgen
from nltk.grammar import Nonterminal


if __name__ == '__main__':
    parser = parse.Parser()
    tree = [l for l in parser.parse("Peter Piper picked a peck of pickled peppers.")][0]
    tree.pretty_print()
    with open('../grammar_en.txt') as f:
        grammar = f.read()
    cfg = CFG.fromstring(grammar)
    result = assembly.recursive_assemble(tree, cfg)
    print(result)

