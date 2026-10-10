from NmapScanning import NmapScanning
import socket
def main():

    hostname  =socket.gethostname();
    IPadrr = socket.gethostbyname(hostname);
    NmapScanning(IPaddr)


if __name__ == "__main__":
    main()
