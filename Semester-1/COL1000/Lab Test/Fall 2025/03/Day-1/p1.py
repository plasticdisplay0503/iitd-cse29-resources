def filterByProperty(array: list, property: str, value: int) -> list:
    #write code here





############################ Do Not Change #################################

def solution(tc):
    prop, val, arr = tc
    return filterByProperty(arr, prop, val)


def parse_object(line: str) -> dict:
    line = line.strip()[1:-1]
    parts = line.split(",")
    obj = {}
    for part in parts:
        if ":" not in part:
            continue
        key, val = part.split(":", 1)
        key = key.strip().strip("'").strip('"')
        val = val.strip().strip("'").strip('"')
        if val.isdigit():
            val = int(val)
        obj[key] = val
    return obj


def process_input(filename):
    lines = open(filename, 'r').readlines()
    lines = [line.strip() for line in lines]
    num_tests = int(lines[0])
    input_tests = []
    current_line_idx = 1

    for _ in range(num_tests):
        prop_val_line = lines[current_line_idx].split()
        prop = prop_val_line[0]
        val = int(prop_val_line[1])
        current_line_idx += 1

        num_objects = int(lines[current_line_idx])
        current_line_idx += 1

        objects_list = []
        for _ in range(num_objects):
            obj_str = lines[current_line_idx]
            obj = parse_object(obj_str)
            objects_list.append(obj)
            current_line_idx += 1

        input_tests.append((prop, val, objects_list))

    return input_tests


if __name__ == "__main__":
    Input = process_input('p1_input.txt')
    for prop, val, arr in Input:
        print(filterByProperty(arr, prop, val))
