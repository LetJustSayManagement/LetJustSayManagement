from OSQueryMonitoring import (get_listening_ports,get_processes,get_users,pretty)
from NmapScanning import NmapScanning
from ReportFinding import ReportFinding
from SendReport import SendReport
import socket

def main():

    hostname  =socket.gethostname();
    IPaddr = socket.gethostbyname(hostname);
    Full_Report = ReportFinding(IPaddr)
    SendReport(Full_Report)
if __name__ == "__main__":
    main()
