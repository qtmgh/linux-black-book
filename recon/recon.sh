#!/bin/bash

RESULTS_DIR="results"
mkdir -p $RESULTS_DIR


echo "[*] Your IP address: " | tee $RESULTS_DIR/ip_address.txt
ip a | grep 'inet ' | grep -v 127.0.0.1 | awk '{print $2}' | tee -a $RESULTS_DIR/ip_address.txt
echo | tee -a $RESULTS_DIR/ip_address.txt

echo "[*] Live hosts on your network: " | tee $RESULTS_DIR/live_hosts.txt
ip r | grep default | awk '{print $3}' | xargs -I{} nmap -sn {}/24 | tee -a $RESULTS_DIR/live_hosts.txt
echo | tee -a $RESULTS_DIR/live_hosts.txt

echo "[*] Open ports on this machine: " | tee $RESULTS_DIR/open_ports.txt
sudo netstat -tulpn | grep LISTEN | tee -a $RESULTS_DIR/open_ports.txt
echo | tee -a $RESULTS_DIR/open_ports.txt

read -p "[?] Enter domain to lookup: " domain
dig +short $domain | tee $RESULTS_DIR/domain_lookup.txt
echo | tee -a $RESULTS_DIR/domain_lookup.txt

read -p "[?] Enter a domain for WHOIS lookup: " whois_domain
echo "[*] WHOIS info for $whois_domain: " | tee $RESULTS_DIR/whois.txt
whois $whois_domain | head -n 20 | tee -a $RESULTS_DIR/whois.txt
echo | tee -a $RESULTS_DIR/whois.txt

read -p "[?] Enter a domain for DNS lookup: " dns_domain
echo "[*] Resolving IP address for $dns_domain..." | tee $RESULTS_DIR/dns_lookup.txt
dig +short $dns_domain | tee -a $RESULTS_DIR/dns_lookup.txt
echo | tee -a $RESULTS_DIR/dns_lookup.txt

read -p "[?] Enter domain for subdomain enumeration: " enum_domain
echo "[*] Enumerating subdomains for $enum_domain using crt.sh..." | tee $RESULTS_DIR/subdomains.txt
curl -s "https://crt.sh/?q=%25.$enum_domain&output=json" |
	grep -oP '"name_value:"\K[^"]+' |
	sort -u | tee -a $RESULTS_DIR/subdomains.txt
echo | tee -a $RESULTS_DIR/subdomains.txt
