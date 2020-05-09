'''
Dependencies Import
'''

import sys, socket, paramiko, getpass, re, dns.resolver, requests
from scapy.all import *

'''
Tools Import
'''
from tools.hostscan import hostscan
from tools.portscan import portscan
from tools.sniffer import sniffer
from tools.ssh import ssh
from tools.dnsenum import dnsenum
from tools.dirscan import dirscan

# Main Menu
def menu():
    print('''\033[1m
    TOOLS::

    [1] Hostscan            [5] DNS Enum
    [2] Portscan            [6] Dir Scan
    [3] Pass Sniffer        [0] Exit
    [4] SSH Client          
    \033[m''')

    option = int(input('\033[1;31m>\033[m '))

    if option == 1:

        print('\n\033[1;31m[#] =-=NETWORK HOST SCANNER=-=\n\033[m')
        hostscan()
        menu()


    elif option == 2:

        print('\n\033[1;31m[#] =-=TCP PORTSCANNER=-=\n\033[m')
        portscan()
        menu()

    elif option == 3:

        print('\n\033[1;31m[#] =-=Password Sniffer=-=\n\033[m')
        sniffer()
        menu()

    elif option == 4:

        print('\n\033[1;31m[#] =-=SSH Client=-=\n\033[m')
        ssh()
        menu()

    elif option == 5:

        print('\n\033[1;31m[#] =-=DNS Enumerator=-=\n\033[m')
        dnsenum()
        menu()

    elif option == 6:
    
        print('\n\033[1;31m[#] =-=Dir Scanner=-=\n\033[m')
        dirscan()
        menu()
        
    elif option == 0:

        sys.exit(0)

    else:
        
        print('\nInvalid Option \nTry Again')
        menu()


'''
BHPsec STARTS::
'''

# ASCII Print
print('''\033[1;32m
    ____  __  ______     _____                      _ __       
   / __ )/ / / / __ \   / ___/___  _______  _______(_) /___  __
  / __  / /_/ / /_/ /   \__ \/ _ \/ ___/ / / / ___/ / __/ / / /
 / /_/ / __  / ____/   ___/ /  __/ /__/ /_/ / /  / / /_/ /_/ / 
/_____/_/ /_/_/       /____/\___/\___/\__,_/_/  /_/\__/\__, /  
                                                      /____/ By ByteHackr
A tribute Pentest Tool to my Home City(Berhampore,Murshidabad,India)

\033[m''')

# Main Menu Init
menu()
