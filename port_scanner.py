import socket
import threading
import argparse
from utils import scan_port, print_report

def scan_ports(target_ip, ports):
    open_ports = []
    def scan(port):
        if scan_port(target_ip, port):
            open_ports.append(port)
    
    threads = []
    for port in ports:
        thread = threading.Thread(target=scan, args=(port,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return open_ports

def main():
    parser = argparse.ArgumentParser(description="Python Port Scanner")
    parser.add_argument("target", help="Target IP address")
    parser.add_argument("ports", help="Comma-separated list of ports to scan")
    args = parser.parse_args()
    
    target_ip = args.target
    ports = [int(port) for port in args.ports.split(",")]
    
    open_ports = scan_ports(target_ip, ports)
    print_report(target_ip, open_ports)

if __name__ == "__main__":
    main()
