""" Boilerplate Code for Problem 1 of LabTest4-Day3
"""
import pprint # Do not change
from typing import Callable, Dict, List # Do not change

def make_reader() -> Callable[[], List[str]]:
    """
    Creates and returns a parameter-less function that reads all input lines
    from the specified input file.

    Args:
        None.

    Returns:
        function: A parameter-less function that reads all lines until EOF.

    Analogy:
        Think of this as a 'book reader' who reads all the pages (lines)
        from a specified book.

    Example:
        >>> reader = make_reader()
        >>> lines = reader()  # Reads all lines from input1.txt
    """
    pass


def tokens(s: str, sep: str) -> filter:
    """
    Extracts valid Key=Value tokens separated by a given separator.

    Args:
        s (str): Input string containing key-value pairs.
        sep (str): Separator between tokens (e.g., space or comma).

    Returns:
        filter: A filtered iterable of valid tokens.

    Rules:
        - Each token must be in the form 'Key=Value'.
        - Key must consist of only English alphabets (A–Z, a–z).
        - Value must be a valid integer string.
        - Key must be at least 2 characters long.

    Constraints:
        - Must be implemented as a SINGLE statement (using map or filter).
        - No loops allowed.

    Analogy:
        Imagine this as a filter that only allows correctly formed 'Key=Value'
        passes through a security gate.

    Example:
        >>> list(tokens("AA=12 BB=34", " "))
        ['AA=12', 'BB=34']
    """
    pass


def convert(s: str) -> bool:
    """
    Recursively checks if the Key part of 'Key=Value' is symmetric.

    Args:
        s (str): String of the form 'Key=Value'.

    Returns:
        bool: True if the key is symmetric, False otherwise.

    Rules:
        - A string is symmetric if:
            * It has even length AND
            * The first half equals the second half OR its reverse and each half is symmetric
        - Must be implemented recursively.

    Analogy:
        Think of symmetry like folding a paper in half — if both sides match,
        it’s symmetric.

    Example:
        >>> convert("AA=100")
        True
        >>> convert("XYZZYX=10")
        False
    """
    pass


def process(sep: str) -> Dict[int, Dict[str, bool]]:
    """
    Orchestrates the workflow of reading, tokenizing, converting, 
    and structuring results into a map of maps.

    Args:
        sep (str): Separator for tokens (e.g., space " " or comma ",").

    Returns:
        dict: Dictionary of dictionaries containing Boolean results.

    Steps:
        1. Create a reader using make_reader().
        2. Read input lines from the file.
        3. Tokenize each line using tokens().
        4. Convert each token using convert().
        5. Structure results as a map of maps.

    Analogy:
        This function is like the 'factory manager' who ensures every machine
        (reader, tokenizer, converter) does its job in sequence, and collects
        the finished products neatly.

    Example:
        Input File (input1.txt):
            3
            Key1=12 Key2=23 Key3=34
            AA=100 ABAB=200 XYXY=300
            K=45 ZZ=67 XYZZYX=20

        Output:
            {
              1: {'Key1': False, 'Key2': False, 'Key3': False},
              2: {'AA': True, 'ABAB': True, 'XYXY': True},
              3: {'K': False, 'ZZ': True, 'XYZZYX': False}
            }
    """
    pass



############################## DO NOT CHANGE ########################################
def solution(tc):
    """
    Solution entry point for test case handling.
    """
    if isinstance(tc, str):
        # For backward compatibility, assume space separator
        return process(" ", tc)
    elif isinstance(tc, tuple) and len(tc) == 2:
        # New format: (input_filename, separator)
        input_filename, separator = tc
        return process(separator)
    else:
        raise ValueError("Test case must be a string (filename) or tuple (filename, separator)")


def process_input(filename: str):
    """
    Reads the test case file and extracts input filenames and separators for the solution.
    """
    lines = open(filename, 'r').read().splitlines()
    num_tests = int(lines[0])
    test_data = []
    for i in range(1, num_tests + 1):
        line = lines[i]
        parts = line.split(' ', 1)  # Split on first space
        input_filename = parts[0]
        if len(parts) > 1:
            separator = parts[1] if parts[1] else " "  # If separator is empty string, use space
        else:
            separator = " "  # Default to space if no separator
        test_data.append((input_filename, separator))
    return test_data

if __name__ == "__main__":
    from pprint import pprint
    Input = process_input('p1_input.txt')
    for tc in Input:
        result = solution(tc)
        if result != "":
            pprint(result)
