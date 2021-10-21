"""
Script to zero-pad the problem numbers of LeetCode files downloaded by the
leetcode-cli (for proper alphabetic ordering).

"""

import os
import re


def rename_leetcode_files():
    """
    Renames the default name of leetcode files in this directory.

    """
    EXCLUDED = [
        "README.md",
        "rename_lc.py",
    ]
    lc_file_re = re.compile(r"^(?P<id>[\d]+)\.(?P<filename>[\w\-]+).py$")
    files = [f for f in os.listdir() if f not in EXCLUDED and f[0] != "."]

    for f in files:
        match = lc_file_re.match(f)
        if match is not None:
            d = match.groupdict()
            new_filename = d["filename"].replace("-", "_")
            new_path = f"{int(d['id']):>04d}-{new_filename}.py"
            print(f'Renaming "{f}" to "{new_path}"')
            os.rename(f, new_path)
    return


if __name__ == "__main__":
    rename_leetcode_files()
