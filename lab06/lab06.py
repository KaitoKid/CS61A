## Lab 6: OOP and Nonlocal ##

# Question 1
def vending_machine(snacks):
    """Cycles through list of snacks.

    >>> vender = vending_machine(['chips', 'chocolate', 'popcorn'])
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(['brownie'])
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    "*** YOUR CODE HERE ***"
    slist = snacks
    index = 0
    called = False
    def cycler():
        nonlocal slist
        nonlocal index
        nonlocal called
        if not called:
            called = True
            return slist[index]
        index += 1
        if index == len(slist):
            index = 0
        return slist[index]
    return cycler
