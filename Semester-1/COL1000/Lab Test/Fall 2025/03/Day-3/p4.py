from typing import List # do not remove

def find_first_non_repeating(nums: List[int]) -> int:
    # write code here







############################ Do Not Change #################################

def solution(tc):
    return find_first_non_repeating(tc)

def process_input(filename):
    lines = open(filename, 'r').readlines()
    lines = [line.strip() for line in lines]
    num_tests = int(lines[0])
    input_tests = []
    
    for i in range(1, num_tests + 1):
        num_list = [int(x) for x in lines[i].split()]
        input_tests.append(num_list)
        
    return input_tests

if __name__ == "__main__":
    Input = process_input('p4_input.txt')
    for num_list in Input:
        print(find_first_non_repeating(num_list))