import os, platform, sys
appendingSys: str = str(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(f"{appendingSys}")
del appendingSys
from imports import *
from variables import *

@overload
def clear() -> None: ...
@overload
def clear(specifier: str) -> None: ...

def clear(specifier: Optional[str] = None) -> None:
    if specifier is None:
        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Linux" :
            os.system("clear")
        else:
            print("Clear system not functional on this operating system.")
    else:
        print(f"If you can see this, function '{YELLOW}clear{WHITE}(){RESET}' did not work because '{BLUE}specifier{RESET} : {RED}{specifier}{RESET}' is incorrect or in-operable.")
        os.system(specifier)

