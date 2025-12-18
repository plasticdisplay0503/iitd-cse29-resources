"""Boilerplate code for Day 4 – Problem 1."""
from typing import Callable, List


def make_reader(line_count: int) -> Callable[[], list]:
    """
    Returns a parameter-less function that reads exactly `line_count` lines from standard input.

    Behavior:
        • Reads one line at a time using `input()`, stripping trailing newlines.
        • If EOFError is encountered before reading all lines, print:
              Fewer than {line_count} were provided
          and exit the program (raise SystemExit).
        • If more than `line_count` lines are provided, print:
              More lines than {line_count} were provided
          and exit the program (raise SystemExit).
    """
    pass


def tokens(s: str, sep: str, isvalid: Callable[[str], bool]) -> filter:
    """
    Returns a filter object of *valid words* from the string `s`.
    A word is considered valid if the given `isvalid` function returns True for it.

    Behavior:
        • Words are separated by one or more occurrences of `sep`.
        • Must assert that `sep` is not an empty string (raise AssertionError if it is).
        • Implement with a single `return` statement (a helper function is allowed).
        • Must NOT use any loops (including list comprehensions).

    """
    pass


def balanced(L: List[str]) -> bool:
    """
    Recursively checks whether a list `L` of strings is *balanced*.

    Definition:
        • An empty list is always balanced.
        • A non-empty list is balanced if:
            1. It has an even number of strings, AND
            2. The sums of lengths of its two halves differ by at most 1, AND
            3. Both halves are themselves balanced.

       Where:
            L1 = L[:len(L)//2]
            L2 = L[len(L)//2:]

    Constraints:
        • Must be implemented recursively.
        • Must NOT use loops.
    """
    pass


def process(sep:str, num_lines:int, isValid:Callable[...,bool]):
    """
    Performs the overall processing pipeline.

    Steps:
        1. Calls `make_reader()` to obtain a reader function that reads the input lines.
        2. Invokes that reader to get a list of lines.
        3. Tokenizes each line using `tokens(line, sep, isvalid)`.
        4. Keeps only those tokenized lines that are *balanced* using `balanced()`.
        5. Returns a *filter of list*, where each inner list represents the tokens of one line.
    """
    pass











###############################
# Local test configuration
###############################
N = 10   # expected number of input lines
SEP = " "  # token separator








##############################################################
# Do not change below this line
##############################################################
def map2dict(M: map) -> dict:
    """Converts a map of maps into a dictionary of dictionaries for easy display."""
    D = {}
    for lno, lineM in enumerate(M):
        D[lno] = {}
        for tno, t in enumerate(lineM):
            D[lno][tno] = t
    return D


def solution(sep:str, n: int, isvalid: Callable[[str], bool]):
    """
    Calls `process()` and materializes the returned maps for readable output.
    """
    try:
        M = process(sep, n, amodule.isvalid)
        materialized = [list(line) for line in M]
        print("**********************************************")
        print(f"Processing {n} lines with separator '{sep}':")
        for lno, line_list in enumerate(materialized):
            print(f"Line {lno} tokens:")
            for t in line_list:
                print("\t", t)
        return materialized
    except SystemExit:
        print("Program exited as expected.")
    except Exception as e:
        print(f"Error in process() or dependent functions. Error: {e}")
    return None


if __name__ == "__main__":
    import amodule
    result = solution(SEP, N, amodule.isvalid)
