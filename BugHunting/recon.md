Google Dorking :
site:*.target.com intext:"docs.google.com/spreadsheets"
site:*.target.com intext:"docs.google.com/drive"
site:*.target.com intext:"docs.google.com/presentation/d"
site:*.target.com intext:"Target 2026" ( copyright claim )
site:sub.target.com "admin" "login" "data" "user"
Kali Tools : 
paramspider
subfinder
nmap
xoxo
Shodan
https://web.archive.org
https://search.censys.io : In-depth analysis of certificates, identifying misconfigurations, finding related certificates and hosts.
https://crt.sh/: Quick and easy searches, identifying subdomains, checking certificate issuance history. : curl -s "https://crt.sh/?q=facebook.com&output=json" | jq -r '.[]
https://builtwith.com: Web technology profiler that provides detailed reports on a website's technology stack.
whatweb: Command-line tool for website fingerprinting.
nikto -h inlanefreight.com -Tuning b 
