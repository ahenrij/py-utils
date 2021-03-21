"""Tests for utils functions.
"""
import utils

def test_readable_time():
    assert utils.readable_time(0)       == "00:00:00"
    assert utils.readable_time(5)       == "00:00:05"
    assert utils.readable_time(60)      == "00:01:00"
    assert utils.readable_time(3600)    == "01:00:00"
    assert utils.readable_time(14700)   == "04:05:00"
    assert utils.readable_time(86399)   == "23:59:59"