from os import system
import sys
from colorama import Fore , init
from time import sleep
from base64 import b64encode
import codecs
import hashlib
import urllib.parse
from Banner import banner, menu, bold, endBold, clean
import Decoder

init()

while (True):
    try:
        system(clean())
        banner()
        menu()
        option = int(input(bold + Fore.RED + "[*] Tools" + Fore.WHITE + "/home → " + endBold))

        if (option == 1):
            system(clean())
            banner()
            print(Fore.WHITE + "Enter Your Text:")
            user_option = input(bold + Fore.RED + "[*] Tools" + Fore.WHITE + "/home/base64 → " + endBold)
            print(bold + Fore.WHITE + "Encrypted!\n" + endBold)
            byte_data = user_option.encode('ascii')
            encoded_data = b64encode(byte_data)
            Encrypted = encoded_data.decode('ascii')
            print(Fore.WHITE + Encrypted)
            input(bold + Fore.GREEN + "Press Any Key..." + endBold)
            continue

        elif (option == 2):
            system(clean())
            banner()
            print(Fore.WHITE + "Enter Your Text:")
            user_option = input(bold + Fore.RED + "[*] Tools" + Fore.WHITE + "/home/Hex → " + endBold)
            print(bold + Fore.WHITE + "Encrypted!\n" + endBold)
            result_string = user_option.encode("utf-8").hex()
            print(result_string)
            input(bold + Fore.GREEN + "Press Any Key..." + endBold)
            continue

        elif (option == 3):
            system(clean())
            banner()
            print(Fore.WHITE + "Enter Your Text:")
            user_option = input(bold + Fore.RED + "[*] Tools" + Fore.WHITE + "/home/Rot13 → " + endBold)
            rot13 = codecs.encode(user_option, 'rot_13')
            print(bold + Fore.WHITE + "Encrypted!\n" + endBold)
            print(rot13)
            input(bold + Fore.GREEN + "Press Any Key..." + endBold)
            continue

        elif (option == 4):
            system(clean())
            banner()
            print(Fore.WHITE + "Enter Your Text:")
            user_option = input(bold + Fore.RED + "[*] Tools" + Fore.WHITE + "/home/Url → " + endBold)
            url = urllib.parse.quote(user_option)
            print(bold + Fore.WHITE + "Encrypted!\n" + endBold)
            print(url)
            input(bold + Fore.GREEN + "Press Any Key..." + endBold)
            continue

        elif (option == 5):
            system(clean())
            banner()
            print(Fore.WHITE + "Enter Your Text:")
            user_option = input(bold + Fore.RED + "[*] Tools" + Fore.WHITE + "/home/MD5 → " + endBold)
            md5_hash = hashlib.md5()
            md5_hash.update(user_option.encode('utf-8'))
            md5 = md5_hash.hexdigest()
            print(bold + Fore.WHITE + "Encrypted!\n" + endBold)
            print(md5)
            input(bold + Fore.GREEN + "Press Any Key..." + endBold)
            continue

        elif (option == 6):
            system(clean())
            banner()
            Decoder.decoder_menu()
            user_option = int(input(bold + Fore.RED + "[*] Tools" + Fore.WHITE + "/home/Decoder → " + endBold))
            Decoder.decoder(user_option)
            continue
        
        elif (option == 0):
            system(clean())
            banner()
            print(bold + Fore.RED + "Tnx For Using My Tools" + endBold)
            sleep(1)
            break
            
    except:
        print(Fore.RED + "Invalid")
        sleep(2)
        sys.exit()