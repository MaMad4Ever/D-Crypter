from colorama import Fore, init
from time import sleep
import platform


def clean():
    os_type = platform.system()
    if os_type == "Linux":
        return "clear"
    elif os_type == "Windows":
        return "cls"
    else:
        return "clear"

init()

bold = '\033[1m'
endBold = '\033[0m'

def banner():
    print(Fore.RED + """
    ____           ______                             __               
   / __ \         / ____/   _____   __  __    ____   / /_  ___    _____
  / / / / ______ / /       / ___/  / / / /   / __ \ / __/ / _ \  / ___/
 / /_/ / /_____// /___    / /     / /_/ /   / /_/ // /_  /  __/ / /    
/_____/         \____/   /_/      \__, /   / .___/ \__/  \___/ /_/     
                                 /____/   /_/                          """)
    print(bold + Fore.WHITE + """
    -------------------------
    • Developer: MaMad4Ever •
    • Github: MaMad4Ever    •
    • IG: MaMad.web3        •
    -------------------------
""" + endBold)
sleep(0.5)

def line():
    print(Fore.CYAN + "*" * 22)
    sleep(0.1)

def menu():
    print(bold + Fore.WHITE + "[1]" + Fore.LIGHTYELLOW_EX + "Base64" + endBold)
    line()
    
    print(bold + Fore.WHITE + "[2]" + Fore.LIGHTYELLOW_EX + "Hex" + endBold)
    line()

    print(bold + Fore.WHITE + "[3]" + Fore.LIGHTYELLOW_EX + "Rot13" + endBold)
    line()

    print(bold + Fore.WHITE + "[4]" + Fore.LIGHTYELLOW_EX + "Url" + endBold)
    line()

    print(bold + Fore.WHITE + "[5]" + Fore.LIGHTYELLOW_EX + "MD5" + endBold)
    line()

    print(bold + Fore.WHITE + "[6]" + Fore.LIGHTYELLOW_EX + "Decoder" + endBold)
    line()

    print(bold + Fore.WHITE + "[0]" + Fore.LIGHTYELLOW_EX + "Exit" + endBold)
    line()

