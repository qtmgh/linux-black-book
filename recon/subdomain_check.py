import requests

def check_subdomain(domain, subdomain):
    url = f"http://{subdomain}.{domain}"
    try:
        response = requests.get(url, timeout=2)
        # If we get a response without exception, subdomain is live
        print(f"[+] Live: {url}")
        return True
    except requests.RequestException:
        # Subdomain did not respond or does not exist
        print(f"[-] Dead: {url}")
        return False

if __name__ == "__main__":
    domain = input("Enter domain (e.g., example.com): ").strip()
    sub = input("Enter subdomain to check (e.g., www): ").strip()

    check_subdomain(domain, sub)
