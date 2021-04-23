"""
We are going to create our own custom progress bars'
"""
import os

from colorama import Fore
from termcolor import colored
from tqdm import tqdm
from tqdm import trange


def colorBar(range):
    for i in trange(int(range),
                    bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.GREEN, Fore.RESET)):
        pass


def fileOpenBar(filePath):
    tqdm.write(colored("Opening file ...", "green"))
    fileSize = os.path.getsize(filePath)
    with tqdm(total=fileSize, bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.GREEN, Fore.RESET)) as pbar:
        with open(filePath, mode='r') as inFile:
            for line in inFile:
                pbar.update(len(line.encode('utf-8')))


colorBar(2000000 * 500)

fileOpenBar(filePath="Andriod_2k.log")
