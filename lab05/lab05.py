## Mutable Lists ##

# Q1
def map(fn, lst):
    """Maps fn onto lst using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> map(lambda x: x * x, original_list)
    >>> original_list
    [25, 1, 4, 0]
    """
    index = 0
    while index < len(lst):
        lst[index] = fn(lst[index])
        index += 1


## Dictionaries ##

# Q3
def replace_all(d, x, y):
    """Replace all occurrences of x as a value (not a key) in d with y.
    >>> d = {3: '3', 'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> replace_all(d, 3, 'poof')
    >>> d == {3: '3', 'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    index = 0
    keys = list(d)
    while index < len(keys):
        if d[keys[index]] == x:
            d[keys[index]] = y
        index += 1

# Q4
def counter(message):
    """ Returns a dictionary of each word in message mapped
    to the number of times it appears in the input string.

    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    word_list = message.split() # .split() returns a list of the words in the string. Try printing it!
    temp = list(set(word_list))
    index = 0
    d = {}
    while index < len(temp):
        d[temp[index]] = word_list.count(temp[index])
        index += 1
    return d


## Trees ##

# Q7
def acorn_finder(t):
    """Returns True if t contains a node with the value 'acorn' and
    False otherwise.

    >>> scrat = tree('acorn')
    >>> acorn_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('acorn')]), tree('branch2')])
    >>> acorn_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> acorn_finder(numbers)
    False
    """
    acorns = []
    def checkAcorn(tr, acorns):
        if is_leaf(tr):
            if label(tr) == 'acorn':
                acorns.append(0)
        chil = children(tr)
        if len(chil) != 0:
            ind = 0
            while ind < len(chil):
                checkAcorn(chil[ind], acorns)
                ind += 1
    checkAcorn(t, acorns)
    return len(acorns) > 0

## Tree ADT ##
def tree(label, children=[]):
    for child in children:
        assert is_tree(child), 'children must be trees'
    return [label] + list(children)


def label(tree):
    return tree[0]


def children(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for child in children(tree):
        if not is_tree(child):
            return False
    return True


def is_leaf(tree):
    return not children(tree)


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the label.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for child in children(t):
        print_tree(child, indent + 1)


def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(child) for child in children(t)])
