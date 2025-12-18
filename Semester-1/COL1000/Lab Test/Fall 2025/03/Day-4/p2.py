# Example helper functions - these will be available to the VPL system's process_input
def _increment(x):
    return x + 1

def _double_it(x):
    return x * 2

def _square_it(x):
    return x * x

def _negate(x):
    return -x

def _add_ten(x):
    return x + 10

def _cube_it(x):
    return x ** 3


def apply_operations_sequence(value, *operations):
    #write code here


############################ Do Not Change #################################

# Map string names to actual helper functions
_func_map = {
    "increment": _increment,
    "double_it": _double_it,
    "square_it": _square_it,
    "negate": _negate,
    "add_ten": _add_ten,
    "cube_it": _cube_it,
}


def solution(tc):
    value, func_names = tc
    operations = []
    i = 0
    while i < len(func_names):
        operations.append(_func_map[func_names[i]])
        i += 1
    return apply_operations_sequence(value, *operations)


def process_input(filename):
    lines = open(filename, 'r').readlines()
    lines = [line.strip() for line in lines]
    num_tests = int(lines[0])
    input_tests = []
    current_line_idx = 1

    for _ in range(num_tests):
        value_str = lines[current_line_idx]
        current_line_idx += 1

        operations_str = lines[current_line_idx]
        func_names = operations_str.split()
        current_line_idx += 1

        try:
            value = int(value_str)
        except:
            value = value_str

        input_tests.append((value, func_names))

    return input_tests


if __name__ == "__main__":
    Input = process_input('p2_input.txt')
    i = 0
    while i < len(Input):
        print(solution(Input[i]))
        i += 1
