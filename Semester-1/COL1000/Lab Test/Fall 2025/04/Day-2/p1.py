# p1.py
"""Boilerplate code for problem 1."""
import amodule  # Do not change
from typing import List, Callable, Dict # Do not change


def make_reader(line_count: int) -> Callable[[], list]:
    """
    Creates and returns a parameter-less function that reads exactly line_count lines.
    
    If it encounters an EOFError while reading, it must print the exact message:
    f"Fewer than {line_count} were provided" 
    and then exit the program. You can use exit() or raise SystemExit.
    """
    pass


def tokens(s: str, sep: str) -> filter:
    """
    Returns a filter object of valid "words" in string s, separated by 'sep'.
    
    A word is considered valid if it can be converted into an integer.
    A special case is that an empty string ("") is also considered valid and
    represents the integer 0.
    
    Constraints:
    - Must be implemented with a single 'return' statement (a helper function is allowed).
    - Must not use any loops.
    """
    pass


def convert(t: str) -> str:
    """
    Recursively converts a string t into another string based on its longest
    run of repeated characters.
    
    - Base Case: An empty string converts to a single dot ('.').
    - Recursive Step: The function finds the first longest run of repeated
      characters (LR) in t using amodule.longest_run(). It splits t into
      the part before the run (BLR) and the part after (ALR). The result is
      formatted as: convert(BLR)-LR-convert(ALR).
      
    Constraints:
    - Must be implemented recursively.
    - Must not use any loops.
    
    Example:
        convert("aaabbc") -> ".-aaa-.-bb-.-c-."
    """
    pass


def process(count: int, sep: str):
    """
    Orchestrates the reading, tokenizing, and converting of input lines.
    
    1. Calls make_reader() to get a reader function, then calls it to get input lines.
    2. Tokenizes each line using the 'tokens' function with the specified 'sep'.
    3. Converts each resulting token using the 'convert' function.
    4. Returns a map of maps, where each inner map contains the converted tokens for one line.
    
    Partial Credit: Returning a list of lists or similar container instead of a
    map of maps will be graded for 60% of the marks for this function.
    """
    pass


#### #### #### #### #### #### #### #### #### 
# To test your code, change values of N and SEP:
N = 3
SEP = ","
#### #### #### #### #### #### #### #### #### 

########### Do not change below this line ###########
def solution(n, sep):
    import copy
    try:
        M = process(n, sep)
        materialized = [list(line) for line in M]
        print(f"**********************************************")
        print(f"Processing {n} lines with separator '{sep}':")
        for lno, line_list in enumerate(materialized):
            print(f'Line {lno} converted tokens:')
            for t in line_list:
                print('\t', t)
        return materialized
    except SystemExit:
        print("Program exited as expected.")
    except Exception as e:
        print(f"Error parsing result from process() function. Error:{e}")
    return None

if __name__ == "__main__":
    result = solution(N, SEP)