from utils import *

# Q1
from math import sqrt
def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    return sqrt((get_lat(city1) - get_lat(city2))**2 + (get_lon(city1) - get_lon(city2))**2)

# Q2
def closer_city(lat, lon, city1, city2):
    """ Returns the name of either city1 or city2, whichever is closest
        to coordinate (lat, lon).

        >>> berkeley = make_city('Berkeley', 37.87, 112.26)
        >>> stanford = make_city('Stanford', 34.05, 118.25)
        >>> closer_city(38.33, 121.44, berkeley, stanford)
        'Stanford'
        >>> bucharest = make_city('Bucharest', 44.43, 26.10)
        >>> vienna = make_city('Vienna', 48.20, 16.37)
        >>> closer_city(41.29, 174.78, bucharest, vienna)
        'Bucharest'
    """
    distance_one = sqrt((get_lat(city1) - lat)**2 + (get_lon(city1) - lon)**2)
    distance_two = sqrt((get_lat(city2) - lat)**2 + (get_lon(city2) - lon)**2)
    if distance_one < distance_two:
        return get_name(city1)
    return get_name(city2)
# Q3
def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    final_b = 0
    while a > 0:
        final_b = final_b + b
        a = a - 1
    return final_b + c

# Q4
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def counter(i):
        if i < n:
            if n%i == 0:
                return False
            return counter(i + 1)
        return True
    return counter(2)

# Q5
def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    def calculator(i, f_calc, total):
        if i <= n:
            return calculator(i+2, f_calc, total + f_calc(i))
        return total
    return calculator(1, odd_term, 0) + calculator(2, even_term, 0)
