import json
from datetime import datetime
from Run_Osquery import (get_listening_ports,get_processes,get_users,pretty)
from NmapScanning import NmapScanning
from OpenvasScan import OpenvasScan


def Nmap_Report(IPaddr):
  Results = NmapScanning(IPaddr)
  Results_list = {}
  for host in Results.all_hosts():
    Results_list[host] ={
    "Host Name": Results[host].hostname(),
    "State": Results[host].state(),
    "Open TCP Ports": Results[host].all_tcp()
    }
  return Results_list

def Osquery_Report():
  return{
    "Listening Ports: ": get_listening_ports(),
    "Processes: ": get_processes(),
    "Users: " :get_users()
  }
  
def OpenVAS_Report(IPaddr):
    Results = OpenvasScan(IPaddr)
    return "scan Finding": Results
def OpenVAS_Recommendations
    Results = openvasScan(IPaddr)
    return "Hardening Recommendation :" 
def Full_Report(IPaddr):
  return {"Nmap" : Nmap_Report(IPaddr),
          "OSquery" : Osquery_Report()
         }

def Write_Report(IPaddr):
  Now = datetime.now().strftime("%a,%b,%d,%Y,%H:%M:%S")
  filename = f"ASM_REPORT_{Now}.json"
  with open(filename,"w") as file:
    json.dump(Full_Report(IPaddr),file, indent = 4)


  return filename
