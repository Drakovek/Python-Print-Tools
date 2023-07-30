#!/usr/bin/env python3

import os.path
from typing import List

def get_color_code(color:str) -> str:
    """
    Returns an ANSI color code for a given color.
    white: "w", red: "r", green: "g" blue: "b"
    black: "k", cyan: "c", yellow: "y", magenta: "m"
    bright white: "bw", bright red: "br", bright green: "bg", bright blue: "bb"
    bright black: "bk", bright cyan: "bc", bright yellow: "by", bright magenta: "bm"

    :param color: Color to return
    :type color: str, required
    :return: ANSI color code
    :rtype: str
    """
    cl = color.lower()
    if cl == "k" or cl == "black":
        return "\033[30m"
    if cl == "r" or cl == "red":
        return "\033[31m"
    if cl == "g" or cl == "green":
        return "\033[32m"
    if cl == "y" or cl == "yellow":
        return "\033[33m"
    if cl == "b" or cl == "blue":
        return "\033[34m"
    if cl == "m" or cl == "magenta":
        return "\033[35m"
    if cl == "c" or cl == "cyan":
        return "\033[36m"
    if cl == "w" or cl == "white":
        return "\033[37m"
    if cl == "bk" or cl == "bright black":
        return "\033[90m"
    if cl == "br" or cl == "bright red":
        return "\033[91m"
    if cl == "bg" or cl == "bright green":
        return "\033[92m"
    if cl == "by" or cl == "bright yellow":
        return "\033[93m"
    if cl == "bb" or cl == "bright blue":
        return "\033[94m"
    if cl == "bm" or cl == "bright magenta":
        return "\033[95m"
    if cl == "bc" or cl == "bright cyan":
        return "\033[96m"
    if cl == "bw" or cl == "bright white":
        return "\033[97m"
    else:
        return "\033[0m"
    
def color_print(text:str, color:str):
    """
    Prints text to the terminal in color.

    :param text: Text to print
    :type text: str, required
    :param color: Color to print text in
    :type color: str, required
    """
    color_code = get_color_code(color)
    default = get_color_code("q")
    print(f"{color_code}{text}{default}")

def truncate_path(base_dir:str, file:str) -> str:
    """
    Truncates the string of an absolute path to be relative to a given base directory.

    :param base_dir: Base directory that relative path should be relative to
    :type base_dir: str, required
    :param file: Given file to truncate
    :type file: str, required
    :return: Relative path of the given file
    :rtype: str
    """
    # Return file unaltered if not inside the base directory
    full_base = os.path.abspath(base_dir)
    full_file = os.path.abspath(file)
    if full_base == full_file or not full_file.startswith(full_base):
        return full_file
    # Truncate the path of the given file
    truncated = full_file[len(full_base):]
    return f"...{truncated}"

def print_files(base_dir:str, files:List[str]):
    """
    Prints a given list of files, truncated to be relative to a base directory.

    :param base_dir: Base directory that relative paths should be relative to
    :type base_dir: str, required
    :param files: Files to print
    :type files: list[str], required
    """
    for file in files:
        print(truncate_path(base_dir, file))
