import socket                                                      #collect data 
from IPy import IP                                                 #scan ipaddress

def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[_0 Scanning target ' + str(target))
    for port in range(1, 50):                                      #scan port in the given range
         scan_port(converted_ip, port)

def check_ip(ip):                   
    try:
        IP(ip)                                                     #check if the ip is correc
        return(ip)
    except ValueError:             
        return socket.gethostbyname(ip)                            #to find ip of the given  websites


def get_banner(s):
    return s.recv(1024)                                            #receive server information of open port


def scan_port(ipaddress, port):
    try:
         sock = socket.socket()                                    #collect data
         sock.settimeout(0.5)                                      #time given for scanning port
         sock.connect((ipaddress, port))
         try:
             banner = get_banner(sock)                             #store the information under banner
             print('[+] Port open is ' + str(port) + ':' + str(banner.decode().strip('\n')))
         except:
             print("[+] port " + str(port) + ' is Open')

    except:                                                        #incase port is closed pass to next port
        pass

if __name__ == '__main__':                                         #to implement the given below code in the main fie for printing multiple ipaddress
    targets = input('[+] Enter Target/s To Scan(splits multiple targets with "s") : ')
    if ',' in targets:                                             
           for ip_add in targets.split(','):
              scan(ip_add.strip(' '))
    else:
        scan(targets)