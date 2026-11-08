from OSQueryMonitoring import (get_listening_ports,get_processes,get_users,pretty)
from NmapScanning import NmapScanning
from ReportFinding import Full_Report
from SendReport import SendReport
import socket

def main():

    hostname  =socket.gethostname();
    IPaddr = socket.gethostbyname(hostname);
    Full_Report = ReportFinding(IPaddr)
    SendReport(FullReport)
if __name__ == "__main__":
    main()
