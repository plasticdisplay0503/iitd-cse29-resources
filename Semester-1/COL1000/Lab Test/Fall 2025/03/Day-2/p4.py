from typing import Tuple

def find_prime_pair(n: int) -> Tuple[int, int]:
    # write code here
    pass

############################ Do Not Change #################################

def solution(tc):
    return find_prime_pair(tc)

def process_input(filename):
    lines = open(filename, 'r').readlines()
    lines = [line.strip() for line in lines]
    num_tests = int(lines[0])
    input_tests = []
    
    for i in range(1, num_tests + 1):
        n = int(lines[i])
        input_tests.append(n)
        
    return input_tests

if __name__ == "__main__":
    Input = process_input('p4_input.txt')
    for n_val in Input:
        print(find_prime_pair(n_val))