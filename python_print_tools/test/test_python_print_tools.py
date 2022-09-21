#!/usr/bin/env python3

from os.path import abspath, join
from python_print_tools.main.python_print_tools import truncate_path

def test_truncate_path():
    """
    Tests the truncate_path function
    """
    # Test truncating path
    base = abspath("")
    new_file = abspath(join(base, "new_file.txt"))
    truncated = truncate_path(base, new_file)
    assert truncated == ".../new_file.txt"
    # Test truncating identical path
    assert truncate_path(base, base) == base
    # Test truncating path in a totally different directory
    truncated = truncate_path(base, "/non/existant/but/different.txt")
    assert truncated == "/non/existant/but/different.txt"
