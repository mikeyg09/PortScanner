import socket
from concurrent.futures import ThreadPoolExecutor

#how many threads (concurrent processes) will be created
n_threads = 200

#Checks to see if a particular port is open
def is_port_open(host, port):

    #AF_INET specifies IPv4, SOCK_STREAM specifies TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        #timeout keeps script from getting stuck
        s.settimeout(3)

        #Tries to connect to port, if successful returns port #
        try:
            s.connect((host, port))
            return port
        except:
            return False

# Creates threads to scan each port
def scan_ports(host):

    #Creates an empty set for the open ports
    open_ports = set()

    #Creates a pool of threads to execute port scans
    with ThreadPoolExecutor(max_workers=n_threads) as executor:
        #empty list for port scan results
        futures = []

        #Iterates over range of ports, checks if port is open, adds result to list
        for port in range(1, 5001):
            futures.append(executor.submit(is_port_open, host, port))

        #Iterates over list of results, if the port was open it is added to open_ports set
        for future in futures:
            result = future.result()
            if result:
                open_ports.add(result)
    return open_ports

if __name__ == '__main__':
    #Takes user input for host IP address
    host = input("Enter the host IP address:")

    #scans host's ports
    open_ports = scan_ports(host)

    #Prints out list of open ports
    if open_ports:
        for port in open_ports:
            print(f"{host}: port {port} is open")
    else:
        print(f"{host} has no open ports")