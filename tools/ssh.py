import sys, socket, paramiko, getpass, re, dns.resolver, requests
from scapy.all import *
def ssh():
    def connect():
        try:
            print('Type q() to exit\n')
            host = input('Host IP > ') # Example: 23.178.13.200
            if host == 'q()':
                menu()

            user = input('Username > ') # Example: root
            if user == 'q()':
                menu()

            passwd = getpass.getpass('Password > ') # User password (Hidden input)
            if passwd == 'q()':
                menu()

            cl.connect(host, username=user, password=passwd)
            print(f'\n\nConnected on {user}:{host}\nType "q()" to quit\n')

        except Exception as error:
            print('\nAutentication Error \nTry Again\n')
            connect()

    cl = paramiko.SSHClient()
    cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    connect()
    cn = True
    while cn:
        command = input('> ')
        if command == 'q()':
            cn = False
        else:
            stdin, stdout, stderr = cl.exec_command(command)
            print(stdout.readlines())