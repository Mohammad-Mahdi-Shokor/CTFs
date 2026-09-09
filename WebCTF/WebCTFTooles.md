The following tools are core utilities for web application CTF challenges, reconnaissance, and traffic analysis.

> **Note:** Most of these tools come pre-installed on Kali/Parrot, or can be installed via `apt`, `go install`, or Python's `pipx`.

---

### Interception & Proxying

| Tool / Command | Common Use Case | Real-World Command Example |
| :--- | :--- | :--- |
| `burpsuite` | Intercept, modify, and replay HTTP/S requests; tamper with tokens, parameters, and headers via Proxy and Repeater | `burpsuite &` *(configure browser proxy to `127.0.0.1:8080`)* |

---

### Reconnaissance & Surface Mapping

| Tool / Command | Common Use Case | Real-World Command Example |
| :--- | :--- | :--- |
| `subfinder` | Passive subdomain discovery using OSINT sources without touching the target domain directly | `subfinder -d example.com -o subdomains.txt` |
| `nmap` | Host discovery, open port detection, and identifying running service versions / banners | `nmap -sC -sV -p- target.thm -oN scan.txt` |
| `paramspider` | Mine web archives (Wayback Machine) to mine parameter-heavy endpoints for injection testing | `paramspider -d example.com --level high` |

---

### Scanning & Vulnerability Detection

| Tool / Command | Common Use Case | Real-World Command Example |
| :--- | :--- | :--- |
| `nuclei` | Fast, template-based scanner to detect CVEs, misconfigurations, and exposed panels across hosts | `nuclei -u https://example.com -t cves/ -severity medium,high,critical` |

---

### Network Inspection & Low-Level Interaction

| Tool / Command | Common Use Case | Real-World Command Example |
| :--- | :--- | :--- |
| `wireshark` | Deep packet inspection for raw PCAP captures; inspect unencrypted HTTP streams or extract downloaded files | `wireshark capture.pcap &` |
| `telnet` | Establish raw TCP sessions to manually banner-grab, test mail/HTTP daemons, or interact with text-based challenge ports | `telnet 10.10.10.10 80` *(send raw `GET / HTTP/1.1` request)* |

---

### Handy Complementary Web Tools

* `ffuf` / `gobuster` — Fast directory and parameter fuzzing for uncovering unlinked routes.
* `curl -i` / `httpie` — Rapid CLI-based request testing and header inspection without spinning up a GUI proxy.
* `jwt_tool` — Tampering, testing invalid signature algorithms, and cracking JSON Web Tokens.
