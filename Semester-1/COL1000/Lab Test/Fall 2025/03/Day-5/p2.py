def filter_and_transform(items, filter_func, transform_func):
    #write code here
    
    
    




############################ Do Not Change #################################

# Example helper functions - these will be available to the VPL system's process_input
# Students do NOT need to implement these.
def _is_even(x):
    return x % 2 == 0

def _is_positive(x):
    return x > 0

def _square_it(x):
    return x * x

def _double_it(x):
    return x * 2

def _has_char_e(s):
    if isinstance(s, str):
        return 'e' in s.lower()
    return False

def _to_uppercase(s):
    if isinstance(s, str):
        return s.upper()
    return s

_func_map = {
    "is_even": _is_even,
    "is_positive": _is_positive,
    "square_it": _square_it,
    "double_it": _double_it,
    "has_char_e": _has_char_e,
    "to_uppercase": _to_uppercase,
}

def solution(tc):
    items, filter_func_name, transform_func_name = tc
    filter_func = _func_map[filter_func_name]
    transform_func = _func_map[transform_func_name]
    return filter_and_transform(items, filter_func, transform_func)

def process_input(filename):
    lines = open(filename, 'r').readlines()
    lines = [line.strip() for line in lines]
    num_tests = int(lines[0])
    input_tests = []
    current_line_idx = 1

    for _ in range(num_tests):
        filter_name = lines[current_line_idx]
        current_line_idx += 1

        transform_name = lines[current_line_idx]
        current_line_idx += 1

        num_items = int(lines[current_line_idx])
        current_line_idx += 1

        current_items_list = []
        for _ in range(num_items):
            item_str = lines[current_line_idx]
            try:
                current_items_list.append(int(item_str))
            except:
                current_items_list.append(item_str)
            current_line_idx += 1

        input_tests.append((current_items_list, filter_name, transform_name))

    return input_tests

if __name__ == "__main__":
    Input = process_input('p2_input.txt')
    i = 0
    while i < len(Input):
        print(solution(Input[i]))
        i += 1
