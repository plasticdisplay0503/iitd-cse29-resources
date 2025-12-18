from typing import Callable, Tuple, List

def create_password_validator() -> Callable[[str], Tuple[bool, List[str]]]:

    def validator_function(password):
        
    #write code here
    
    
    return validator_function



    
############################ Do Not Change #################################

def solution(password_str):
    validator = create_password_validator()
    return validator(password_str)

def process_input(filename):
    lines = open(filename, 'r').readlines()
    lines = [line.strip() for line in lines]
    num_tests = int(lines[0])
    input_tests = []
    
    for t in range(1, num_tests + 1):
        input_tests.append(lines[t])
    
    return input_tests

if __name__ == "__main__":
    Input = process_input('p1_input.txt')
    for password in Input:
        print(solution(password))