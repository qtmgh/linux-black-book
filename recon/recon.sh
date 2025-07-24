#!/bin/bash

echo "[*] Your IP address: "
ip a | grep 'inet ' | grep -v 127.0.0.1 | awk '{print $2}'
echo

echo "[*] Live hosts on your network: "
ip r | grep default | awk '{print $3}' | xargs -I{} nmap -sn {}/24
echo

echo "[*] Open ports on this machine: "
sudo netstat -tulpn | grep LISTEN

read -p "[?] Enter domain to lookup: " domain
dig +short $domain
echo

read -p "[?] Enter a domain for WHOIS lookup: " whois_domain
echo "[*] WHOIS info for $whois_domain: "
whois $whois_domain | head -n 20
echo

read -p "[?] Enter a domain for DNS lookup: " dns_domain
echo "[*] Resolving IP address for $dns_domain..."
dig +short $dns_domain
echo
