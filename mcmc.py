import math
import random

# We don't care about suits for blackjack
def randomCard():
    card = random.randint(1,13)
    if card > 10:
        card = 10
    return card