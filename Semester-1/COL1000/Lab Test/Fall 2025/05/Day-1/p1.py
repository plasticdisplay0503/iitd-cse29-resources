import subprocess
import shlex

############################ Do Not Change This File #################################
# This file implements a caller function for the csvtool utility.
# It is used by the exercises and must not be modified.

def csvtool_caller(command: str) -> str:
    """Execute csvtool command."""
    try:
        # Use shlex.split to handle arguments correctly
        args = shlex.split(command)
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            timeout=2 # Add a timeout for safety
        )
        if result.returncode != 0:
            # Errors from csvtool.py are printed to stderr
            return result.stderr.strip()
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "Error: Command timed out"
    except Exception as e:
        return f"Error: Failed to execute command - {str(e)}"

def solution(inp):
    return csvtool_caller(inp)

def process_input(filename):
    lines = open(filename, 'r').readlines()
    lines = [line.strip() for line in lines if line.strip()]
    num_tests = int(lines[0])
    input_tests = [lines[t].strip() for t in range(1, num_tests + 1)]
    return input_tests

if __name__ == "__main__":
    try:
        Input = process_input('p1_input.txt')
        for command in Input:
            print(f"Executing: {command}")
            output = solution(command)
            print(f"--- Tool Output ---")
            print(output if output else "[No output produced]")
            print("-------------------\n")
    except FileNotFoundError:
        print("p1_input.txt not found.")