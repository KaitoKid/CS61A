from time import time
from timeit import timeit
from random import *

print("""
We are going to run a timing test on list and set.
In particular, you need to specify two number, size and prob.
Then the program will initiate a list containing number from 0
to size, and check a random membership for prob times. For
example:

size = 5, prob = 3

Then this program will initiate the list (0, 1, 2, 3, 4), and
randomly pick 3 items from [0, 4] and check their memberships,
and print the time of this operation. Then it will initiate the
list contianing the same number [0, 4], and check the memberships for
the same 3 random items.
""")

size = input('Enter the size of the size/set: ')
prob_len = input('Enter the amount of lookups: ')

try:
    size = int(size)
    prob_len = int(prob_len)
except ValueError:
    print("You need to enter integers for size and prob")
    exit(1)

lst = [i for i in range(size)]
prob = [choice(lst) for i in range(prob_len)]

print("All set! size = {0}, prob = {1}".format(str(size), str(prob_len)))

print("Starting the test on the list")
t0 = time()
for i in prob:
    i in lst
t1 = time() - t0
print("spent {0:.6f}s".format(t1))

lst = set(lst)
print("Starting the test on the set")
t0 = time()
for i in prob:
    i in lst
t1 = time() - t0
print("spent {0:.6f}s".format(t1))
