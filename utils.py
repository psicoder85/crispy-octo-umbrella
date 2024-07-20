import socket

def scan_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        try:
            s.connect((ip, port))
            return True
        except (socket.timeout, socket.error):
            return False

def print_report(ip, open_ports):
    print(f"Open ports on {ip}:")
    for port in open_ports:
        print(f"Port {port} is open")
