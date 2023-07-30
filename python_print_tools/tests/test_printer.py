#!/usr/bin/env python3

import os.path
import python_print_tools.printer

def test_truncate_path():
    """
    Tests the truncate_path function
    """
    # Test truncating path
    base = os.path.abspath("")
    new_file = os.path.abspath(os.path.join(base, "new_file.txt"))
    truncated = python_print_tools.printer.truncate_path(base, new_file)
    assert truncated == ".../new_file.txt"
    # Test truncating identical path
    assert python_print_tools.printer.truncate_path(base, base) == base
    # Test truncating path in a totally different directory
    truncated = python_print_tools.printer.truncate_path(base, "/non/existant/but/different.txt")
    assert truncated == "/non/existant/but/different.txt"
