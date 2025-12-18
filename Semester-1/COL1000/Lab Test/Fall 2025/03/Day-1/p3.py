def countdown(n: int) -> None:
    # write your code here below





############################ Do Not Change #################################

def solution(inp):
    return countdown(inp)

def process_input(filename):
    lines = open(filename, 'r').readlines()
    lines = [int(line.strip()) for line in lines]
    num_tests = int(lines[0])  # First line: number of test cases
    input_tests = []
    
    for t in range(1, num_tests + 1):
        # Parse the test case (list of integers) for each line
        L = lines[t]
        input_tests.append(L)  # Append the list directly
    
    return input_tests

if __name__ == "__main__":
    Input = process_input('p3_input.txt')
    for inp in Input:
        solution(inp)
