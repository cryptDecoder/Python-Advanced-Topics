"""
tqdm is very useful when you want show progress bar in python console
"""
from time import sleep

from tqdm import tqdm

for tqdm in tqdm(range(10)):
    sleep(0.1)
    pass
