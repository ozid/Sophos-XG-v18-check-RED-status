#!/usr/bin/python3
__author__ = "Olivier Lamarque"
import paramiko as paramiko
from paramiko import SSHClient
import sys
import re
sophos_host = sys.argv[1]

ssh = SSHClient()
ssh.load_system_host_keys()


ssh.connect(sophos_host, username='admin', password='password', key_filename='/home/nagios/.ssh/sophosxg')
stdin, stdout, stderr = ssh.exec_command('/bin/sh', get_pty=True)
stdin.write('''
grep "Red devices:" /log/red.log | tail -1
exit
''')
for line in iter(stdout.readline, ""):
    if "REDD" in line:
        ##see output##
        #print(line)
        numbers = [int(word) for word in line.split() if word.isdigit()]
        #print(numbers[3])
        if numbers[3] > 0:
            print(numbers[3], "RED device disconnected")
            sys.exit(2)
        else:
            print("All RED are UP")
            sys.exit(0)

stdout.close()
stdin.close()
ssh.close()
