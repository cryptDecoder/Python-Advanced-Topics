"""
This i a tutorial for understand how we can use decorator in file operations
"""
import os
import sys
from pathlib import Path

from tqdm import tqdm


def operations(func):
    def open_file(file_path):
        file_path = os.path.join(sys.path[0], file_path)
        with tqdm(total=Path(file_path).stat().st_size) as pbar:
            with open(file_path) as fin:
                pbar.update(fin.tell() - pbar.n)
                fin.readline()

    return open_file


@operations
def fileOpen(filepath):
    print("File is openinng")


fileOpen("config.json")
