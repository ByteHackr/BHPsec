import sys, socket, paramiko, getpass, re, dns.resolver, requests
from scapy.all import *
def dirscan():
    while True:
        url = input('Type the URL Target > ')
        if url[0:4] != 'http':
            print('Missing HTTP/HTTPS in URL')
        else:
            break

    worl = open('src/wordlists/dir-wordlist-small.txt').read().splitlines()

    print('[+] Scanning...')

    try:
        for word in worl:

            nurl = url + '/' + word
            res = requests.get(nurl)

            if res.status_code == 200:
                print(f'\033[1;32m[!] FIND ===> {nurl}\033[m')

    except Exception as error:
        print('\033[1;31m[!] An error Ocurred \033[m')

    print('\033[1;31m[#] Scan Finished!\033[m')