# Q2
def if_this_not_that(i_list, this):
    """Define a function which takes a list of integers `i_list` and an integer
    `this`. For each element in `i_list`, print the element if it is larger
    than `this`; otherwise, print the word "that".

    >>> original_list = [1, 2, 3, 4, 5]
    >>> if_this_not_that(original_list, 3)
    that
    that
    that
    4
    5
    """
    for i in i_list:
        if this < i:
            print (i)
        else:
            print ('that')

# Q3
def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """
    "*** YOUR CODE HERE ***"
    return [[i, fn(i)] for i in seq if fn(i) <= upper and fn(i) >= lower]

# Q5
def link_to_list(linked_lst):
    """Return a list that contains the values inside of linked_lst

    >>> link_to_list(empty)
    []
    >>> lst1 = link(1, link(2, link(3, empty)))
    >>> link_to_list(lst1)
    [1, 2, 3]
    """
    lis = []
    while linked_lst != empty:
        lis += [first(linked_lst)]
        linked_lst = rest(linked_lst)
    return lis

# Q6
def insert_at_end(lst, elem):
    """Return a linked list that is the same as lst with elem added
    at the end.

    >>> lst1 = insert_at_end(empty, 1)
    >>> print_link(lst1)
    1
    >>> lst2 = insert_at_end(lst1, 2)
    >>> print_link(lst2)
    1 2
    >>> lst3 = insert_at_end(lst2, 3)
    >>> print_link(lst3)
    1 2 3
    """
    a = empty
    if lst == empty:
        a = link(elem, a)
    else:
        while lst != empty:
            a = link(first(lst), a)
            lst = rest(lst)
        a = link(elem, a)
    return reverse(a)

def reverse(lst):
    new_lst = empty
    while lst != empty:
        new_lst = link(first(lst), new_lst)
        lst = rest(lst)
    return new_lst

# Linked List definition
empty = 'empty'


def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))


def link(first, rest=empty):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]


def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), 'first only applies to linked lists.'
    assert s != empty, 'empty linked list has no first element.'
    return s[0]


def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), 'rest only applies to linked lists.'
    assert s != empty, 'empty linked list has no rest.'
    return s[1]

def print_link(s):
    """Print elements of a linked list s.

    >>> s = link(1, link(2, link(3, empty)))
    >>> print_link(s)
    1 2 3
    """
    line = ''
    while s != empty:
        if line:
            line += ' '
        line += str(first(s))
        s = rest(s)
    print(line)
