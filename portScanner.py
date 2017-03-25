#! /usr/bin/env python
from socket import *
import sys,time
from datetime import datetime

host='' #string
portList=[20,21,22,23,24,25,53,80,110,344,443] #ports to b searched
#supply aditional ports as necessary
def scanHost(host,port,r_code=1):
    try:
        s=socket(AF_INET,SOCK_STREAM)
        code = s.connect_ex((host,port))

        if code== 0:
            r_code=code
        s.close()
    except Exception, e:
        pass
    return r_code
def main():

    try:
        host=raw_input("[+] Enter Host Address: ")
    except KeyboardInterrupt:
        print("\n\n[*] User requested to Interrupt.")
        print("[*] Application shutting Down.")
        sys.exit(1)

    host_ip = gethostbyname(host) #get host's ip

    print ("\n[+] Host: %s IP: %s" % (host,host_ip))
    print ("[*] Scan started at %s...\n" % (time.strftime("%H:%M:%S")))
    start_time=datetime.now()

    for port in portList:
        try:
            response= scanHost(host,port)
            if response==0:
                print("[+] Port %d: Open" %(port))
        except Exception, e:
            pass
    stop_time=datetime.now()
    time_duration=stop_time- start_time
    print("\n[*] Scanning finished at %s..." % (time.strftime("%H:%M:%S")))
    print("[*] Scanning duration: %s..."% (time_duration))

if __name__=='__main__':
    main()
