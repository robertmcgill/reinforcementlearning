import math
import random

# We don't care about suits for blackjack
def randomCard():
    card = random.randint(1,13)
    if card > 10:
        card = 10
    return card

# A hand is just a tuple.
# Ex.: (14, False), a total card value of 14 without a useable ace
# If the Ace can be an 11 without busting the hand, it's useable
def useable_ace(hand):
    val, ace = hand
    return ((ace) and ((val + 10) <= 21))

def totalValue(hand):
    val, ace = hand
    if (useable_ace(hand)):
        return (val + 10)
    else:
        return val