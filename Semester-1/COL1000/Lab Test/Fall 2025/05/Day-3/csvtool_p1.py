#!/usr/bin/env python3

# You may add supporting functions, but do not change the signature of filter_rows.
# You are NOT allowed to use the 'csv' module, 're' module, or 'collections' module.

from lab_utils import run_csvtool_p1_main
from typing import List, Dict, Any, Tuple

# ===================================================================================
# =================== WRITE YOUR FUNCTION IN THE SPACE BELOW ========================
#
# Refer to the Problem 1 description for the EXACT specifications.
#
# ===================================================================================




# ===================================================================================
# =================== DO NOT MODIFY THE CODE BELOW THIS LINE ========================
# ===================================================================================

if __name__ == '__main__':
    # The run_csvtool_p1_main function (in lab_utils) handles parsing the command-line
    # arguments into tuples before calling your filter_rows function.
    
    # This will fail until you have defined the filter_rows function.
    run_csvtool_p1_main(filter_rows_func=filter_rows)