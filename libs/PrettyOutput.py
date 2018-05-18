from __future__ import print_function
import sys

from colorama import Fore, Back, Style
from colorama import init as color_init

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def output_good(line):
    eprint(Fore.GREEN + Style.BRIGHT + "[+]" + Style.RESET_ALL, line)

def output_indifferent(line):
    eprint(Fore.BLUE + Style.BRIGHT + "[*]" + Style.RESET_ALL, line)

def output_error(line):
    eprint(Fore.RED + Style.BRIGHT + "[-] !!! " + Style.NORMAL, line, Style.BRIGHT + "!!!")

def output_bad(line):
    eprint(Fore.RED + Style.BRIGHT + "[-]" + Style.RESET_ALL, line)

def output_info(line):
    eprint(Fore.WHITE + Style.BRIGHT + "[*]" + Style.RESET_ALL, line)
