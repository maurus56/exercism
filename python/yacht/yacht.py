from collections import Counter

def count(num):
    return lambda dice: num * Counter(dice)[num] 

def score(dice, category):
    return category(dice)

# Score categories
# Change the values as you see fit
YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0
ONES = count(1)
TWOS = count(2)
THREES = count(3)
FOURS = count(4)
FIVES = count(5)
SIXES = count(6)
FULL_HOUSE = lambda dice: sum(dice) if sorted(Counter(dice).values()) == [2,3] else 0
FOUR_OF_A_KIND = lambda dice: 4 * Counter(dice).most_common(1)[0][0] if Counter(dice).pop(Counter(dice).most_common(1)[0][0]) >= 4 else 0
LITTLE_STRAIGHT = lambda dice: 30 if len(Counter(dice).values()) == 5 and sum(Counter(dice).keys()) == 15 else 0
BIG_STRAIGHT = lambda dice: 30 if len(Counter(dice).values()) == 5 and sum(Counter(dice).keys()) == 20 else 0
CHOICE = lambda dice: sum(dice)