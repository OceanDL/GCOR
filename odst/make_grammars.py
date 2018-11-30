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
    # Get lists of productions for each non-terminal
    for rule in rules.splitlines():
        origin, product = rule.split('->')
        origin, product = origin.strip(), product.strip()
        productions[origin].append(product)
    all_nonterminals = set()
    for v in productions.values():
        for prod in v:
            all_nonterminals.update(prod.split())
    for nt in all_nonterminals:
        # Trigger the creation of default object for all non-terminals in
        # the grammar
        productions[nt]
    for k in productions:
        productions[k].append("'{}'".format(k))
    return '\n'.join(['{} -> {}'.format(k, ' | '.join(v)) for k, v in productions.items()])


def escape_specials(rules):
    rules = rules.replace('. ', 'PUNC_PERIOD ')
    rules = rules.replace(', ', 'PUNC_COMMA ')
    rules = rules.replace('PRP$ ', 'PRPS ')
    return rules

if __name__ == '__main__':
    print('Parsing sentences...')
    raw_rules = make_unfiltered_rules_from_corpus()
    print('Filtering rules...')
    filtered = trim_nonterminals(raw_rules)
    print('Joining productions...')
    joined = join_productions(filtered)
    print('Handling special characters in non-terminals...')
    escaped = escape_specials(joined)
    print('Done!\n')
    print()
    print(escaped)
    with open('../grammar_en.txt', 'w') as f:
        f.write(escaped)

