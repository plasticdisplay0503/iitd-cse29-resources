import subprocess
import shlex
import os

############################ Do Not Change This File #################################
# This file implements a caller function for the csvtool utility.
# It is used by the exercises and must not be modified,
# except for the local testing preview section at the end.
######################################################################################


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
        Input = process_input("p2_input.txt")
        for command in Input:
            print(f"Executing: {command}")

            # Execute student's csvtool command
            program_output = solution(command)

            # Show stdout clearly (dedupe doesn't usually print anything)
            if program_output.strip():
                print(f"\n--- Output from your program ---\n{program_output}\n------------------------------\n")
            else:
                print("\n--- Output from your program ---\n[No output produced]\n------------------------------\n")

            # --- File Preview Logic (for dedupe) ---
            try:
                parts = shlex.split(command)
                if "-dedupe" in parts:
                    # According to: -dedupe <input> <keycols> <output> <keep>
                    idx = parts.index("-dedupe")
                    if len(parts) >= idx + 5:
                        output_file = parts[idx + 3]
                        print(f"======= PREVIEW of created file: '{output_file}' =======")
                        if os.path.exists(output_file):
                            with open(output_file, "r") as f:
                                content = f.read()
                            if content.strip():
                                print(content.strip())
                            else:
                                print("[ The file was created but is empty. ]")
                        else:
                            print(f"[ File '{output_file}' was not found. It may not have been created due to an error. ]")
                        print("================ END OF PREVIEW ================\n")

            except Exception as e:
                print(f"[ Could not generate file preview due to an error: {e} ]\n")

    except FileNotFoundError:
        print("p2_input.txt not found. Cannot run local tests.")
    except Exception as e:
        print(f"An unexpected error occurred in the runner script: {e}")
