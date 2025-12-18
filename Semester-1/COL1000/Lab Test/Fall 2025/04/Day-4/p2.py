"""Boilerplate Problem 2: Function Call Counter with Tuple Return"""

from typing import Callable, Any, Tuple

def counter(f: Callable[..., Any]) -> Callable[..., Tuple[int, Any]]:
    """
    A HOF that counts how many times a function is called.
    
    Returns a wrapper function that:
    - Maintains a count of invocations of f
    - Returns a tuple (count, original_result) at each call
    - First invocation returns count = 1
    
    Args:
        f: Any callable function to wrap
        
    Returns:
        A wrapper function that returns (count, f(...))
    """

    
    # WRITE YOUR CODE BELOW
    pass

############################ Do Not Change #################################

def solution(tc):
    func, arg = tc
    if func is None:
        print("Error: counter not implemented correctly.")
        return None
    return func(arg) if arg is not None else func()


def process_input(filename: str):
    import p2_utils
    with open(filename) as f:
        lines = [line.strip() for line in f if line.strip()]

    n = int(lines[0])
    tests = lines[1:n + 1]

    funcs = {
        name: counter(getattr(p2_utils, name)) if hasattr(p2_utils, name) else None
        for name in {line.split("(", 1)[0].strip() for line in tests}
    }

    parsed = []
    for line in tests:
        name, arg = line.split("(", 1)
        arg = arg.rstrip(")").strip()
        func = funcs.get(name.strip())

        if not arg:
            parsed.append((func, None))
        elif arg[0] in "\"'":
            parsed.append((func, arg[1:-1]))
        else:
            try:
                parsed.append((func, int(arg)))
            except ValueError:
                parsed.append((func, arg))
    return parsed


if __name__ == "__main__":
    for tc in process_input("p2_input.txt"):
        print(solution(tc))
