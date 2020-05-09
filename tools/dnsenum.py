import sys, socket, paramiko, getpass, re, dns.resolver, requests
from scapy.all import *
def dnsenum():
    opt = input('Do you want use your own wordlist?\n[1] Yes\n[2] No\n> ')

    if opt == '1':
        arq = open(input('\nType the wordlist name/location > '))
        rea = arq.read().splitlines()
    elif opt == '2':
        arq = open('src/wordlists/subdomains-100.txt')
        rea = arq.read().splitlines()
    else:
        print('\nInvalid Option \nTry Again')
        dnsenum()

    while True:
        target = input('\nType the Target URL > ')
        if '.com' or '.org' in target:
            print('\n[#] Scanning...\n\n')
            for sub in rea:
                try:
                    dom = f'{sub}.{target}'
                    req = dns.resolver.query(dom, 'a')
                    for sucess in req:
                        print(f'\033[1;32m[!] Subdomain Found => {dom} : {sucess}\033[m')
                except:
                    pass
            print('\033[1;31m[#] Scan Finished!\033[m')
            break
        else:
            print('Invalid URL \nTry Again\n')