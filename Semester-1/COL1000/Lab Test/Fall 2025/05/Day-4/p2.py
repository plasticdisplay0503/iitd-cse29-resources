#!/usr/bin/env python3
import subprocess
import shlex
import os

############################ Do Not Change This File #################################
# This file implements a caller function for the csvtool utility (split_csv).
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

            program_output = solution(command)

            if program_output.strip():
                print(f"\n--- Output from your program ---\n{program_output}\n------------------------------\n")
            else:
                print("\n--- Output from your program ---\n[No output produced]\n------------------------------\n")

            # --- File Preview Logic (for split_csv) ---
            try:
                parts = shlex.split(command)
                if "-split" in parts:
                    # According to: -split <file> <col> <prefix>
                    idx = parts.index("-split")
                    if len(parts) >= idx + 4:
                        prefix = parts[idx + 3]
                        # Show preview for all files matching prefix_*.csv
                        print(f"======= PREVIEW of generated files (prefix='{prefix}') =======")
                        found = False
                        for fname in os.listdir("."):
                            if fname.startswith(prefix + "_") and fname.endswith(".csv"):
                                found = True
                                print(f"\n--- {fname} ---")
                                with open(fname, "r") as f:
                                    content = f.read().strip()
                                print(content if content else "[ Empty file ]")
                        if not found:
                            print(f"[ No files found with prefix '{prefix}_'. It may not have created any. ]")
                        print("================ END OF PREVIEW ================\n")

            except Exception as e:
                print(f"[ Could not generate file preview due to an error: {e} ]\n")

    except FileNotFoundError:
        print("p2_input.txt not found. Cannot run local tests.")
    except Exception as e:
        print(f"An unexpected error occurred in the runner script: {e}")
