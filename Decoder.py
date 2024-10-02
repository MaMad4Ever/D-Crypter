from os import system
import sys
from colorama import Fore, init
from time import sleep
from base64 import b64decode
import codecs
import urllib.parse
from Banner import banner, line, bold, endBold, clean

init()


def decoder_menu():
    print(bold + Fore.WHITE +"[1]" +Fore.LIGHTYELLOW_EX + "Base64" + endBold)
    print(Fore.CYAN + "*" * 22)
    sleep(0.1)

    print(bold + Fore.WHITE +"[2]" +Fore.LIGHTYELLOW_EX + "Hex" + endBold)
    print(Fore.CYAN + "*" * 22)
    sleep(0.1)

    print(bold + Fore.WHITE +"[3]" +Fore.LIGHTYELLOW_EX + "Rot13" + endBold)
    print(Fore.CYAN + "*" * 22)
    sleep(0.1)

    print(bold + Fore.WHITE +"[3]" +Fore.LIGHTYELLOW_EX + "Url" + endBold)
    print(Fore.CYAN + "*" * 22)
    sleep(0.1)

    print(bold + Fore.WHITE +"[0]" +Fore.LIGHTYELLOW_EX + "Back" + endBold)
    print(Fore.CYAN + "*" * 22)
    sleep(0.1)


def decoder(user_input):
    if (user_input == 1):
        system(clean())
        banner()
        print(Fore.WHITE + "Enter Your Encrypted text in base64")
        user_option = input(bold + Fore.RED + "[*] Tools" + Fore.WHITE + "/home/decoder/base64 → " + endBold)
        print(bold + Fore.WHITE + "Decrypted!\n" + endBold)
        base64_bytes = user_option.encode('ascii')
        decoded_data = b64decode(base64_bytes)
        Decrypted = decoded_data.decode('ascii')
        print(Fore.WHITE + Decrypted)
        input(bold + Fore.GREEN + "Press Any Key..." + endBold)

    elif (user_input == 2):
        system(clean())
        banner()
        print(Fore.WHITE + "Enter Your Encrypted text in Hex")
        user_option = input(bold + Fore.RED + "[*] Tools" + Fore.WHITE + "/home/decoder/Hex → " + endBold)
        result_string = codecs.decode(user_option, 'hex').decode('utf-8')
        print(bold + Fore.WHITE + "Decrypted!\n" + endBold)
        print(result_string)
        input(bold + Fore.GREEN + "Press Any Key..." + endBold)

    elif (user_input == 3):
        system(clean())
        banner()
        print(Fore.WHITE + "Enter Your Encrypted text in Rot13")
        user_option = input(bold + Fore.RED + "[*] Tools" + Fore.WHITE + "/home/decoder/Rot13 → " + endBold)
        text = codecs.decode(user_option, 'rot_13')
        print(bold + Fore.WHITE + "Decrypted!\n" + endBold)
        print(text)
        input(bold + Fore.GREEN + "Press Any Key..." + endBold)

    elif (user_input == 4):
        system(clean())
        banner()
        print(Fore.WHITE + "Enter Your Encrypted text in Url")
        user_option = input(bold + Fore.RED + "[*] Tools" + Fore.WHITE + "/home/decoder/Url → " + endBold)
        text = urllib.parse.unquote(user_option)
        print(bold + Fore.WHITE + "Decrypted!\n" + endBold)
        print(text)
        input(bold + Fore.GREEN + "Press Any Key..." + endBold)
        
    elif (user_input == 0):
        pass

    else:
        print(bold + Fore.RED + "Bad Input..." + endBold)
        sleep(2)
        sys.exit