# Networking Commands

## ifconfig
Used to display and configure network interface information

## ip a
Shows all your network interfaces and their IPs

## ip route 
Displays the routing table -- where traffic gets sent.

## ping -c 4 google.com
Sends 4 ICMP packets to Google and shows response time. 

## netstat -tuln
Shows active TCP/UDP sockets. Great for seeing open ports. 

## dig google.com 
Gets DNS information about a domain.

# nmap -s5 localhost 
Scans your own machine for open ports using a stealth SYN scan. 

## traceroute google.com
Shows the hops (routers) your packets take to reach Google. 

## arp -a
Lists IPs and MAC addresses of devices on the LAN.
