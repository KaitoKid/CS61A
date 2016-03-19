## Sets + Orders of Growth ##

# Q2
def find_duplicates(lst):
    """Returns True if lst has any duplicates and False if it does not.

    >>> find_duplicates([1, 2, 3, 4, 5])
    False
    >>> find_duplicates([1, 2, 3, 4, 2])
    True
    >>> find_duplicates(list(range(100000)) + [-1]) # make sure you have linear time
    False
    """
    a = set(lst)
    b = sorted(a)
    return len(b) != len(lst)

# Q3
def pow(n,k):
    """Computes n^k.

    >>> pow(2, 3)
    8
    >>> pow(4, 2)
    16
    >>> a = pow(2, 100000000) # make sure you have log time
    """
    if (k == 0):
        return 1
    if (k == 1):
        return n
    if (k%2 == 0):
        return pow(n*n, k/2)
    else:
        return n * pow(n*n, k/2)
