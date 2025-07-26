from scapy.all import ARP, Ether, srp
import requests

def get_vendor(mac):
    url = f"https://api.macvendors.com/{mac}" # Construct API URL with MAC address

    try:
        response = requests.get(url, timeout =3) # Send GET request to the API, 3 second timeout

        if response.status_code == 200:
            return response.text # If successful, return vendor name
        else:
            return "Vendor not found" # If the API responds with error, return message
    except requests.RequestException as e:
            return f"Error:{e}" # If request fails, return error message (network error, timeout, etc.)



def scan_network(ip_range):
    # Create ARP request
    arp = ARP(pdst=ip_range)
    # Create Ethernet frame to broadcast to all devices
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Stack them together
    packet = ether/ arp 

    # Send the packet and capture the responses
    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        mac = received.hwsrc
        vendor = get_vendor(mac) # Look up vendor here
        devices.append({
            "ip": received.psrc,
            "mac": mac,
            "vendor": vendor
            })
    return devices


if __name__ == "__main__":
    target_range = input("Enter your IP range: ").strip()
    scanned_devices = scan_network(target_range)

    print("\nDiscovered Devices: ")
    for device in scanned_devices:
        print(f"{device['ip']} \t {device['mac']} \t Vendor: {device['vendor']}")
