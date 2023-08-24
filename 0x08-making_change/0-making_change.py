#!/usr/bin/python3
"""
min change
"""


def makeChange(coins, total):
    """
    get minimum change of a value using dynamic programing
    """
    nums = [float('inf') for x in range(total + 1)]
    nums[0] = 0

    for coin in coins:
        for amount in range(len(nums)):
            if coin <= amount:
                nums[amount] = min(nums[amount], 1 + nums[amount - coin])

    return nums[total] if nums[total] != float('inf') else -1
