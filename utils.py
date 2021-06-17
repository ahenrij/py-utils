"""Python utilities functions written for fun.

...

Author
------
    Henri A. <ahenrij@gmail.com>

"""

import math
from pytube import YouTube

def readable_time(time):
    """Returns an human readable time based on input.

    Args:
        time (int): Time in seconds.

    Raises:
        ValueError if time does not belongs to [0, 86399]
    """

    if time < 0 or time > 86399:
        raise ValueError("Invalid range for time in second")

    hours = math.floor(time / (60*60))
    remaining_time = time - hours * (60*60) # when we extract hours
    minutes = math.floor(remaining_time / 60)
    seconds = remaining_time - minutes * 60
    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)


def youtube_download(link:str, format:str="mp4"):
    """Download a youtube video via link"""

    video = YouTube(link)
    stream = video.streams.filter(progressive=True, 
        file_extension=format).order_by('resolution').desc().first()
    stream.download()