"""Boilerplate code for problem 1."""
import amodule  # Do not change
from typing import List, Callable, Dict # Do not change


def make_reader(line_count: int)->Callable[[], list]:
    """
    Creates and returns a parameter-less function that reads exactly
    line_count lines from stdin and returns them as a list of strings.
    
    Args:
        line_count (int): Number of lines to read
    
    Returns:
        function: A parameter-less function that reads line_count lines
    
    Example:
        >>> reader = make_reader(3)
        >>> lines = reader()  # Returns list of 3 lines from stdin
    """
    
    pass


def tokens(s: str, line_number:int=0)->filter:
    """
    Returns a collection of valid words from string s.

    This function has a single statement that returns the collection.
    It defines an internal helper function that is used by this statement.
    Internal helper must ONLY handle BadError and print below message:
        f"Bad Word {w} in line {line_number}"
    
    Args:
        s (str): The string (line) to tokenize.
        line_number (int, optional): The line number for error messages. Defaults to 0.
    Returns:
        filter: A filter object containing the valid words.
    Constraints:
        - The return must be a SINGLE STATEMENT (can be after the helper function).
        - Must NOT use any 'for' or 'while' loops, even in the helper function.
    """
    
    pass


def convert(t: str) -> list:
    """
    Recursively converts a string t into a nested list of characters.
    Args:
        t (str): A string of length at least 1.
    Returns:
        list: A nested list representation of the string.
    Constraints:
        - Must be implemented recursively.
        - Must NOT use any loops.
    Example:
        convert("ab") -> [['a'], ['b']]
        convert("abcd") -> [[['a'], ['b']], [['c'], ['d']]]
    """
    
    pass


def process(count: int):
    """
    Reads 'count' lines, processes them, and returns a map of maps.

    First, it calls make_reader to get a reader function and calls it
    to get a list of lines.
    
    It then tokenizes each line by mapping the 'tokens' function to 
    the lines along with their line numbers.
    
    Finally, it converts each token of each line into a recursive list
    and returns a map of maps (where each map represents the 
    converted tokens of one line).
    
    Args:
        count (int): The number of lines to process.
    
    Returns:
        map: An iterator (a map object) of map objects.
             The outer map iterates over processed lines.
             Each inner map iterates over the converted tokens 
             (recursive lists) for that line.
    
    Example structure:
        {
            0: {0: [['h'], ['i']], 1: [['b'], ['y'], ['e']]},
            1: {0: [['f'], ['o'], ['o']]}
        }
    
    Note: Returning a list of lists or maps instead of this "map of maps" 
          structure (nested map iterators) will receive 80% credit.
    
    Challenge (no extra credit): Try implementing this in a single 
    composite statement (helper functions are allowed).
    """
    
    pass







#### #### #### #### #### #### #### #### #### 
# To test your code, change values of N: ###
# N is number of lines to read          ####
N=5                                     ####
#### #### #### #### #### #### #### #### #### 


########### Do not change below this line ###########

def solution(n):
    import copy
    M = process(n)
    MCopy = copy.deepcopy(M)
    try:
        print(f"**********************************************")
        print(f"Processing {n} lines of input:")
        for lno, lineM in enumerate(MCopy):
            print(f'Line {lno} converted tokens (one per line):')
            for t in lineM: print('\t',t)
    except Exception as e:
        print(f"Error parsing result from process() function. Got {MCopy}\nError:{e}")
    return MCopy

def process_input(filename):
    lines = open(filename, 'r').read().splitlines()
    num_tests = int(lines[0])
    input_tests = lines[1:]
    return input_tests[:num_tests]

if __name__ == "__main__":
    result = solution(N)