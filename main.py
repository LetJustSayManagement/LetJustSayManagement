from Run_Osquery import (get_listening_ports,get_processes,get_users,pretty)
from NmapScanning import NmapScanning
from ReportFinding import Write_Report
from SendReport import SendReport
import socket

def main():

    hostname  =socket.gethostname();
    IPaddr = socket.gethostbyname(hostname);
    Full_Report = Write_Report(IPaddr)
    SendReport(Full_Report)
if __name__ == "__main__":
    main()




