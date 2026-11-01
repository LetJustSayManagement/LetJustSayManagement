import json
from datetime import datetime
from OSQueryMonitoring import (get_listening_ports,get_processes,get_users,pretty)
from NmapScanning import NmapScanning
from OpenvasScan import OpenvasScan
def Nmap_Report(IPaddr):
  Results = NmapScanning(IPaddr)
  for (ports in Results):
    print("===PORTS===")
    print(f"{port}")
def Osquery_Report(IPaddr):

def OpenVAS_Report(IPaddr):
  
Now = datetime.datetime.now().strftime("%a,%b,%d,%Y,%H:%M:%S")
filename = f"ASM_REPORT_{Now}.json"
with open(filename,"w") as file:
    
