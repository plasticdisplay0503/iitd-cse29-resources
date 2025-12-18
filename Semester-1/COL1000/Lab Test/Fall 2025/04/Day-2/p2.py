# p2.py
"""Boilerplate for Problem 2: Function Call Counter."""

from typing import Callable, Any # Do not change

def counter(f: Callable[..., Any]) -> Callable[..., Any]:
    """
    A HOF that counts and prints how many times any function `f` is called.

    This is a Higher-Order Function (HOF). It must return a NEW function
    (a "wrapper") that replaces the original function 'f'. The wrapper must
    be able to accept any number of positional arguments.
    
    Args:
        f (Callable): The original function to wrap.

    Returns:
        Callable: A new wrapper function that, when called:
                  1. Prints "Call number {xx} for {f.__name__}"
                  2. Executes the original function `f` with the given arguments.
                  3. Returns the result of `f` unchanged.
    """
    # todo: your code: Be sure to set and update count appropriately 
    
    return None


############################ Do Not Change #################################
# The below code is for testing your implementation
def solution(tc):
    func, args, kwargs = tc
    if func is None:
        print("Error: counter not implemented correctly.")
        return None
    return func(*args, **kwargs)

def process_input(filename: str):
    """Parses input file and dynamically loads + decorates only required functions."""
    import p2_utils
    import ast
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    num_tests = int(lines[0])
    test_lines = lines[1:num_tests + 1]
    func_names = {line.split("(", 1)[0].strip() for line in test_lines}

    functions = {}
    for name in func_names:
        if hasattr(p2_utils, name):
            # This line correctly calls the student's 'counter' function
            functions[name] = counter(getattr(p2_utils, name))
        else:
            print(f"Warning: Function '{name}' does not exist")
            functions[name] = None

    parsed_tests = []
    for line in test_lines:
        # Correctly handles various argument formats, including keyword arguments
        try:
            tree = ast.parse(line)
            call_node = tree.body[0].value
            func_name = call_node.func.id
            
            args = [ast.literal_eval(arg) for arg in call_node.args]
            kwargs = {kw.arg: ast.literal_eval(kw.value) for kw in call_node.keywords}
            
            func = functions.get(func_name)
            parsed_tests.append((func, args, kwargs))

        except (ValueError, SyntaxError, AttributeError) as e:
            # Fallback for simple cases if full parsing fails
            print(f"Warning: Could not parse '{line}' with AST. Falling back to simple parsing. Error: {e}")
            func_name, rest = line.split("(", 1)
            arg_str = rest.rstrip(")").strip()
            func = functions.get(func_name.strip())
            parsed_tests.append((func, [arg_str], {})) 

    return parsed_tests


if __name__ == "__main__":
    for tc in process_input("p2_input.txt"):
        print("Return value:", solution(tc))