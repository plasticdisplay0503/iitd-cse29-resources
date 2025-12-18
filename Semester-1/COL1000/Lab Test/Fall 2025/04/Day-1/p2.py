"""Boilerplate for Problem 2: Function Call Counter."""

from typing import Callable, Any # Do not change


def counter(f: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """
    A HOF that counts and prints how many times a single-arg function is called.

    This is a Higher-Order Function (HOF). It must return a NEW function
    (a "wrapper") that replaces the original function 'f'.
    
    Args:
        f (Callable): The original single-argument function to wrap.
                      Example: is_even, is_positive, etc.

    Returns:
        Callable: A new wrapper function to keep track of each function's call count
    """
    # todo: your code: Be sure to set and update count appropriately 
    
    return None







############################ Do Not Change #################################

def solution(tc):
    func, arg = tc
    if func is None:
        print("Error: counter not implemented correctly.")
        return None
    return func(arg) if arg is not None else func()


def process_input(filename: str):
    import p2_utils
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    num_tests = int(lines[0])
    test_lines = lines[1:num_tests + 1]
    func_names = {line.split("(", 1)[0].strip() for line in test_lines}

    functions = {}
    for name in func_names:
        if hasattr(p2_utils, name):
            functions[name] = counter(getattr(p2_utils, name))
        else:
            print(f"Warning: Function '{name}' does not exist")
            functions[name] = None

    parsed_tests = []
    for line in test_lines:
        func_name, rest = line.split("(", 1)
        arg_str = rest.rstrip(")").strip()
        func = functions.get(func_name.strip())

        if not arg_str:
            arg = None
        elif (arg_str.startswith('"') and arg_str.endswith('"')) or (arg_str.startswith("'") and arg_str.endswith("'")):
            arg = arg_str[1:-1]
        else:
            try:
                arg = int(arg_str)
            except ValueError:
                arg = arg_str

        parsed_tests.append((func, arg))

    return parsed_tests


if __name__ == "__main__":
    for tc in process_input("p2_input.txt"):
        print(solution(tc))