#!/usr/bin/python3
"""
prime game
"""


def isWinner(x, nums):
    """
    x - number of rounds
    nums - array of n
    if winner cant be determined return none
    """

    """check  if number of rounds  and array is not 0"""
    if not nums or x < 1:
        return None

    n = max(nums)
    m = max(n + 1, 2)
    filt = [True for _ in range(m)]

    for i in range(2, int(pow(n, 0.5)) + 1):
        if not filt[i]:
            continue

        for j in range(i*i, n + 1, i):
            filt[j] = False

    filt[0] = filt[1] = False

    c = 0

    for i in range(len(filt)):
        if filt[i]:
            c += 1
        filt[i] = c

    winner = ''
    p1 = 0
    ln = len(nums)

    # check if its a prime nmber and if it the last one
    for n in nums:
        p1 += filt[n] % 2 == 1
    if p1 * 2 == ln:
        winner = None
    elif p1 * 2 > ln:
        winner = "Maria"
    else:
        winner = "Ben"
    return winner
