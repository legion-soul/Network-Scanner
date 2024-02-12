import nmap
import socket
import re
import time

# Validation Functions
def validate_ip_or_cidr(target):
    cidr_pattern = r"^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(\/([0-9]|[1-2][0-9]|3[0-2]))$"
    ip_pattern = r"^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"
    return re.match(cidr_pattern, target) or re.match(ip_pattern, target)

def validate_nmap_option(option):
    basic_pattern = r"^-[A-Za-z0-9]+$" 
    return re.match(basic_pattern, option) is not None

# Input with Validation 
target = ""
while True:
    target = input("Enter target IP address or network range (e.g., 192.168.1.0/24 or 192.168.1.10): ")
    if validate_ip_or_cidr(target):
        break
    else:
        print("Invalid IP address or CIDR notation. Please try again.")

nmap_option = ""
while True:
    nmap_option = input("Enter desired Nmap scan option (e.g., -sV, -O, -sP): ")
    if validate_nmap_option(nmap_option):
        break
    else:
        print("Invalid Nmap option format. Should start with '-' and use common flags.")

# Nmap Scanning 
print("-" * 50)
print("Scanning target network: " + target)
print("Using Nmap option:", nmap_option)
print("-" * 50)

nm = nmap.PortScanner()
nm.scan(hosts=target, arguments=nmap_option) 

print("Scan Progress: 100%") 

# Result Formatting (Text Report)
with open("nmap_scan_results.txt", "w") as output_file:
    output_file.write("-" * 50 + "\n")
    output_file.write(f"Scan Results for Target: {target}\n")
    output_file.write(f"Nmap Option: {nmap_option}\n")
    output_file.write("-" * 50 + "\n")

    host_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    output_file.write(f"{len(host_list)} hosts scanned.\n\n")

    output_file.write("Alive Hosts:\n")
alive_hosts = []  # Start with an empty list
for host, status in host_list:
    if nm[host]['status']['state'] == 'up':  # Nmap marked it as 'up'
        alive_hosts.append(host)
    else: 
        # Check if ANY ports are open
        for port in nm[host]['tcp'].keys():
            if nm[host]['tcp'][port]['state'] == 'open':
                alive_hosts.append(host)
                break  # Found an open port, no need to keep checking 

# Enhancement: Also consider hosts with open ports
for host, status in host_list:
    if nm[host]['status']['state'] == 'up':  # If host was determined 'up'
        alive_hosts.append(host)
    else: 
        # Check if ANY ports are open for this host
        for port in nm[host]['tcp'].keys():
            if nm[host]['tcp'][port]['state'] == 'open':
                alive_hosts.append(host)
                break  # No need to check further ports if we know at least one is open

print(nm.get_nmap_last_output())
