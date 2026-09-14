# OSINT & Security Reconnaissance Toolkit

A curated reference list of essential tools, repositories, case studies, and resources categorized by operational discipline.

---

## 1. Reverse Image Search & Synthetic Media
Reverse lookup engines for tracking image reuse, verification, profile validation, and synthetic identity generation.

* **[Yandex Images](https://yandex.ru/images/search)**  
  Direct search endpoint for Yandex visual lookup. Known for precision in facial recognition and indexing across regional domains.
* **[Google Lens](https://lens.google/)**  
  Direct interface for Google visual object detection and image verification.
* **[Google Images](https://images.google.com)**  
  Traditional reverse image search interface powered by Google.
* **[This Person Does Not Exist](https://thispersondoesnotexist.com/)**  
  StyleGAN-based tool generating photorealistic, synthetic human profile portraits for persona generation and testing image attribution.

---

## 2. Google Dorking
Advanced search operators to discover misconfigurations, exposed sensitive files, and unindexed web pathways.

* **[Google Hacking Database (GHDB)](https://exploit-db.com/google-hacking-database)**  
  Curated repository on Exploit-DB containing categorized search strings for finding exposed systems, login portals, server vulnerabilities, and sensitive documents.

---

## 3. Dark Web & Breach Monitoring
Identify compromised credentials, leaked database snapshots, and credential-stuffing exposure.

* **[Have I Been Pwned](https://haveibeenpwned.com)**  
  Breach search utility and notification service documenting compromised email addresses, usernames, and passwords from public leaks and dark web databases.

---

## 4. Port Scanning & Service Discovery
Network socket exploration, port discovery, and service banner fingerprinting.

* **[Nmap](https://nmap.org)**  
  Standard network mapper and port scanner with full script engine (NSE) support. Available out-of-the-box in Kali Linux (`nmap`).
* **[RustScan (GitHub Repository)](https://github.com/bee-san/RustScan)**  
  Modern, asynchronous port scanner written in Rust capable of scanning 65,535 ports in seconds and feeding targets into Nmap.
* **[RustScan Usage & Guide (GeeksforGeeks)](https://www.geeksforgeeks.org/linux-unix/rustscan-faster-nmap-scanning-with-rust/)**  
  Practical guide covering RustScan installation, flags, and workflow integration with Nmap on Linux.

---

## 5. DNS Enumeration & Reconnaissance (Kali Linux Tools)
Identify infrastructure namespaces, resolve records, discover virtual hosts, and passively map target attack surfaces.

* **[dig (Domain Information Groper)](https://digwebinterface.com)**  
  Native Kali Linux command-line tool for DNS lookup and record extraction (A, AAAA, MX, TXT, CNAME, AXFR). Standalone source via [ISC BIND](https://www.isc.org/bind/).
* **[Whois](https://lookup.icann.org)**  
  CLI utility standard in Kali Linux for retrieving registrar data, registration dates, and nameservers.
* **[subfinder](https://github.com/projectdiscovery/subfinder)**  
  Passive subdomain discovery tool by ProjectDiscovery (packaged in Kali Linux) that aggregates passive online sources.
* **[ffuf (Fuzz Faster U Fool)](https://github.com/ffuf/ffuf)**  
  High-performance web and DNS fuzzer written in Go (standard in Kali Linux), commonly used for virtual host, subdomain, and content discovery.

---

## 6. Wordlist Generation
Generate targeted dictionaries and password permutations for penetration testing and brute-forcing.

* **[CeWL (Custom Word List generator)](https://github.com/digininja/CeWL)**  
  Native Kali Linux Ruby application (`cewl`) that crawls a target web application to extract unique vocabulary and jargon.
* **[crunch](https://sourceforge.net/projects/crunch-wordlist)**  
  Kali Linux tool (`crunch`) for generating custom wordlists based on specific character sets, lengths, and patterns.

---

## 7. Vulnerability Scanning
Automated signature detection, misconfiguration auditing, and CVE mapping.

* **[nuclei](https://github.com/projectdiscovery/nuclei)**  
  Declarative, YAML-template-based vulnerability scanner targeting web services, network protocols, and misconfigurations.
* **[OpenVAS / Greenbone Community Edition](https://www.greenbone.net/en/community-edition/)**  
  Comprehensive, open-source vulnerability scanner and manager. Official repository available on [GitHub](https://github.com/greenbone/openvas-scanner).

---

## 8. Geolocation & Open Source Investigation
Methodologies and case studies for locating real-world assets, verifying media, and tracking geographical movements.

* **[Bellingcat Investigation: Geolocating Venezuelan Lawmakers in Europe](https://www.bellingcat.com/news/2020/01/21/geolocating-venezuelan-lawmakers-in-europe/)**  
  Detailed OSINT case study demonstrating street-level geolocation techniques, landmark matching, architectural cross-referencing, and metadata analysis.
