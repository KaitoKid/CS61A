## Extra Questions

# Q4
from math import sqrt
def is_prime_sqrt(n):
    """Tests whether a number N is prime or not. Implement this function
    in O(sqrt(n)) time. You can assume n >= 2

    >>> is_prime_sqrt(2)
    True
    >>> is_prime_sqrt(67092481)
    False
    >>> is_prime_sqrt(524287)
    True
    >>> is_prime_sqrt(2251748274470911)
    False
    >>> is_prime_sqrt(6700417)
    True
    >>> is_prime_sqrt(44895587973889)
    False
    >>> is_prime_sqrt(2147483647)
    True
    >>> is_prime_sqrt(67280421310721)
    True
    """
    # sqrt(k) will give the square root of k as a floating point (decimal)
    "*** YOUR CODE HERE ***"

# Q5
def find_duplicates_k(k, lst):
    """Returns True if there are any duplicates in lst that are within k
    indices apart.

    >>> find_duplicates_k(3, [1, 2, 3, 4, 1])
    False
    >>> find_duplicates_k(4, [1, 2, 3, 4, 1])
    True
    >>> find_duplicates_k(4, [1, 1, 2, 3, 3])
    True
    """
    "*** YOUR CODE HERE ***"

## BST Extra Practice ##

# Q6
def size(tree):
    """ Return the number of entries in the binary tree b.

    >>> b = BinTree(4,
    ...         BinTree(2,
    ...             BinTree(1)),
    ...         BinTree(6,
    ...             BinTree(5)))
    >>> size(b)
    5
    """
    "*** YOUR CODE HERE ***"

# Q7
def tree_to_ordered_link(s):
    """Return an ordered Link containing the elements of tree set s.

    Assume that s is a well-formed binary search tree.

    >>> b = binTree([7, [1, [], [4]], [9]])
    >>> tree_to_ordered_link(b)
    Link(1, Link(4, Link(7, Link(9))))
    """
    "*** YOUR CODE HERE ***"

# Q8
def next_element(t, n):
    """This function takes in a binary search tree T and a number N and
    it returns the smallest element that is greater than N. None if it has
    no such element, or t does not contain n

    >>> t = binTree([8, [3, [1], [6, [4], [7]]], [10, [], [14, [13], []]]])
    >>> next_element(t, 1)
    3
    >>> next_element(t, 3)
    4
    >>> next_element(t, 5)
    >>> next_element(t, 7)
    8
    >>> next_element(t, 10)
    13
    >>> next_element(t, 14)
    >>> result = [1]
    >>> a = next_element(t, 1)
    >>> while a:
    ...   result += [a]
    ...   a = next_element(t, a)
    >>> result
    [1, 3, 4, 6, 7, 8, 10, 13, 14]
    """
    "*** YOUR CODE HERE ***"



# Tree definition
class BinTree:
    empty = ()

    def __init__(self, label, left=empty, right=empty):
        self.label = label
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left == self.empty and self.right == self.empty:
            return 'BinTree({})'.format(repr(self.label))
        left = 'BinTree.empty' if self.left == self.empty else repr(self.left)
        right = 'BinTree.empty' if self.right == self.empty else repr(self.right)
        return 'BinTree({}, {}, {})'.format(repr(self.label), left, right)

def binTree(tupleTree):
    """A convenience method for succinctly constructing binary trees.  The
    empty tuple or list stands for BinTree.empty; (V,) or [V] stands
    for BinTree(V); (V, T1, T2) or [V, T1, T2] stands for
    BinTree(V, binTree(T1), binTree(T2)).
    >>> binTree((3,
    ...          (1, (), [2]),
    ...          (6, [5], [7])))
    BinTree(3, BinTree(1, BinTree.empty, BinTree(2)), BinTree(6, BinTree(5), BinTree(7)))
    """
    if len(tupleTree) == 0:
        return BinTree.empty
    elif len(tupleTree) == 1:
        return BinTree(tupleTree[0])
    else:
        return BinTree(tupleTree[0], binTree(tupleTree[1]), binTree(tupleTree[2]))

