#!/usr/bin/python3
""" lock box challenge"""


def canUnlockAll(boxes):
    """ determines if all boxes can be opened
     check if we can get any/all the keys from the unlocked box at [0]
     check if any indexes of the other box match with the key in 0 **loop**
     if there is a match it will become true
     then append the index of the new box to the list
     repeat the loop till alllboxes are opened
    """

    unlocked = []
    keys = set()
    a = len(boxes)
    i = 0

    while i < a:
        temp = i
        unlocked.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < a and key not in unlocked:
                i = key
                break
        if temp != i:
            continue
        else:
            break

    for i in range(a):
        if i not in unlocked and i != 0:
            return False
    return True
