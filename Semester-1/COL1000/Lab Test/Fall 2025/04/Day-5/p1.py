# p1.py
"""Boilerplate code for problem 1."""
import amodule  # Do not change
from typing import List, Callable, Dict # Do not change


def make_reader() -> Callable[[], list]:
    """
    Creates and returns a parameter-less function that reads lines until EOF.

    The returned function should read all lines from input until an EOFError
    is encountered. If a line contains one or more newline characters ('\n'),
    it must be split into multiple lines. The function returns a list of all
    the resulting lines.
    """
    # Your code here
    pass


def tokens(s: str, sep: str, isvalid: Callable[..., bool]) -> filter:
    """
    Returns a filter object of valid "words" from string s.

    Words are separated by ANY character present in the `sep` string. A word is
    considered valid if the provided function `isvalid` returns `True` when
    called with the word as an argument.

    Constraints:
    - Must be implemented with a single 'return' statement (a helper function is allowed).
    - Must not use any loops (this includes for, while, and comprehensions).
    - Hint: A recursive helper function can be used to handle multiple separators
      without a loop. Consider a strategy where you recursively replace all
      separator characters in the input string with a single, chosen separator (like
      the first character of `sep`). Once the string is normalized, a simple 
      `split()` will be sufficient.
    """
    # Your code here
    pass


def convert(t: str) -> str:
    """
    Recursively converts a string `t` into a new string that encodes a list
    of its parts.

    The conversion rule is as follows: `convert(t)` becomes a string formatted
    as `[convert(BLR),LR,convert(ALR)]`, where:
      - LR is the first longest run of repeated characters in `t`.
      - BLR is the part of `t` before LR.
      - ALR is the part of `t` after LR.

    Important Rules:
      - If any of the three parts (convert(BLR), LR, or convert(ALR)) is an
        empty string, it is completely omitted from the output, including its
        comma. The output might have 1, 2, or 3 parts.
      - The base case is that an empty string `t` converts to an empty string `""`.
      - You must use the provided `amodule.longest_run(t)` function.

    Example:
      - `convert('weer')` -> `'[[w],ee,[r]]'`
      - `convert('aaab')` -> `'[aaa,[b]]'` (BLR is empty)
      - `convert('bbaaa')` -> `'[[bb],aaa]'` (ALR is empty)
      - `convert('ccc')` -> `'[ccc]'` (BLR and ALR are empty)
    """
    # Your code here
    pass


def process(sep: str, isvalid: Callable[..., bool]):
    """
    Orchestrates the reading, tokenizing, and converting of input lines.

    This function is the main driver of the program. It receives a separator string
    `sep` and a validation function `isvalid`.

    Steps:
    1. Calls make_reader() to get a reader function, then calls it to get all input lines.
    2. Tokenizes each line by calling the `tokens` function with the specified `sep`
       and the `isvalid` function provided to this `process` function.
    3. Converts each valid token resulting from step 2 using the `convert` function.
    4. Returns a map of maps, where each inner map contains the converted tokens for one line.

    Partial Credit: Returning a list of lists or similar container instead of a
    map of maps will be graded for 50% of the marks for this function.
    """
    # Your code here
    pass


#################################################################
# HOW TO TEST YOUR CODE LOCALLY:
#
# 1. Edit the contents of the `p1_input.txt` file with your test data.
# 2. Change the value of the SEP variable below to match your test.
# 3. Press the "Run" button.
#
#################################################################

SEP = " ,"   # We have a whitespace and , in SEP. So, separators would be " " & ","

########### Do not change below this line ###########
def solution(sep):
    import copy
    try:
        M = process(sep, amodule.isvalid)
        materialized = [list(line) for line in M]
        print(f"**********************************************")
        print(f"Processing all input lines with separator '{sep}':")
        for lno, line_list in enumerate(materialized):
            print(f'Line {lno} converted tokens:')
            for t in line_list:
                print('\t', t)
        return materialized
    except Exception as e:
        print(f"Error parsing result from process() function. Error:{e}")
    return None

if __name__ == "__main__":
    result = solution(SEP)