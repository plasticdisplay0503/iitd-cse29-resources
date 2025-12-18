import subprocess
import shlex
import os
from typing import Tuple, Optional, List

############################ Do Not Change This File #################################

def csvtool_caller(command: str) -> Tuple[str, Optional[str]]:
    """Execute csvtool command and return combined output and destination filename."""
    try:
        args = shlex.split(command)
        dest_filename = args[-1] if len(args) > 1 and args[-1].endswith('.csv') else None
        
        result = subprocess.run(
            args, capture_output=True, text=True, timeout=2
        )
        
        # MODIFIED LOGIC: Ignore exit code. Return stderr if it has content, otherwise stdout.
        stderr_content = result.stderr.strip()
        stdout_content = result.stdout.strip()

        final_output = stderr_content if stderr_content else stdout_content
        return final_output, dest_filename

    except Exception as e:
        return f"Error: Failed to execute command - {str(e)}", None

def solution(inp: str) -> str:
    """Wrapper function that the evaluator's subprocess calls."""
    output, _ = csvtool_caller(inp)
    return output

def process_input(filename: str) -> List[str]:
    """Function the evaluator imports to get test case commands."""
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    num_tests = int(lines[0])
    return lines[1 : num_tests + 1]

if __name__ == "__main__":
    """Logic for when a student clicks the 'Run' button."""
    try:
        commands = process_input('p2_input.txt')
        for command in commands:
            print(f"Executing: {command}")
            
            program_output, dest_filename = csvtool_caller(command)
            
            print(f"\n--- Output from your program ---\n{program_output if program_output else '[No output produced]'}\n------------------------------\n")
            
            if dest_filename and not program_output:
                print(f"======= PREVIEW of created file: '{dest_filename}' =======")
                if os.path.exists(dest_filename):
                    with open(dest_filename, 'r') as f:
                        content = f.read()
                    print(content.strip() if content else "[ File is empty ]")
                else:
                    print(f"[ File '{dest_filename}' was not created. ]")
                print("================ END OF PREVIEW ================\n")

    except FileNotFoundError:
        print("p2_input.txt not found. Cannot run local tests.")
    except Exception as e:
        print(f"An unexpected error occurred in the runner script: {e}")