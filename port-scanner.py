import socket
import sys

def scan_ports(host='127.0.0.1', start_port=20, end_port=30):
    # Input validation
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Invalid port range provided.")
        return

    print(f"Scanning {host} from port {start_port} to {end_port}...")
   
    # Attempt to resolve host
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Invalid host or host unreachable.")
        return

    for port in range(start_port, end_port + 1):
        # Create a new socket for each attempt
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # Set timeout to half a second for quicker scans
       
        try:
            result = s.connect_ex((remote_ip, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            else:
                print(f"Port {port}: CLOSED")
        except socket.error as e:
            print(f"Error scanning port {port}: {e}")
        finally:
            s.close()

if __name__ == "__main__":
    # You can parse command line arguments or hardcode values for demonstration.
    # Example usage:
    # python3 port_scanner.py localhost 20 30
    # For demonstration, just run: python3 port_scanner.py
    # and it will scan localhost ports 20 to 30.

    # Basic argument handling (not strictly required, but good to demonstrate)
    if len(sys.argv) == 4:
        host = sys.argv[1]
        try:
            start_port = int(sys.argv[2])
            end_port = int(sys.argv[3])
        except ValueError:
            print("Port values must be integers.")
            sys.exit(1)
       
        scan_ports(host, start_port, end_port)
    else:
        # Default scan if no arguments provided
        scan_ports('127.0.0.1', 20, 30)