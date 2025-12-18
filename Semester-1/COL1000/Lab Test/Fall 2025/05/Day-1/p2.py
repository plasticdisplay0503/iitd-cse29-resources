import subprocess
import shlex
import os

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

# --- MODIFIED SECTION FOR LOCAL TESTING AND FILE PREVIEW ---
if __name__ == "__main__":
    try:
        Input = process_input('p2_input.txt')
        for command in Input:
            print(f"Executing: {command}")
            
            # Execute the student's command and get the direct output
            program_output = solution(command)
            
            # Print the output from their program clearly
            print(f"\n--- Output from your program ---\n{program_output}\n------------------------------\n")

            # --- File Preview Logic ---
            # This part runs AFTER the student's code to show the result
            try:
                parts = shlex.split(command)
                # Check if this was a merge command
                if '-merge' in parts:
                    # The destination file is the last argument
                    dest_filename = parts[-1]
                    
                    print(f"======= PREVIEW of created file: '{dest_filename}' =======")
                    if os.path.exists(dest_filename):
                        with open(dest_filename, 'r') as f:
                            content = f.read()
                        if content:
                            print(content.strip())
                        else:
                            print("[ The file was created but is empty. ]")
                    else:
                        print(f"[ File '{dest_filename}' was not found. It may not have been created due to an error. ]")
                    print("================ END OF PREVIEW ================\n")

            except Exception as e:
                # This is a fallback in case parsing the command fails
                print(f"[ Could not generate file preview due to an error: {e} ]\n")

    except FileNotFoundError:
        print("p2_input.txt not found. Cannot run local tests.")
    except Exception as e:
        print(f"An unexpected error occurred in the runner script: {e}")