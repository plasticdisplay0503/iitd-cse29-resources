from typing import List

def find_longest_subarray(nums: List[int]) -> int:
    # write code here














############################ Do Not Change #################################

def solution(tc):
    return find_longest_subarray(tc)

def process_input(filename):
    lines = open(filename, 'r').readlines()
    lines = [line.strip() for line in lines]
    num_tests = int(lines[0])
    input_tests = []
    
    for i in range(1, num_tests + 1):
        if lines[i]: # Handle empty lines
            num_list = [int(x) for x in lines[i].split()]
        else:
            num_list = []
        input_tests.append(num_list)
        
    return input_tests

if __name__ == "__main__":
    Input = process_input('p4_input.txt')
    for num_list in Input:
        print(find_longest_subarray(num_list))