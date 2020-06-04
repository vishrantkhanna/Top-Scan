#!/usr/bin/python3

import sys
import socket
from datetime import datetime
import terminal_banner
import pyfiglet

# Display name of tool as ASCII art banner
ascii_banner = pyfiglet.figlet_format("Top Scan")
print(ascii_banner)

# Display description of tool as banner
top_banner_tool_desc_text = ("A python script that finds out which ports might be open on a server."
                " Written in Python 3.")
top_banner_tool_desc = terminal_banner.Banner(top_banner_tool_desc_text)
print(top_banner_tool_desc)

print("\n")
print("Scanning top ports....")

top_ports = {
    1: "TCP Port Service Multiplexer (TCPMUX)",
    5: "Remote Job Entry (RJE)",
    7: "ECHO",
    18: "Message Send Protocol (MSP)",
    20: "FTP -- Data",
    21: "FTP -- Control",
    22: "SSH Remote Login Protocol",
    23: "Telnet",
    25: "Simple Mail Transfer Protocol (SMTP)",
    29: "MSG ICP",
    37: "Time",
    42: "Host Name Server (Nameserv)",
    43: "WhoIs",
    49: "Login Host Protocol (Login)",
    53: "Domain Name System (DNS)",
    69: "Trivial File Transfer Protocol (TFTP)",
    70: "Gopher Services",
    79: "Finger",
    80: "HTTP",
    103: "X.400 Standard",
    108: "SNA Gateway Access Server",
    109: "POP2",
    110: "POP3",
    115: "Simple File Transfer Protocol (SFTP)",
    118: "SQL Services",
    119: "Newsgroup (NNTP)",
    137: "NetBIOS Name Service",
    139: "NetBIOS Datagram Service",
    143: "Interim Mail Access Protocol (IMAP)",
    150: "NetBIOS Session Service",
    156: "SQL Server",
    161: "SNMP",
    179: "Border Gateway Protocol (BGP)",
    190: "Gateway Access Control Protocol (GACP)",
    194: "Internet Relay Chat (IRC)",
    197: "Directory Location Service (DLS)",
    389: "Lightweight Directory Access Protocol (LDAP)",
    396: "Novell Netware over IP",
    443: "HTTPS",
    444: "Simple Network Paging Protocol (SNPP)",
    445: "Microsoft-DS",
    458: "Apple QuickTime",
    546: "DHCP Client",
    547: "DHCP Server",
    563: "SNEWS",
    569: "MSN",
    1080: "Socks",
}


# Define our target
def targetHost():
    if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
        banner(target)
    else:
        print("Invalid amount of arguments")
        print("Syntax: python3 scanner.py <ip>")


# Add a pretty banner
def banner(target):
    print("-" * 50)
    print("Scanning target " + target)
    strtTime = str(datetime.now())
    print("Time started: " + strtTime)
    print("-" * 50)
    scanner(target, top_ports)
    print("-" * 50)
    endTime = str(datetime.now())
    print("Time Ended: " + endTime)
    totalTime = endTime-strtTime
    print("Total Time Taken: " + totalTime)
    print("-" * 50)



def scanner(target, top_ports):
    try:
        for port in top_ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(2)
            result = s.connect_ex((target,port))
            if result == 0:
                print("Port {} is open".format(port))
            s.close()
    except KeyboardInterrupt:
        print("\n Exiting scan...")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("Could not connect to server.")
        sys.exit()


if __name__ == "__main__":
    targetHost()