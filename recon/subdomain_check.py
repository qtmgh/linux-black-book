import requests
import socket

def check_subdomain(domain, subdomain):
    url = f"http://{subdomain}.{domain}"
    try:
        response = requests.get(url, timeout=2)
        # If we get a response without exception, subdomain is live
        print(f"[+] Live: {url}")
        return f"{subdomain}.{domain}"
    except requests.RequestException:
        # Subdomain did not respond or does not exist
        print(f"[-] Dead: {url}")
        return None

def port_scan(host):
    common_ports = [21, 22, 23, 80, 443]
    open_ports = []
    for port in common_ports: 
        # create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # set timeout to 3 seconds 
        s.settimeout(5) 
        # try to connect to host on this port
        try:
            s.connect((host,port)) 
            open_ports.append(port) # add ports to open list
            print(f"        [OPEN] Port {port}")
            grab_banner(host, port) # Not subdomain, working with full host)
        except:
            pass # if fails, ignore error
        finally:
            s.close() # Close socket whether success or error


    return open_ports # Returns the list of open ports found



def grab_banner(subdomain, port):
    try:
        # create a socket and set a timeout
        sock = socket.socket()
        sock.settimeout(3)

        # connect to the target
        sock.connect((subdomain, port))

        # receive data (up to 1024 bytes)
        banner = sock.recv(1024).decode().strip()
        print(f"[BANNER] {subdomain}:{port} --> {banner}")
        sock.close()
    except socket.timeout:
        print(f"[!] {subdomain}:{port} timed out.")
    except Exception as e:
        print(f"[!] Could not grab banner from {subdomain}:{port} ({e})")



if __name__ == "__main__":
    domain = input("Enter domain (e.g., example.com): ").strip()
    sub = input("Enter subdomain to check (e.g., www): ").strip()

    full_domain = check_subdomain(domain, sub)
    open_ports = port_scan(full_domain)
    if full_domain:
        port_scan(full_domain)
    if open_ports:
        print(f"Open ports on {full_domain}: {open_ports}")
    else:
        print("No common ports are open.")
