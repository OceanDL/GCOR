from collections import Counter, defaultdict, deque
from nltk.parse.generate import generate


def recursive_assemble(tree, grammar):
    # Handle leaves
    if type(tree) == str:
        return tree
    # Get counts for subtree types
    subtree_label_counts = Counter([st.label() for st in tree])
    # Get subtree queue by label
    subtree_label_dict = defaultdict(lambda: deque)
    for st in tree:
        subtree_label_dict[st.label()].append(st)
    # Iterate over sentences in the grammar to find a matching one.
    sentential_form = None
    for sentence in generate(grammar, start=tree.label(), depth=1, n=10000):
        sentence_label_counts = Counter(sentence.split())
        if sentence_label_counts == subtree_label_counts:
            sentential_form = sentence.split()
            break
    # Raise error if no valid sentential form was found
    if sentential_form is None:
        raise ValueError('Did not find a construction for the sentence tree. Tree: {}'.format(tree))
    # Build a list of sentence components
    sentence_components = list()
    for token in sentential_form.split():
        subtree = subtree_label_dict[token].popleft()
        assembled_component = recursive_assemble(subtree, grammar)
        sentence_components.append(assembled_component)
    # join then components
    return ' '.join(sentence_components)

