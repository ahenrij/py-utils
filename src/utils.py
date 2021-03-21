"""Python utilities functions written for fun.

...

Author
------
    Henri A. <ahenrij@gmail.com>

"""

import math


def readable_time(time):
    """Give an human readable time based on input.

    Args:
        time (int): Time in seconds.
    """

    hours = math.floor(time / (60*60))
    time -= hours * (60*60)
    minutes = math.floor(time / 60)
    seconds = time - minutes * 60
    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)


if __name__ == '__main__':
    print(readable_time(14700))
