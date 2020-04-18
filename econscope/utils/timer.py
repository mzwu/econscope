""""
Timer for Event Logging
"""
import time
PRECISION = {
    "second": 0,
    "sec": 0,
    "s": 0,
    "millisecond": 3,
    "msec": 3,
    "ms": 3,
    "microsecond": 6,
    "usec": 6,
    "us": 6,
}


class Timer(object):
    """
    A simple Timer, ideal for recording event of sequence
    """
    def __init__(self, name="Unknown Timer"):
        self.name = name

    @staticmethod
    def get_epoch(precision="sec"):
        """
        Return EPOCH time in seconds
        :return:
        """
        if isinstance(precision, str):
            prec = PRECISION.get(precision.lower(), 0)
        elif isinstance(precision, int):
            prec = precision
            prec = min(6, prec)
            prec = max(0, prec)
        else:
            prec = 0
        fmt = "%%%0.1ff" % (prec/10)
        ts = fmt % time.time()
        if prec == 0:
            return int(ts)
        else:
            return float(ts)
