# OSINT & Security Reconnaissance Toolkit

A curated reference list of essential tools, repositories, and direct links categorized by operational discipline.

---

## 1. Reverse Image Search
Used to verify profiles, uncover mirrored assets, track stolen imagery, and correlate real-world infrastructure.

* **[Yandex Images](https://yandex.com/images)**  
  Known for facial recognition precision and tracking images across international and regional hosts.
* **[Google Images / Lens](https://images.google.com)**  
  Broad web indexing and visual object search powered by Google Lens.

---

## 2. Google Dorking
Advanced search operators used to discover sensitive file disclosures, exposed credentials, configuration backups, and unindexed web paths.

* **[Google Hacking Database (GHDB)](https://exploit-db.com/google-hacking-database)**  
  Curated repository on Exploit-DB containing categorized search strings for finding exposed systems, login portals, server vulnerabilities, and sensitive documents.

---

## 3. Dark Web & Breach Monitoring
Identify compromised credentials, leaked database snapshots, and credential-stuffing exposure across black-market collections.

* **[Have I Been Pwned](https://haveibeenpwned.com)**  
  Breach search utility and notification engine documenting compromised email addresses, usernames, and hashed passwords from commercial leaks and underground dumps.

---

## 4. Port Scanning & Service Discovery
Host discovery, open socket auditing, and daemon banner fingerprinting across external perimeter targets.

* **[Nmap](https://nmap.org)**  
  The de facto network exploration tool and security scanner. Supports NSE scripting, OS fingerprinting, and service identification.
* **[RustScan](https://github.com/RustScan/RustScan)**  
  Extremely fast, asynchronous port scanner written in Rust designed to scan 65,535 ports in seconds and feed findings directly to Nmap for deep service analysis.

---

## 5. DNS Enumeration & Reconnaissance
Identify asset namespaces, resolve nameservers, find virtual hosts, and passively map target attack surfaces.

* **[dig (Domain Information Groper)](https://digwebinterface.com)**  
  Standard DNS investigation utility for querying specific record types (A, AAAA, MX, TXT, CNAME, SOA, AXFR). Standalone source available via [ISC BIND](https://www.isc.org/bind/).
* **[Whois](https://lookup.icann.org)**  
  Domain registry query tool for pulling registrar records, creation dates, nameservers, and administrative contacts. CLI native or ICANN lookup.
* **[subfinder](https://github.com/projectdiscovery/subfinder)**  
  Passive subdomain discovery utility by ProjectDiscovery that aggregates passive online sources to discover valid subdomains quickly without touching the target.
* **[ffuf (Fuzz Faster U Fool)](https://github.com/ffuf/ffuf)**  
  High-performance HTTP fuzzer written in Go, useful for subdomain discovery, virtual host identification, and directory/parameter brute-forcing.

---

## 6. Wordlist Generation
Produce targeted dictionaries and permutations based on client profiling, brand keywords, or syntax constraints.

* **[CeWL (Custom Word List generator)](https://github.com/digininja/CeWL)**  
  Command-line Ruby application that spiders a target domain to extract unique words, industry jargon, and internal terminology for custom password/directory lists.
* **[crunch](https://sourceforge.net/projects/crunch-wordlist)**  
  Flexible utility that generates custom wordlists based on defined character sets, lengths, and regex-like pattern structures.

---

## 7. Vulnerability Scanning
Automated signature detection, misconfiguration auditing, and CVE mapping across networks and applications.

* **[nuclei](https://github.com/projectdiscovery/nuclei)**  
  Fast, community-driven vulnerability scanner utilizing declarative YAML templates for automated checks across HTTP, DNS, TCP, SSL, and Websocket protocols.
* **[OpenVAS / Greenbone Community Edition](https://www.greenbone.net/en/community-edition/)**  
  Enterprise-grade, open-source vulnerability scanner capable of running thousands of Network Vulnerability Tests (NVTs) across complex network infrastructure. Official repository on [GitHub](https://github.com/greenbone/openvas-scanner).
