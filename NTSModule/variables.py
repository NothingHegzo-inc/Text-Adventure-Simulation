import os

# Directory Location
folderInName: str = "\\".join(str(os.path.dirname(os.path.realpath(__file__))).split("\\")[:-1])
appendingSys: str = str(os.path.dirname(os.path.realpath(__file__)))

# Text Editting
RESET: str  = "\033[0m"
BOLD: str = "\033[1m"
ITALIC: str = "\033[3m"
UNDERLINE: str = "\033[4m"
HIGHLIGHT: str = "\033[7m"
INVISIBLETEXT: str = "\033[8m"
STRIKETHRU: str = "\033[9m"
DOUBLEUNDERLINE: str = "\033[21m"
BLACK: str  = "\033[30m"
DRED: str   = "\033[31m"
DGREEN: str  = "\033[32m"
DYELLOW: str = "\033[33m"
DBLUE: str   = "\033[34m"
DPINK: str = "\033[35m"
TEAL: str   = "\033[36m"
DWHITE: str  = "\033[37m"
DREDBACK: str = "\033[41m"
DGREENBACK: str = "\033[42m"
DYELLOWBACK: str = "\033[43m"
DBLUEBACK: str = "\033[44m"
DPINKBACK: str = "\033[45m"
DCYANBACK: str = "\033[46m"
DWHITEBACK: str = "\033[47m"
UPPERLINE: str = "\033[53m"
RED: str   = "\033[91m"
GREEN: str   = "\033[92m"
YELLOW: str   = "\033[93m"
BLUE: str   = "\033[94m"
PINK: str   = "\033[95m"
CYAN: str   = "\033[96m"
WHITE: str   = "\033[97m"
GREYBACK: str = "\033[100m"
REDBACK: str = "\033[101m"
GREENBACK: str = "\033[102m"
YELLOWBACK: str = "\033[103m"
LIGHTBLUEBACK: str = "\033[104m"
PINKBACK: str = "\033[105m"
CYANBACK: str = "\033[106m"
WHITEBACK: str = "\033[107m"


if __name__ == '__main__':
    from Print import Print
    Print(f"{folderInName} {appendingSys}")
    

del os