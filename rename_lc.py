"""
Script to zero-pad the problem numbers of LeetCode files downloaded by the
leetcode-cli (for proper alphabetic ordering).

"""


import os
import re


def rename_leetcode_files():
    """
    Renames all leetcode files in this directory.

    """
    EXCLUDED = [
        'README.md',
        'rename_lc.py',
    ]
    lc_file_re = re.compile(r'(?P<id>[\d]+)(?P<filename>\.[\w\-]+.py)')
    files = [f for f in os.listdir() if f not in EXCLUDED and f[0] != '.']

    for f in files:
        match = lc_file_re.match(f)
        if match is not None:
            d = match.groupdict()
            new_filename = f"{int(d['id']):>04d}{d['filename']}"
            print(f'Renaming "{f}" to "{new_filename}"')
            os.rename(f, new_filename)
    return


if __name__ == '__main__':
    rename_leetcode_files()
