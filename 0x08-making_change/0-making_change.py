#!/usr/bin/python3

"""
Given a pile of coins of different values,
determine the fewest number of coins needed
to meet a given amount total
"""


def makeChange(coins, total):
    """
    Args: coins (list), total (int)
    returns: fewest coins needed (int)
    """

    if total <= 0:
        return 0
    
    number_of_coins = 0
    coins.sort(reverse=True)

    for coin in coins:
        while coin <= total:
            total -= coin
            number_of_coins += 1

    if total == 0:
        return number_of_coins
    return -1