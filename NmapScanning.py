""" 
    This is the Nmap scanner. 
    We first import and create a new scannaer. 
    Then we set up the destination, range, and how the scanner will act.
    next we will loop through each host printing the results.
"""
import nmap

def NmapScanning(Ipaddr):
  scanner = nmap.PortScanner()
  scanner.scan(Ipaddr, '1-65535', arguments='-sT -T4')
  for host in scanner.all_hosts():
    print(f"host: {host}")
    print(f"Host Name: {scanner[host].hostname()}")
    print(f"Host State: {scanner[host].state()}")
    print(f"Open TCP Ports: {scanner[host].all_tcp()}")
