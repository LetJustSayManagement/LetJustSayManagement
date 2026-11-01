from OSQueryMonitoring import (get_listening_ports,get_processes,get_users,pretty)
from NmapScanning import NmapScanning
import socket
def main():

    hostname  =socket.gethostname();
    IPaddr = socket.gethostbyname(hostname);

if __name__ == "__main__":
    main()
