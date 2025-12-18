def rotate_string(s: str, k: int) -> str:
    # write code here





############################ Do Not Change #################################

def solution(tc):
    s_val, k_val = tc
    return rotate_string(s_val, k_val)

def process_input(filename):
    lines = open(filename, 'r').readlines()
    lines = [line.strip() for line in lines]
    num_tests = int(lines[0])
    input_tests = []
    
    for i in range(1, num_tests + 1):
        parts = lines[i].split(' ', 1)
        k = int(parts[0])
        s = parts[1] if len(parts) > 1 else ""
        input_tests.append((s, k))
        
    return input_tests

if __name__ == "__main__":
    Input = process_input('p4_input.txt')
    for s_val, k_val in Input:
        print(rotate_string(s_val, k_val))