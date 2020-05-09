import sys, socket, paramiko, getpass, re, dns.resolver, requests
from scapy.all import *
def hostscan():
    try:
        target = input('Gateway IP > ')  # Example: 192.168.0.1

        def scan(ip):
            arping(ip + '/24')

        scan(target)
        print('\n\n\033[1;31m[#] Scan Finished\n\n\033[m')

    except Exception as error:
        if '[Errno 1] Operation not permitted' in str(error):
            print('Privileges Error \nTry run with "sudo"')