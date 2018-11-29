from parse import Parser
from nltk.tree import Tree
from nltk.tbl.rule import Rule
from collections import defaultdict


def make_unfiltered_rules_from_corpus():
    parser = Parser()
    parsed_sents = set()
    with open("../corpus.txt", "r") as corpus_file:
        for line in corpus_file.readlines():
            tree = parser.parse(line)
            parsed_sents.add(tree)
    ruleset = set()
    for iterable in parsed_sents:
        for tree in iterable:
            for rule in tree.productions():
                ruleset.add(rule)
    return '\n'.join([str(r) for r in ruleset])


def trim_nonterminals(rules_as_string):
    return '\n'.join([r for r in rules_as_string.split('\n') if "'" not in r])


def join_productions(rules):
    productions = defaultdict(list)
    for rule in rules.splitlines():
        origin, product = rule.split('->')
        origin, product = origin.strip(), product.strip()
        productions[origin].append(product)
    for k in productions:
        productions[k].append("'{}'".format(k))
    return '\n'.join(['{} -> {}'.format(k, ' | '.join(v)) for k, v in productions.items()])


if __name__ == '__main__':
    print('Parsing sentences...')
    raw_rules = make_unfiltered_rules_from_corpus()
    print('Filtering rules...')
    filtered = trim_nonterminals(raw_rules)
    print('Joining productions...')
    joined = join_productions(filtered)
    print('Done!\n')
    print(joined)
    with open('../grammar.txt', 'w') as f:
        f.write(joined)

