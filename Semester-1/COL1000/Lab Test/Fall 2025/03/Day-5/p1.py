from typing import List, Any

def rotate_matrix_90(matrix: List[List[Any]], clockwise: bool = True) -> List[List[Any]]:
    # write code here







############################ Do Not Change #################################

def solution(tc):
    inp_matrix, inp_clockwise = tc
    return rotate_matrix_90(inp_matrix, inp_clockwise)


def process_input(filename):
    lines = open(filename, 'r').readlines()
    lines = [line.strip() for line in lines]
    num_tests = int(lines[0])
    input_tests = []
    current_line_idx = 1
    
    for _ in range(num_tests):
        clockwise_str = lines[current_line_idx]
        clockwise_bool = True if clockwise_str.lower() == 'true' else False
        current_line_idx += 1
        
        n = int(lines[current_line_idx])
        current_line_idx += 1
        
        matrix = []
        for _ in range(n):
            row_str = lines[current_line_idx].split()
            row = []
            for x in row_str:
                if x.isdigit() or (x.startswith('-') and x[1:].isdigit()):
                    row.append(int(x))
                else:
                    row.append(x)
            matrix.append(row)
            current_line_idx += 1
        
        input_tests.append((matrix, clockwise_bool))
    
    return input_tests


if __name__ == "__main__":
    Input = process_input('p1_input.txt')
    for tc in Input:
        print(solution(tc))
