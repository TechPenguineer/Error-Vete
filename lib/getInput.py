
import sys

from lib.STDOUT_cmds import flush_console
from .ERROR_MESSAGES import ERROR_MSG

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def getInput() -> str:
    inputVAL = """"""
    print(color.YELLOW + "( i ) To Paste press CTRL+V ( windows ) or CTRL+ALT+V ( linux )")
    data = input(color.BOLD + color.GREEN + "\n( ? ) " + color.CYAN + "What was the error?\n\t" + color.RED)
    print(color.END)


    return data