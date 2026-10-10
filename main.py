from OSQueryMonitoring import (get_listening_ports,get_processes,get_users)
from NmapScanning import NmapScanning
import socket
def main():

    hostname  =socket.gethostname();
    IPadrr = socket.gethostbyname(hostname);
    NmapScanning(IPaddr)
    print(get_listening_ports())
    print(get_processes())
    print(get_users())

if __name__ == "__main__":
    main()
