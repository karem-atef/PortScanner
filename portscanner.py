#!/bin/python3

# importing modules 
import sys
import socket
from datetime import datetime

# Define out target 
if (len(sys.argv) == 2):
    target = socket.gethostbyname(sys.argv[1]) # translate host to ipv4 
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 portscanner.py <ip>")

# Add a pretty banner 
print("-" * 50)
print("Scanning Target : "+ target)
print("Starting Time : "+ str(datetime.now()))
print("-" * 50)

# The process 
try:
    for port in range(50,80):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
except KeyboardInterrupt:
    print("\n Exiting Program !.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to the server.")
    sys.exit()