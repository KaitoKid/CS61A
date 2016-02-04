"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 0.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN Question 1
    final_score, pig_out = 0, False
    while (num_rolls > 0):
        roll = dice()
        if roll == 1:
            pig_out = True
        final_score += roll
        num_rolls -= 1

    if pig_out:
        return 0

    return final_score
    # END Question 1

def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    # Assume opponent_score is less than 100
    # Implement free_bacon and hog_prime

    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'

    # BEGIN Question 2

    # Make hog_prime
    def is_prime (number):
        if number < 2:
            return False
        temp = 2
        while (temp < number):
            if number % temp == 0:
                return False
            temp += 1
        return True

    def next_prime (prime):
        temp = prime + 1
        while True:
            if is_prime(temp):
                return temp
            temp += 1

    def hog_prime(number):
        if is_prime(number):
            return next_prime(number)
        return number

    # Make list of opponent_score
    opponent_score_list = list(map(int, str(opponent_score)))

    # Check free_bacon
    if num_rolls == 0:
        return hog_prime(max(opponent_score_list) + 1)

    return hog_prime(roll_dice(num_rolls, dice))
    # END Question 2


def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    # BEGIN Question 3
    # Hog wild
    if (score + opponent_score)%7 == 0:
        return four_sided
    return six_sided
    # END Question 3


def is_swap(score0, score1):
    """Returns whether the last two digits of SCORE0 and SCORE1 are reversed
    versions of each other, such as 19 and 91.
    """
    # BEGIN Question 4
    # Swine swap
    a = score0
    b = a % 10
    a = a - b
    a = a // 10
    c = a % 10
    d = score1
    e = d%10
    d = d-e
    d = d//10
    f = d%10
    if b == f and c == e:
        return True
    else:
        return False
    # END Question 4


def other(player):
    """Return the other player, for a player PLAYER numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - player


def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN Question 5

    s0, s1 = score0, score1

    # Check if anyone won
    def is_win(num1, num2):
        return (num1 >= goal) or (num2 >= goal)


    while True:
    # Player moves
        dice = select_dice(s0, s1)
        strat = strategy0(s0, s1)

        # Actually rolls the dice
        result = take_turn(strat, s1, dice)
        # Piggy Back
        if (result == 0):
            s1 += strat
        s0 += result

        # swap
        if is_swap(s0, s1):
            s2 = s1
            s1 = s0
            s0 = s2

        if is_win(s0, s1):
            return s0, s1


    # Other moves
        dice = select_dice(s1, s0)
        strat = strategy1(s1, s0)
        # Actually rolls the dice
        result = take_turn(strat, s0, dice)
        # Piggy Back
        if (result == 0):
            s0 += strat
        s1 += result

        # swap
        if is_swap(s0, s1):
            s2 = s1
            s1 = s0
            s0 = s2

        if is_win(s0, s1):
            return s0, s1

    # END Question 5
    return s0, s1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n

    return strategy


# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    5.5

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 0.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 5.5.
    Note that the last example uses roll_dice so the hogtimus prime rule does
    not apply.
    """
    # BEGIN Question 6
    def foo(*args):
        temp = num_samples
        sum = 0
        while temp!= 0:
            sum += fn(*args)
            temp -= 1
        return sum / num_samples
    return foo
    # END Question 6


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN Question 7
    i = 1
    averagedList = []
    while (i < 11):
        averagedList.append(make_averaged(roll_dice, 1000)(i, dice))
        i += 1
    return averagedList.index(max(averagedList)) + 1
    # END Question 7


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    "*** You may add additional experiments as you wish ***"


# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 8
    if take_turn(0, opponent_score) >= margin:
        return 0
    else:
        return num_rolls  # Replace this statement
    # END Question 8


def swap_strategy(score, opponent_score, num_rolls=5):
    """This strategy rolls 0 dice when it results in a beneficial swap and
    rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 9
    if opponent_score > score and is_swap(score + take_turn(0, opponent_score), opponent_score) and ((score + take_turn(0, opponent_score)) != opponent_score):
        return 0
    return num_rolls
    # END Question 9


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN Question 10
    "*** REPLACE THIS LINE ***"
    return 5  # Replace this statement
    # END Question 10


##########################
# Command Line Interface #
##########################


# Note: Functions in this section do not need to be changed. They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
