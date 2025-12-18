def doubler(x):
     #write code

def add_ten(x):
     #write code

def squarer(x):
     #write code

def pipe(*functions):
     #write code





############################ Do Not Change #################################

processor = pipe(doubler, add_ten, squarer)

def solution(tc):
    return processor(tc)

def process_input(filename):
    lines = open(filename, 'r').readlines()
    lines = [line.strip() for line in lines]
    num_tests = int(lines[0])
    input_values = []
    
    for t in range(1, num_tests + 1):
        input_values.append(int(lines[t]))
    
    return input_values

if __name__ == "__main__":
    Input = process_input('p2_input.txt')
    for value in Input:
        print(solution(value))
