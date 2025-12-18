def compose(*functions):
    # write code here









############################ Do Not Change #################################

# Example helper functions
def doubler(x):
    return x * 2

def add_ten(x):
    return x + 10

def squarer(x):
    return x * x

def negate(x):
    return -x

def increment(x):
    return x + 1

# Map string names to actual helper functions
_func_map = {
    "doubler": doubler,
    "add_ten": add_ten,
    "squarer": squarer,
    "negate": negate,
    "increment": increment,
}

def solution(tc):
    func_names, value = tc
    functions_to_compose = [_func_map[name] for name in func_names]
    composed_func = compose(*functions_to_compose)
    return composed_func(value)


def process_input(filename):
    lines = open(filename, 'r').readlines()
    lines = [line.strip() for line in lines]
    num_tests = int(lines[0])
    input_tests = []
    current_line_idx = 1

    for _ in range(num_tests):
        func_names_str = lines[current_line_idx]
        func_names = func_names_str.split()
        current_line_idx += 1

        value = int(lines[current_line_idx])
        current_line_idx += 1

        input_tests.append((func_names, value))

    return input_tests


if __name__ == "__main__":
    Input = process_input('p2_input.txt')
    for func_names, value in Input:
        print(solution((func_names, value)))
