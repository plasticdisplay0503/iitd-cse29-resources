"""Student implementation for Problem 2: Function Call Logger with Global Result Tracking"""

from typing import Callable, Any

# Global log dictionary - DO NOT MODIFY THIS LINE
log = {}

def logger(f: Callable[..., Any]) -> Callable[..., Any]:
    """
    A HOF that logs all function call results in a global dictionary.
    
    Returns a wrapper function that:
    - Maintains a global log of all function call results
    - Appends results to log[f.__name__] in chronological order
    - Returns the original function result unchanged
    
    Args:
        f: Any callable function to wrap
        
    Returns:
        A wrapper function that returns f(...) and logs the result
    """
    # TODO: Implement this function
    # You need to:
    # 1. Create a wrapper function that captures the global log
    # 2. The wrapper should:
    #    - Call the original function f with given arguments
    #    - Append the result to log[f.__name__] list (create list if needed)
    #    - Return the original result unchanged
    # 3. Use the global log dictionary defined above
    
    # WRITE YOUR CODE BELOW
    pass

############################ Do Not Change #################################

def solution(tc):
    func, arg = tc
    if func is None:
        print("Error: logger not implemented correctly.")
        return None
    result = func(arg) if arg is not None else func()
    print(f"Result: {result}")
    return result


def process_input(filename: str):
    import p2_utils
    with open(filename) as f:
        lines = [line.strip() for line in f if line.strip()]

    n = int(lines[0])
    tests = lines[1:n + 1]

    funcs = {
        name: logger(getattr(p2_utils, name)) if hasattr(p2_utils, name) else None
        for name in {line.split("(", 1)[0].strip() for line in tests}
    }

    parsed = []
    for line in tests:
        name, rest = line.split("(", 1)
        arg_str = rest.rstrip(")").strip()
        func = funcs.get(name.strip())

        if not arg_str:
            parsed.append((func, None))
        elif "," in arg_str:
            # Handle multiple arguments
            args = []
            for arg in arg_str.split(","):
                arg = arg.strip()
                if arg[0] in "\"'":
                    args.append(arg[1:-1])
                else:
                    try:
                        args.append(int(arg))
                    except ValueError:
                        args.append(arg)
            parsed.append((func, args))
        elif arg_str[0] in "\"'":
            parsed.append((func, arg_str[1:-1]))
        else:
            try:
                parsed.append((func, int(arg_str)))
            except ValueError:
                parsed.append((func, arg_str))
    return parsed


if __name__ == "__main__":
    # Clear log at start
    log.clear()
    
    test_cases = process_input("p2_input.txt")
    
    for tc in test_cases:
        solution(tc)
    
    print("\nGlobal log contents:")
    print(log)