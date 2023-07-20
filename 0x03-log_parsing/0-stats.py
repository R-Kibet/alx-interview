#!/usr/bin/python3
""" log parsing """

from sys import stdin


def log_prs(codes, t_size):
    """ print the output """
    print("File size: {}".format(t_size))

    for k, vl in sorted(codes.items()):
        if vl != 0:
            print("{}: {}".format(k, vl))


if __name__ == '__main__':
    codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }

    t_size = 0

    try:
        cnt = 0
        for line in stdin:
            arg = line.split()
            if len(arg) > 6:
                stat = arg[-2]
                f_size = arg[-1]
                t_size += int(f_size)
                if stat in codes:
                    cnt += 1
                    codes[stat] += 1
                    if cnt % 10 == 0:
                        log_prs(codes, t_size)
    except KeyboardInterrupt:
        log_prs(codes, t_size)
        raise
    else:
        log_prs(codes, t_size)
