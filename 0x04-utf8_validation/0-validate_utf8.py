#!/usr/bin/python3
"""
valid utf8 in a given data.
"""


def validUTF8(data):
    """
    Return true:
    if data is valid utf with chars 1-4 bytes long
    """

    numb = 0

    for n in data:
        bn_result = format(n, '#010b')[-8:]

        if numb == 0:
            for bit in bn_result:
                if bit == '0':
                    break
                numb += 1

            if numb == 0:
                continue

            if numb == 1 or numb > 4:
                return False
        else:
            if not (bn_result[0] == '1' and bn_result[1] == '0'):
                return False

        numb -= 1

    return numb == 0