###########################################################
# Tree printing functions, kindly provided by Joseph Hui. #
# You do not need to look at these.                       #
###########################################################

def print_bintree(tree):
    print(tree_string(tree))

def tree_string(tree):
    return "\n".join(tree_block(tree)[0])

def tree_block(tree):
    r"""Returns a list of strings, each string being
    one line in a rectangle of text representing the
    tree.
    Also returns the index in the string which is
    centered above the tree's root.

    num_width: The width of the widest number in the tree (100 => 3)
    >>> print(tree_string(binTree( (1, (3, (), [2]), (4, [5], [6])) )))
     -1-
    /   \
    3   4
     \ / \
     2 5 6
    """
    #If no children, just return string
    empty = BinTree.empty
    if tree.left is empty and tree.right is empty:
        return [str(tree.label)], len(str(tree.label))//2
    num_width = len(str(tree.label)) #Width of this tree's label
    #If only right child:
    if tree.left is empty:
        r_block, r_cent = tree_block(tree.right)
        #Add left padding if necessary
        if r_cent < num_width*3/2:
            padding = ' '*((num_width*3)//2-r_cent)
            r_cent += ((num_width*3)//2-r_cent) #Record new center
            for line_index in range(len(r_block)):
                r_block[line_index] = padding+r_block[line_index]

        #Generate top two lines
        t_line = str(tree.label)
        t_line += '-'*(r_cent-len(t_line))
        t_line += ' '*(len(r_block[0])-len(t_line))
        m_line = ' '*r_cent + '\\'
        m_line += ' '*(len(r_block[0])-len(m_line))

        return [t_line, m_line]+r_block, num_width//2
    #If only left child:
    if tree.right is empty:
        l_block, l_cent = tree_block(tree.left)
        #Add right padding if necessary
        if len(l_block[0]) < l_cent+1+num_width:
            padding = ' '*(l_cent+1+num_width-len(l_block[0]))
            for line_index in range(len(l_block)):
                l_block[line_index] = l_block[line_index]+padding
        #Generate lines
        t_line = ' '*(l_cent+1)
        t_line += '-'*(len(l_block[0])-l_cent-1-num_width)
        t_line += str(tree.label)
        m_line = ' '*l_cent+'/'
        m_line += ' '*(len(l_block[0]) - len(m_line))
        return [t_line, m_line]+l_block, len(t_line)-num_width//2
    #Otherwise, has both
    l_block, l_cent = tree_block(tree.left)
    r_block, r_cent = tree_block(tree.right)

    #Pad left block
    spacing = r_cent+len(l_block)-l_cent-2
    padding = ' '*max(1, (spacing-num_width))
    for line_index in range(len(l_block)):
        l_block[line_index] = l_block[line_index]+padding

    #Add left and right blocks
    new_block = []
    for line_index in range(max(len(l_block), len(r_block))):
        new_line = l_block[line_index] if line_index < len(l_block) else ' '*len(l_block[0])
        new_line += r_block[line_index] if line_index < len(r_block) else ' '*len(r_block[0])
        new_block.append(new_line)
    r_cent += len(l_block[0])

    #Generate top lines
    my_cent = (l_cent+r_cent)//2
    t_line = ' '*(l_cent+1)
    t_line += '-'*(my_cent-num_width//2-len(t_line))
    t_line += str(tree.label)
    t_line += '-'*(r_cent-len(t_line))
    t_line += ' '*(len(new_block[0])-len(t_line))

    m_line = ' '*l_cent + '/'
    m_line += ' '*(r_cent-len(m_line)) + '\\'
    m_line += ' '*(len(new_block[0])-len(m_line))

    return [t_line, m_line]+new_block, my_cent

# Linked List Class
class Link:
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s
    Link(1, Link(2, Link(3)))
    >>> len(s)
    3
    >>> s[2]
    3
    >>> s = Link.empty
    >>> len(s)
    0
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)
