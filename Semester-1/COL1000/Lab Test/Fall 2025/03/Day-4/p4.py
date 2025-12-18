def is_balanced(s: str) -> bool:
    # write code here
    pass

############################ Do Not Change #################################

def solution(tc):
    return is_balanced(tc)

def process_input(filename):
    lines = open(filename, 'r').readlines()
    lines = [line.strip() for line in lines]
    num_tests = int(lines[0])
    input_tests = []
    
    for i in range(1, num_tests + 1):
        input_tests.append(lines[i])
        
    return input_tests

if __name__ == "__main__":
    Input = process_input('p4_input.txt')
    for s_val in Input:
        print(is_balanced(s_val))