import json
from datetime import datetime
from OSQueryMonitoring import (get_listening_ports,get_processes,get_users,pretty)
from NmapScanning import NmapScanning
from OpenvasScan import OpenvasScan


def Nmap_Report(IPaddr):
  Results = NmapScanning(IPaddr)
  Results_list = {}
  for host in Results.all_hosts():
    Results_list[host] ={
    "Host Name": {Results[host].hostname(),
    "State": {Results[host].state(),
    "Open TCP Ports": {Results[host].all_tcp()
    }
  return Results_list


def Osquery_Report(IPaddr):

def OpenVAS_Report(IPaddr):
  
def Full_Report(IPaddr):
  Now = datetime.now().strftime("%a,%b,%d,%Y,%H:%M:%S")
  filename = f"ASM_REPORT_{Now}.json"
  with open(filename,"w") as file:
    json.dump(Nmap_Report(IPaddr),file, indent = 4)


  return filename
