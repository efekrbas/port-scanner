import socket
import subprocess
import sys
import os
import concurrent.futures
from datetime import datetime
import ipaddress

# clear the screen (cross-platform)
subprocess.call("cls" if os.name == "nt" else "clear", shell=True)

# print welcome message
print("Welcome to Port Scanner")
print("-" * 60)

# take the target IP or domain input from the user
target = input("Enter a remote host to scan (IP address or domain): ")

try:
    ip = ipaddress.ip_address(target) # validate if the IP is correct, if so continue
except ValueError:
    try:
        target = socket.gethostbyname(target) # try to resolve domain
    except socket.gaierror:
        print("-" * 60)
        print("Hostname or IP address {} is not valid".format(target))
        print("Quitting...")
        print("-" * 60)
        sys.exit()

# enter the port range to scan 
port_range = input("Enter the range to scan (ex. 40-100): ")
port_from = port_range.split("-")[0]
port_to = port_range.split("-")[1]

# print an empty line for better readability
print()

# create the banner before scanning
print("-" * 60)
print("Please wait, scanning the host", target, " from port ", port_from, " - " , port_to)
print("-" * 60)

# record the exact time the scan started
time_started = datetime.now()

# define the function to scan a single port
def scan_port(port):
    try:
        # AF_INET specifies IPv4, SOCK_STREAM specifies TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5) # timeout set to 0.5 seconds to prevent hanging
        result = sock.connect_ex((target, port))
        if result == 0: # if result is 0, it means the connection was successful and the port is open
            print("Port", port, "is open")
        sock.close()
    except Exception:
        pass

try:
    # utilize ThreadPoolExecutor for blazing fast multi-threaded scanning (up to 1000 concurrent threads)
    with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
        # +1 ensures the last port entered by the user is also scanned
        ports_to_scan = range(int(port_from), int(port_to) + 1)
        executor.map(scan_port, ports_to_scan)

except KeyboardInterrupt:
    print("You pressed Ctrl+C.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Couldn't connect to server.")
    sys.exit()

time_end = datetime.now()

time_diff = time_end - time_started

print("Scan completed in", time_diff)