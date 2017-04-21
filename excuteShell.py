#!/usr/bin/env python
import os
import paramiko
import time
import sys
import threading


# USERNAME PASSWORD
username = sys.argv[1]
password = sys.argv[2]
# Target machine address
start_IP = 90
end_IP = 100
# Excute the shell command
shell_command = "date"

def excute_shell(ip, username, password, cmd):
    try:
        # Excute the shell command
        ssh =paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip,username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()
        ssh.close()
        time.sleep(1)
        print("#############################################")
        print ip
        print result
    except Exception, e:
        print("####  ERROR  ################  ERROR  #######")
        print ip, str(e)

def main():
    # IP format 
    format_IP = "77.12.56."   
    list_IP = range(start_IP, end_IP+1)
    threads = []
 
    for num in list_IP:
        # Assemble IP address
        ip = format_IP + str(num)
        t = threading.Thread(target=excute_shell, args=(ip, username, password, shell_command))
        threads.append(t)
    # Start thread
    for i in range(len(list_IP)):
        threads[i].start()

    for i in range(len(list_IP)):
        threads[i].join()

if __name__ == "__main__":

    main()
