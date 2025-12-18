def power(base: int, exponent: int) -> int:
    # write your code here below












############################ Do Not Change #################################

def solution(inp):
    return power(*inp)


def process_input(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    num_tests = int(lines[0])
    input_tests = []

    for t in range(1, num_tests + 1):
        base_str, exp_str = lines[t].split(",")
        base = int(base_str.strip())
        exponent = int(exp_str.strip())
        input_tests.append([base, exponent])

    return input_tests


if __name__ == "__main__":
    Input = process_input('p3_input.txt')
    for inp in Input:
        print(solution(inp))
