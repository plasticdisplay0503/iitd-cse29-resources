from typing import List, Any, Callable, Tuple # do not change

def partition_list(lst: List[Any], predicate: Callable[[Any], bool]) -> Tuple[List[Any], List[Any]]:
    #write code here
    







############################ Do Not Change #################################

def _is_even(x):
    return x % 2 == 0

def _is_greater_than_5(x):
    return x > 5

def _has_char_a(s):
    return 'a' in s.lower() if isinstance(s, str) else False

def _is_negative(x):
    return x < 0

def _is_divisible_by_3(x):
    return x % 3 == 0

def _has_vowel(s):
    if not isinstance(s, str):
        return False
    for char in s.lower():
        if char in 'aeiou':
            return True
    return False

def _is_single_digit(x):
    return 0 <= x <= 9

def _ends_with_s(s):
    if not isinstance(s, str):
        return False
    return len(s) > 0 and s[-1].lower() == 's'

def _is_between_10_and_20(x):
    return 10 <= x <= 20

def _starts_with_capital(s):
    if not isinstance(s, str) or len(s) == 0:
        return False
    return 'A' <= s[0] <= 'Z'

def _is_multiple_of_5(x):
    return x % 5 == 0

_predicate_map = {
    "is_even": _is_even,
    "is_greater_than_5": _is_greater_than_5,
    "has_char_a": _has_char_a,
    "is_negative": _is_negative,
    "is_divisible_by_3": _is_divisible_by_3,
    "has_vowel": _has_vowel,
    "is_single_digit": _is_single_digit,
    "ends_with_s": _ends_with_s,
    "is_between_10_and_20": _is_between_10_and_20,
    "starts_with_capital": _starts_with_capital,
    "is_multiple_of_5": _is_multiple_of_5,
}
def solution(tc):
    inp_lst, inp_pred_name = tc
    predicate_func = _predicate_map[inp_pred_name]
    return partition_list(inp_lst, predicate_func)

def process_input(filename):
    lines = open(filename).readlines()
    lines = [line.strip() for line in lines]
    num_tests = int(lines[0])
    input_tests = []
    current_line_idx = 1
    
    for _ in range(num_tests):
        predicate_name_str = lines[current_line_idx]
        current_line_idx += 1
        
        num_elements = int(lines[current_line_idx])
        current_line_idx += 1
        
        current_list = []
        for _ in range(num_elements):
            element_str = lines[current_line_idx]
            
            numeric_predicates = {
                "is_even", "is_greater_than_5", "is_negative", "is_divisible_by_3",
                "is_single_digit", "is_between_10_and_20", "is_multiple_of_5"
            }
            
            string_predicates = {
                "has_char_a", "has_vowel", "ends_with_s", "starts_with_capital"
            }
            
            if predicate_name_str in numeric_predicates:
                try:
                    if '.' in element_str:
                        current_list.append(float(element_str))
                    else:
                        current_list.append(int(element_str))
                except ValueError:
                    current_list.append(element_str)
            else:
                current_list.append(element_str)
            
            current_line_idx += 1
        
        input_tests.append((current_list, predicate_name_str))
    
    return input_tests


if __name__ == "__main__":
    Input = process_input('p1_input.txt')
    for lst, pred_name in Input:
        print(solution((lst, pred_name)))