from OSQueryMonitoring import (get_listening_ports,get_processes,get_users,pretty)
from NmapScanning import NmapScanning
import socket
def main():

    hostname  =socket.gethostname();
    IPaddr = socket.gethostbyname(hostname);
    NmapScanning(IPaddr)
    print(pretty(get_listening_ports()))
    print(pretty(get_processes()))
    print(pretty(get_users()))

if __name__ == "__main__":
    main()
