import sys, socket, paramiko, getpass, re, dns.resolver, requests
from scapy.all import *
def portscan():
    target = input('Target IP > ')  # Example: 192.168.0.10

    def sock_connect(target, port):
        client = socket.socket()
        client.settimeout(0.03)

        code = client.connect_ex((target, int(port)))
        if code == 0:
            print(f'\033[1;32m[!] Port {port} OPEN!\033[m')
        client.close()

    print(f'\n[+] Scanning {target} ...\n\n')

    for port in range(1, 65535):
        sock_connect(target, port)

    print('\n\n\033[1;31m[#] Scan Finished\n\n\033[m')
