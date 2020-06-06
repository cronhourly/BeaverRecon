from os import system
from utils.colors import *
from utils.iputils import *
from utils.usernameutils import *
from time import sleep
from random import choice
import sys

def cls():
    if sys.platform == 'win32':
        system("cls")
    else:
        system("clear")

def banner():
    print (green + ''' 
 ______
|   __ \.-----.---.-.--.--.-----.----.
|   __ <|  -__|  _  |  |  |  -__|   _|
|______/|_____|___._|\___/|_____|__|
 ______
|   __ \.-----.----.-----.-----.
|      <|  -__|  __|  _  |     |
|___|__||_____|____|_____|__|__|

1. IP
2. Username
3. Name
4. Email
5. Phone
6. Address
7. Passwords
8. Info
''' + reset)

def mainloop():
    try:
        while True:
            icons = ['ツ', '卐', '✦', '☣']
            icon = choice(icons)
            cls()
            banner()
            option = input(purple + "Option:" + reset + bold + " ")
            if option.isnumeric():
                pass
            else:
                cls()
                print (orange + "please enter a number...")
                sleep(2)
                continue
            
            if option == "1":
                try:
                    cls()
                    ip = input(purple + "IP:" + reset + bold + " ")
                    if bool(isgoodipv4(ip)) == True:
                        pass
                    else:
                        cls()
                        print (orange + "please enter a valid ipv4 address...")
                        sleep(2)
                        continue
                    cls()
                    print (f"{reset}{green}{icon}{reset} {blue} Geo Lookup {green}{icon}{reset}")
                    for line in iplookup(ip):
                        print (line)
                    print (f"\n{reset}{green}{icon}{reset} {blue} ThatsThem Lookup {green}{icon}{reset}")
                    for line in thatsthemip(ip):
                        if line == "":
                            print ("None")
                        else:
                            print (line)
                    print (f"\n{reset}{green}{icon}{reset} {blue} Scylla Lookup {green}{icon}{reset}")
                    for x in scyllalookup("IP", ip):
                        print (x)
                    input(purple + "\npress enter to go back: ")
                    continue
                except Exception as e:
                    cls()
                    print ("Error Has Occurred: " + str(e))
                    sleep(2)
                    continue
            
            elif option == "2":
                cls()
                username = input(purple + "Username:" + reset + bold + " ")
                cls()
                print (f"{reset}{green}{icon}{reset} {blue} Scylla Lookup {green}{icon}{reset}")
                for x in scyllalookup("User", username):
                    print (x)
                print (f"{reset}{green}{icon}{reset} {blue} Instagram Lookup {green}{icon}{reset}")
                print(igpartialemail(username))
                input(purple + "\npress enter to go back: ")
                continue
            
            elif option == "3":
                cls()
                username = input(f"{purple}Name:{reset}{bold} ")
                cls()
                
            elif option == "4":
                cls()
                email = input(f"{purple}Email:{reset}{bold} ")
                cls()
                print (f"\n{reset}{green}{icon}{reset} {blue} Scylla Lookup {green}{icon}{reset}")
                for x in scyllalookup("Email", email):
                    print (x)
                input(purple + "\npress enter to go back: ")
                continue

            elif option == "5":
                cls()
                email = input(f"{purple}Phone:{reset}{bold} ")
                cls()
                print (f"\n{reset}{green}{icon}{reset} {blue} Phone Lookup {green}{icon}{reset}")
                input(purple + "\npress enter to go back: ")
                continue
            
            elif option == "6":
                cls()
                email = input(f"{purple}Phone:{reset}{bold} ")
                cls()
                print (f"\n{reset}{green}{icon}{reset} {blue} Phone Lookup {green}{icon}{reset}")
                input(purple + "\npress enter to go back: ")
                continue
            
            elif option == "7":
                cls()
                password = input(f"{purple}Password:{reset}{bold} ")
                cls()
                print (f"\n{reset}{green}{icon}{reset} {blue} Scylla Lookup {green}{icon}{reset}")
                for x in scyllalookup("Password", password)
                print(x)
                input(purple + "\npress enter to go back: ")
                continue
            
            elif option == "8":
                cls()
                print (f"\n{reset}{green}{icon}{reset} {blue} Tool Info {green}{icon}{reset}\n")
                print(f'{bold}{blue}Coded By:{reset} CatLinux\n{bold}{blue}Info:{reset} Tool Made For Reversing Info Quicker For OSINT Uses \n{bold}{blue}Sites Used:{reset} Instagram.com, syclla.sh, ip-api.com, thatsthem.com')
                input(purple + "\npress enter to go back: ")
                continue
    except KeyboardInterrupt:
        print (red + "\nCtrl-C Pressed Exiting..." + reset)
        sys.exit()
mainloop()
