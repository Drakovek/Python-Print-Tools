#!/usr/bin/env python3

import python_print_tools as ppt
from os.path import abspath, join


def test_truncate_path():
    """
    Tests the truncate_path function
    """
    # Test truncating path
    base = abspath("")
    new_file = abspath(join(base, "new_file.txt"))
    truncated = ppt.truncate_path(base, new_file)
    assert truncated == ".../new_file.txt"
    # Test truncating identical path
    assert ppt.truncate_path(base, base) == base
    # Test truncating path in a totally different directory
    truncated = ppt.truncate_path(base, "/non/existant/but/different.txt")
    assert truncated == "/non/existant/but/different.txt"

def test_create_text_window():
    """
    Tests the create_text_window function.
    """
    # Test center justified
    d = "\033[0m"
    window = ppt.create_text_window(["Some", "Text!"], 11, 6)
    compare = ""
    compare = f"{compare}{d}+---------+{d}"
    compare = f"{compare}\n{d}|         |{d}"
    compare = f"{compare}\n{d}|{d}  Some   {d}|{d}"
    compare = f"{compare}\n{d}|{d}  Text!  {d}|{d}"
    compare = f"{compare}\n{d}|         |{d}"
    compare = f"{compare}\n{d}+---------+{d}"
    assert window == compare
    # Test left & top justified
    window = ppt.create_text_window(["New", "Text?"], 12, 7, xjust="left", yjust="top")
    compare = ""
    compare = f"{compare}{d}+----------+{d}"
    compare = f"{compare}\n{d}|{d} New      {d}|{d}"
    compare = f"{compare}\n{d}|{d} Text?    {d}|{d}"
    compare = f"{compare}\n{d}|          |{d}"
    compare = f"{compare}\n{d}|          |{d}"
    compare = f"{compare}\n{d}|          |{d}"
    compare = f"{compare}\n{d}+----------+{d}"
    assert window == compare
    # Test right and bottom justified
    window = ppt.create_text_window(["More", "Text."], 12, 7, xjust="right", yjust="bottom")
    compare = ""
    compare = f"{compare}{d}+----------+{d}"
    compare = f"{compare}\n{d}|          |{d}"
    compare = f"{compare}\n{d}|          |{d}"
    compare = f"{compare}\n{d}|          |{d}"
    compare = f"{compare}\n{d}|{d}     More {d}|{d}"
    compare = f"{compare}\n{d}|{d}    Text. {d}|{d}"
    compare = f"{compare}\n{d}+----------+{d}"
    assert window == compare
    # Test different colored window
    g = "\033[32m"
    window = ppt.create_text_window(["Some", "Text!"], 11, 6, color="green")
    compare = ""
    compare = f"{compare}{g}+---------+{d}"
    compare = f"{compare}\n{g}|         |{d}"
    compare = f"{compare}\n{g}|{d}  Some   {g}|{d}"
    compare = f"{compare}\n{g}|{d}  Text!  {g}|{d}"
    compare = f"{compare}\n{g}|         |{d}"
    compare = f"{compare}\n{g}+---------+{d}"
    assert window == compare
    # Test that color codes and whitespace not counted in justifying text
    window = ppt.create_text_window(["  Some  ", f" {g}Text!{d} "], 11, 6)
    compare = ""
    compare = f"{compare}{d}+---------+{d}"
    compare = f"{compare}\n{d}|         |{d}"
    compare = f"{compare}\n{d}|{d}  Some   {d}|{d}"
    compare = f"{compare}\n{d}|{d}  {g}Text!{d}  {d}|{d}"
    compare = f"{compare}\n{d}|         |{d}"
    compare = f"{compare}\n{d}+---------+{d}"
    assert window == compare
    # Test if text is longer than the allowed limits
    window = ppt.create_text_window(["Long Line"], 3, 4)
    compare = ""
    compare = f"{compare}{d}+-+{d}"
    compare = f"{compare}\n{d}|{d} Long Line {d}|{d}"
    compare = f"{compare}\n{d}| |{d}"
    compare = f"{compare}\n{d}+-+{d}"
    assert window == compare
    window = ppt.create_text_window(["Too", "Many", "Lines!", "!!!"], 10, 3)
    compare = ""
    compare = f"{compare}{d}+--------+{d}"
    compare = f"{compare}\n{d}|{d}  Too   {d}|{d}"
    compare = f"{compare}\n{d}|{d}  Many  {d}|{d}"
    compare = f"{compare}\n{d}|{d} Lines! {d}|{d}"
    compare = f"{compare}\n{d}|{d}  !!!   {d}|{d}"
    compare = f"{compare}\n{d}+--------+{d}"
    assert window == compare
