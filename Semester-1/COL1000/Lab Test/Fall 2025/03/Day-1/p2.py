def apply_n_times(value, func, n=1):
    #write code here





############################ Do Not Change #################################

# Helper functions used for testing 
# During evaluation, we may have more functions which will be passed as argument to your apply_n_times function.
# So, don't hardcode any usage of these functions.
def _double_it(x):
    return x * 2

def _add_ten(x):
    return x + 10

def _square_it(x):
    return x * x

def _add_exclamation(s):
    return s + "!"

_func_map = {
    "double_it": _double_it,
    "add_ten": _add_ten,
    "square_it": _square_it,
    "add_exclamation": _add_exclamation,
}

def solution(tc):
    inp_value, inp_func_name, inp_n = tc
    func_obj = _func_map[inp_func_name]
    return apply_n_times(inp_value, func_obj, inp_n)

def process_input(filename):
    lines = open(filename, 'r').readlines()
    lines = [line.strip() for line in lines]
    num_tests = int(lines[0])
    input_tests = []
    current_line_idx = 1
    
    for _ in range(num_tests):
        value_str = lines[current_line_idx]
        current_line_idx += 1
        
        func_name = lines[current_line_idx]
        current_line_idx += 1
        
        n_str = lines[current_line_idx]
        current_line_idx += 1
        
        try:
            value = int(value_str)
        except ValueError:
            value = value_str

        n = int(n_str)
        
        input_tests.append((value, func_name, n))
    
    return input_tests

if __name__ == "__main__":
    Input = process_input('p2_input.txt')
    for tc in Input:
        solution(tc)
