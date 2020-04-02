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
                                                                                                         `--/:`                        
                                                                                                     ./ydmNNMNh                         
                                                                                                  `:hhsNMMMMMMN:                        
                                                                                               -:odNMNNMMMMMMMm/                        
         __                                                                                   smNMMMMMMMMMMMMMN-                        
        |  |--.-----.---.-.--.--.-----.----.                                                  /NMMMMMMMMMMMMMMd`                        
        |  _  |  -__|  _  |  |  |  -__|   _|                                                  +NMMMMMMMMMMMMMN/                         
        |_____|_____|___._|\___/|_____|__|                                                  `+NMMMMMMMMMMMMMNo                          
                                                                                          .+dMMMMMMMMMMMMMMMd`                          
                                                                                       `-+ymMMMMMMMMMMMMMMMMMN+                         
        .----.-----.----.-----.-----.                                              `-+ydNMMMMMMMMMMMMMMMMMMMMMm+.                       
        |   _|  -__|  __|  _  |     |                                            -odNMMMMMMMMMMMMMMMMMMMMMMMNddmd/-`                    
        |__| |_____|____|_____|__|__|                                           .smMMMMMMMMMMMMMMMMMMMMMMMMMNs.`.:+y/                   
                                                                              -dMMMMMMMMMMMMMMMMMMMMMMMMMMMN:                           
        1. IP                                                                -mMMMMMMMMMMMMMMMMMMMMMMMMMMMMN.                           
        2. Username                                                         `dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh                            
        3. Name                                                             +NMMMMMMMMMMMMMMMMMMMMMMMMMMMMN:                            
        4. Email                                                            hMMMMMMMMMMMMMMMNmdmmNMMMMMMMMo                             
        5. Address                                                          mMMMMMMMMMMMMMMMMNmdyo+dMMMMNs`                             
        6. Phone                                                            mMMMMMMMMMMMMMMMMMMMMNs.dMMm+`                              
        7. Settings                                     `/oyyhhhyyyso+:-..``hMMMMMMMMMMMMMMMMMMMMMN`smy-                                
                                                        hMMMMMMMMMMMMMMMNmdhmMMMMMMMMMMMMMMMMMMMMMy`+-`                                 
                                                        +dNNMMMMMMMMMMMNNNmmmNNMMMNNmdddmNNMMMMMMNsoossso+:                             
                                                        `.://+++++///::--.``--::::.`   `.:::::::::::::::::`                             
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
    except KeyboardInterrupt:
        print (red + "\nCtrl-C Pressed Exiting..." + reset)
        sys.exit()
mainloop()