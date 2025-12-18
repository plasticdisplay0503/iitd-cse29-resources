import subprocess
import shlex
import os

############################ Do Not Change This File #################################
def csvtool_caller(command: str) -> str:
    """Execute csvtool command."""
    try:
        args = shlex.split(command)
        result = subprocess.run(
            args, capture_output=True, text=True, timeout=2
        )
        if result.returncode != 0:
            return result.stderr.strip()
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "Error: Command timed out"
    except Exception as e:
        return f"Error: Failed to execute command - {str(e)}"

def solution(inp: str) -> str:
    """Wrapper function that the evaluator calls."""
    return csvtool_caller(inp)

def process_input(filename):
    lines = open(filename, 'r').readlines()
    lines = [line.strip() for line in lines if line.strip()]
    num_tests = int(lines[0])
    input_tests = [lines[t].strip() for t in range(1, num_tests + 1)]
    return input_tests

if __name__ == "__main__":
    try:
        Input = process_input('p2_input.txt')
        for command in Input:
            print(f"Executing: {command}")
            
            program_output = csvtool_caller(command)
            
            print(f"\n--- Output from your program ---\n{program_output if program_output else '[No output is produced]'}\n------------------------------\n")
            
            try:
                parts = shlex.split(command)
                if '-groupby' in parts:
                    dest_filename = parts[-1]
                    
                    print(f"======= PREVIEW of created file: '{dest_filename}' =======")
                    if os.path.exists(dest_filename):
                        with open(dest_filename, 'r') as f:
                            content = f.read()
                        print(content.strip() if content else "[ The file was created but is empty. ]")
                    else:
                        print(f"[ File '{dest_filename}' was not found. ]")
                    print("================ END OF PREVIEW ================\n")
            except Exception as e:
                print(f"[ Could not generate file preview due to an error: {e} ]\n")

    except FileNotFoundError:
        print("p2_input.txt not found. Cannot run local tests.")
    except Exception as e:
        print(f"An unexpected error occurred in the runner script: {e}")