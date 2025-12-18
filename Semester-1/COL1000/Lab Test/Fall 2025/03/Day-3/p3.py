def reverseString(s: str) -> str:
    # write your code here below













############################ Do Not Change #################################

def solution(inp):
    return reverseString(inp)


def process_input(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    num_tests = int(lines[0])
    input_tests = lines[1:num_tests+1]  # Strings to reverse

    return input_tests


if __name__ == "__main__":
    Input = process_input('p3_input.txt')
    for inp in Input:
        print(solution(inp))
