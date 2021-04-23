"""
tqdm is very useful when you want show progress bar in python console
"""
from time import sleep

from tqdm import tqdm

for tqdm in tqdm(range(10)):
    sleep(0.1)
    pass

from tqdm import trange
from colorama import Fore

# Cross-platform colored terminal text.
color_bars = [Fore.BLACK,
              Fore.RED,
              Fore.GREEN,
              Fore.YELLOW,
              Fore.BLUE,
              Fore.MAGENTA,
              Fore.CYAN,
              Fore.WHITE]

for color in color_bars:
    for i in trange(int(7e7),
                    bar_format="{l_bar}%s{bar}%s{r_bar}" % (color, Fore.RESET)):
        pass
from termcolor import colored

tqdm.write(colored('Something bad happened', 'red'))
tqdm.write(colored('Something semi-bad happened', 'yellow'))
tqdm.write(colored('All good', 'green'))
tqdm.write(colored('Magic in the terminal', 'yellow', attrs=['bold', 'blink', 'underline']))
