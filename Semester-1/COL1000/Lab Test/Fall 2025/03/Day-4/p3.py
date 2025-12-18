def removeChar(s: str, c: str) -> str:
    # write your code here below





















############################ Do Not Change #################################

def solution(inp):
    return removeChar(*inp)


def process_input(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    num_tests = int(lines[0])
    input_tests = []

    for t in range(1, num_tests + 1):
        s, c = lines[t].split(",")
        input_tests.append([s.strip(), c.strip()])

    return input_tests


if __name__ == "__main__":
    Input = process_input('p3_input.txt')
    for inp in Input:
        print(solution(inp))
