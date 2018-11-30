from collections import Counter, defaultdict, deque
from nltk.parse.generate import generate
from nltk.grammar import Nonterminal


def recursive_assemble(tree, grammar):
    # Handle leaves
    if type(tree) == str:
        return tree
    if tree.height() <= 2:
        return ' '.join([ch for ch in tree])
    # Get counts for subtree types
    subtree_label_counts = Counter([st if type(st) == str else st.label() for st in tree])
    # Get subtree queue by label
    subtree_label_dict = defaultdict(lambda: deque())
    for st in tree:
        subtree_label_dict[st if type(st) == str else st.label()].append(st)
    # Iterate over sentences in the grammar to find a matching one.
    sentential_form = None
    for sentence in generate(grammar, start=Nonterminal(tree.label()), depth=3, n=10000):
        sentence_label_counts = Counter(sentence)
        if sentence_label_counts == subtree_label_counts:
            sentential_form = sentence
            break
    # Raise error if no valid sentential form was found
    if sentential_form is None:
        raise ValueError('Did not find a construction for the sentence tree. Tree: {}'.format(tree))
    print('Using production <{}> for node {}.'.format(' '.join(sentential_form), tree.label()))
    # Build a list of sentence components
    sentence_components = list()
    for token in sentential_form:
        subtree = subtree_label_dict[token].popleft()
        assembled_component = recursive_assemble(subtree, grammar)
        sentence_components.append(assembled_component)
    # Return the joined components
    return ' '.join(sentence_components)

