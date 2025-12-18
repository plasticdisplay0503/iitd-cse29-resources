import subprocess
import shlex

############################ Do Not Change This File #################################
# This file implements a caller function for the csvtool utility.
# It is used by the exercises and must not be modified.

def csvtool_caller(command: str) -> str:
    """Execute csvtool command."""
    try:
        args = shlex.split(command)
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            timeout=2
        )
        if result.returncode != 0:
            # Return the error exactly as the program would raise it
            return result.stderr.strip()
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "Error: Command timed out"
    except Exception as e:
        return f"{type(e).__name__}: {str(e)}"


def solution(inp: str) -> str:
    return csvtool_caller(inp)


def process_input(filename: str):
    """Reads commands from input file."""
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    num_tests = int(lines[0])
    return lines[1:num_tests + 1]


if __name__ == "__main__":
    try:
        inputs = process_input('p1_input.txt')
        for command in inputs:
            print(f"Executing: {command}")
            output = solution(command)
            print("--- Tool Output ---")
            print(output if output else "[No output produced]")
            print("-------------------\n")
    except FileNotFoundError:
        print("p1_input.txt not found.")
