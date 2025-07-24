import socket

def resolve_domain(domain):
    try: 
        ip = socket.gethostbyname(domain)
        print(f"{domain} resolves to {ip}")
    except socket.gaierror:
        print(f"Failed to resolve {domain}")

if __name__ == "__main__":
    domain = input("Enter domain to resolve: ")
    resolve_domain(domain)
