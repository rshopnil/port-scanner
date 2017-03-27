#! /usr/bin/env python
#script for scanning tcp ports
#this program takes cmd line args
#define methods in camelCase, variables in snake_case
import optparse #required for cmd line arg passing
import socket
from socket import*
from threading import*
screenLock= Semaphore(value=1) #for controlling the printing of diff threads

def connScan(target_host,target_port):
    try:
        connSkt=socket(AF_INET,SOCK_STREAM) #tcp
        connSkt.connect((target_host,target_port))
        connSkt.send("GarbageData\r\n") #for banner grabing
        results=connSkt.recv(100)
        screenLock.acquire()
        print ("[*] %d/tcp !!! open !!!" %target_port)
        print ("[^] "+ str(results))

    except:
        screenLock.acquire()
        print("[#] %d/tcp closed" % target_port)

    finally:
        screenLock.release()
        connSkt.close()

def portScan(target_host,target_ports):

    try:
        target_ip=gethostbyname(target_host)
    except:
        print("[-] Cannot resolve '%s': Unknown host" % target_host)
        return

    try:
        target_name=gethostbyip(target_ip)
        print("\n[+] Scan results for: "+target_name[0])
    except:
        print ("\n[+] Scan results for: "+ target_ip)
    setdefaulttimeout(1)

    for target_port in target_ports: #call connScan with threading
        t= Thread(target=connScan, args=(target_host,int(target_port)))
        t.start()

def main():
    parser=optparse.OptionParser('usage %prog -H'+\
        '<target host> -p <target port>')
    parser.add_option('-H', dest='target_host', type='string',\
        help='specify target host')
    parser.add_option('-p', dest='target_port', type='string',\

        help='specify target port[s] separated by comma')
    (options,args)= parser.parse_args()
    target_host= options.target_host
    target_ports= str(options.target_port).split(',')

    if (target_host==None) | (target_ports[0]==None):
        print ("[-] You must specify target Host and Port[s]")
        exit(0)

    portScan(target_host,target_ports)
if __name__=='__main__':
    main()
