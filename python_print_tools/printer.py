#!/usr/bin/env python3

import os
import re
import math
import shutil
from os.path import abspath
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

def color_input(text:str, color:str):
    """
    Prints text to the terminal in color.

    :param text: Text to print
    :type text: str, required
    :param color: Color to print text in
    :type color: str, required
    :return:c
    :rtype: Any
    """
    color_code = get_color_code(color)
    default = get_color_code("q")
    return input(f"{color_code}{text}{default}")

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
    full_base = abspath(base_dir)
    full_file = abspath(file)
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


def create_text_window(lines:List[str], width:int, height:int,
                xjust:str="center", yjust:str="center", color="q") -> str:
    """
    Creates a "window" using ASCII text with the given lines of text inside.

    :param lines: Text separated into separate lines
    :type lines: List[str], required
    :param width: Width of the window in characters
    :type width: int, required
    :param height: Height of the window in character lines
    :type height: int, required
    :param xjust: Horizontal justification ("left", "center", "right"), defaults to "center"
    :type xjust: str, optional
    :param yjust: Vertical justification ("top", "center", "bottom"), defaults to "center"
    :type yjust: str, optional
    :param color: Color of the window border, defaults to "q" (default terminal text color)
    :type color: str, optional
    :return: Text in a window format
    :rtype: str
    """
    # Get the window color
    ccode = get_color_code(color)
    def_ccode = get_color_code("q")
    # Create the lambda generators
    generate_top = lambda w: ccode + "+" + str("-"*(w-2)) + "+" + def_ccode
    generate_side = lambda w: ccode + "|" + str(" "*(w-2)) + "|" + def_ccode
    generate_sides = lambda l: str(("\n" + generate_side(width))*l)
    # Determine the top and bottom buffer
    top_buffer = 0
    empty_lines = (height - 2) - len(lines)
    if yjust == "center":
        top_buffer = math.floor(empty_lines/2)
    elif yjust == "bottom":
        top_buffer = empty_lines
    bottom_buffer = empty_lines - top_buffer
    # Align each line
    aligned_lines = ""
    for line in lines:
        text = line.strip()
        left_buffer = 0
        spaces = (width - 4) - len(re.sub(r"\x1b\[[0-9]+m", "", text))
        if xjust == "center":
            left_buffer = math.floor(spaces/2)
        elif xjust == "right":
            left_buffer = spaces
        right_buffer = spaces - left_buffer
        aligned_lines = f"{aligned_lines}\n{ccode}|{def_ccode} "
        aligned_lines = aligned_lines + (" "*left_buffer) + text + str(" "*right_buffer)
        aligned_lines = f"{aligned_lines} {ccode}|{def_ccode}"
    # Create the full text
    window = generate_top(width)
    window = window + generate_sides(top_buffer)
    window = window + aligned_lines
    window = window + generate_sides(bottom_buffer)
    window = window + "\n" + generate_top(width)
    # Return the window
    return window

def print_window(lines:List[str], width_shrink:int=0, height_shrink:int=0,
            xjust:str="center", yjust:str="center", color="q"):
    """
    Prints a "window" using ASCII text with the given lines of text inside, fit to the terminal

    :param lines: Text separated into separate lines
    :type lines: List[str], required
    :param width_shrink: Number of characters to reduce window to from the terminal size, defaults to 0
    :type width_shrink: int, optional
    :param height_shrink: Number of lines to reduce window to from the terminal size, defaults to 0
    :type height_shrink: int, optional
    :param xjust: Horizontal justification ("left", "center", "right"), defaults to "center"
    :type xjust: str, optional
    :param yjust: Vertical justification ("top", "center", "bottom"), defaults to "center"
    :type yjust: str, optional
    :param color: Color of the window border, defaults to "q" (default terminal text color)
    :type color: str, optional
    :return: Text in a window format
    :rtype: str
    """
    clear_console()
    # Get the width and height
    width, height = shutil.get_terminal_size()
    width = width - width_shrink
    height = height - height_shrink
    # Print window to the console
    window = create_text_window(lines, width, height, xjust=xjust, yjust=yjust, color=color)
    print(window)

def clear_console():
    """
    Clears the terminal/console/CLI.
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
