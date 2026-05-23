
### Digging DNS:
dig	Versatile DNS lookup tool that supports various query types (A, MX, NS, TXT, etc.) and detailed output.	Manual DNS queries, zone transfers (if allowed), troubleshooting DNS issues, and in-depth analysis of DNS records.
nslookup	Simpler DNS lookup tool, primarily for A, AAAA, and MX records.	Basic DNS queries, quick checks of domain resolution and mail server records.
host	Streamlined DNS lookup tool with concise output.	Quick checks of A, AAAA, and MX records.
dnsenum	Automated DNS enumeration tool, dictionary attacks, brute-forcing, zone transfers (if allowed).	Discovering subdomains and gathering DNS information efficiently.
fierce	DNS reconnaissance and subdomain enumeration tool with recursive search and wildcard detection.	User-friendly interface for DNS reconnaissance, identifying subdomains and potential targets.
dnsrecon	Combines multiple DNS reconnaissance techniques and supports various output formats.	Comprehensive DNS enumeration, identifying subdomains, and gathering DNS records for further analysis.
theHarvester	OSINT tool that gathers information from various sources, including DNS records (email addresses).	Collecting email addresses, employee information, and other data associated with a domain from multiple sources.
Online DNS Lookup Services	User-friendly interfaces for performing DNS lookups.	Quick and easy DNS lookups, convenient when command-line tools are not available, checking for domain availability or basic information




### DNS BruteForcing:

dnsenum	Comprehensive DNS enumeration tool that supports dictionary and brute-force attacks for discovering subdomains.
fierce	User-friendly tool for recursive subdomain discovery, featuring wildcard detection and an easy-to-use interface.
dnsrecon	Versatile tool that combines multiple DNS reconnaissance techniques and offers customisable output formats.
amass	Actively maintained tool focused on subdomain discovery, known for its integration with other tools and extensive data sources.
assetfinder	Simple yet effective tool for finding subdomains using various techniques, ideal for quick and lightweight scans.
puredns	Powerful and flexible DNS brute-forcing tool, capable of resolving and filtering results effectively.



### Virtual Hosts Discovery Tools:
Tool	Description	Features
gobuster	A multi-purpose tool often used for directory/file brute-forcing, but also effective for virtual host discovery.	Fast, supports multiple HTTP methods, can use custom wordlists.
Feroxbuster	Similar to Gobuster, but with a Rust-based implementation, known for its speed and flexibility.	Supports recursion, wildcard discovery, and various filters.
ffuf	Another fast web fuzzer that can be used for virtual host discovery by fuzzing the Host header.	Customizable wordlist input and filtering options.


### Certificate Transperancy Logs:
Tool	Key Features	Use Cases	Pros	Cons
crt.sh	User-friendly web interface, simple search by domain, displays certificate details, SAN entries.	Quick and easy searches, identifying subdomains, checking certificate issuance history.	Free, easy to use, no registration required.	Limited filtering and analysis options.
Censys	Powerful search engine for internet-connected devices, advanced filtering by domain, IP, certificate attributes.	In-depth analysis of certificates, identifying misconfigurations, finding related certificates and hosts.	Extensive data and filtering options, API access.	Requires registration (free tier available).



### Fingerprinting:

Tool	Description	Features
Wappalyzer	Browser extension and online service for website technology profiling.	Identifies a wide range of web technologies, including CMSs, frameworks, analytics tools, and more.
BuiltWith	Web technology profiler that provides detailed reports on a website's technology stack.	Offers both free and paid plans with varying levels of detail.
WhatWeb	Command-line tool for website fingerprinting.	Uses a vast database of signatures to identify various web technologies.
Nmap	Versatile network scanner that can be used for various reconnaissance tasks, including service and OS fingerprinting.	Can be used with scripts (NSE) to perform more specialised fingerprinting.
Netcraft	Offers a range of web security services, including website fingerprinting and security reporting.	Provides detailed reports on a website's technology, hosting provider, and security posture.
wafw00f	Command-line tool specifically designed for identifying Web Application Firewalls (WAFs).	Helps determine if a WAF is present and, if so, its type and configuration.

https://github.com/EnableSecurity/wafw00f
https://github.com/sullo/nikto

### robots.txt:
Directive	Description	Example
Disallow	Specifies paths or patterns that the bot should not crawl.	Disallow: /admin/ (disallow access to the admin directory)
Allow	Explicitly permits the bot to crawl specific paths or patterns, even if they fall under a broader Disallow rule.	Allow: /public/ (allow access to the public directory)
Crawl-delay	Sets a delay (in seconds) between successive requests from the bot to avoid overloading the server.	Crawl-delay: 10 (10-second delay between requests)
Sitemap	Provides the URL to an XML sitemap for more efficient crawling.	Sitemap: https://www.example.com/sitemap.xml


### Well-Known URIs

security.txt	Contains contact information for security researchers to report vulnerabilities.	Permanent	RFC 9116
/.well-known/change-password	Provides a standard URL for directing users to a password change page.	Provisional	https://w3c.github.io/webappsec-change-password-url/#the-change-password-well-known-uri
openid-configuration	Defines configuration details for OpenID Connect, an identity layer on top of the OAuth 2.0 protocol.	Permanent	http://openid.net/specs/openid-connect-discovery-1_0.html
assetlinks.json	Used for verifying ownership of digital assets (e.g., apps) associated with a domain.	Permanent	https://github.com/google/digitalassetlinks/blob/master/well-known/specification.md
mta-sts.txt	Specifies the policy for SMTP MTA Strict Transport Security (MTA-STS) to enhance email security.	Permanent	RFC 8461

### Crawlers:
Popular Web Crawlers

    Burp Suite Spider: Burp Suite, a widely used web application testing platform, includes a powerful active crawler called Spider. Spider excels at mapping out web applications, identifying hidden content, and uncovering potential vulnerabilities.
    OWASP ZAP (Zed Attack Proxy): ZAP is a free, open-source web application security scanner. It can be used in automated and manual modes and includes a spider component to crawl web applications and identify potential vulnerabilities.
    Scrapy (Python Framework): Scrapy is a versatile and scalable Python framework for building custom web crawlers. It provides rich features for extracting structured data from websites, handling complex crawling scenarios, and automating data processing. Its flexibility makes it ideal for tailored reconnaissance tasks.
    Apache Nutch (Scalable Crawler): Nutch is a highly extensible and scalable open-source web crawler written in Java. It's designed to handle massive crawls across the entire web or focus on specific domains. While it requires more technical expertise to set up and configure, its power and flexibility make it a valuable asset for large-scale reconnaissance projects.

    Scrapy 
    ReconSpider https://academy.hackthebox.com/storage/modules/144/ReconSpider.v1.2.zip
      JSON Key	Description
emails	Lists email addresses found on the domain.
links	Lists URLs of links found within the domain.
external_files	Lists URLs of external files such as PDFs.
js_files	Lists URLs of JavaScript files used by the website.
form_fields	Lists form fields found on the domain (empty in this example).
images	Lists URLs of images found on the domain.
videos	Lists URLs of videos found on the domain (empty in this example).
audio	Lists URLs of audio files found on the domain (empty in this example).
comments	Lists HTML comments found in the source code.




### Search Engine: 
Operator	Operator Description	Example	Example Description
site:	Limits results to a specific website or domain.	site:example.com	Find all publicly accessible pages on example.com.
inurl:	Finds pages with a specific term in the URL.	inurl:login	Search for login pages on any website.
filetype:	Searches for files of a particular type.	filetype:pdf	Find downloadable PDF documents.
intitle:	Finds pages with a specific term in the title.	intitle:"confidential report"	Look for documents titled "confidential report" or similar variations.
intext: or inbody:	Searches for a term within the body text of pages.	intext:"password reset"	Identify webpages containing the term “password reset”.
cache:	Displays the cached version of a webpage (if available).	cache:example.com	View the cached version of example.com to see its previous content.
link:	Finds pages that link to a specific webpage.	link:example.com	Identify websites linking to example.com.
related:	Finds websites related to a specific webpage.	related:example.com	Discover websites similar to example.com.
info:	Provides a summary of information about a webpage.	info:example.com	Get basic details about example.com, such as its title and description.
define:	Provides definitions of a word or phrase.	define:phishing	Get a definition of "phishing" from various sources.
numrange:	Searches for numbers within a specific range.	site:example.com numrange:1000-2000	Find pages on example.com containing numbers between 1000 and 2000.
allintext:	Finds pages containing all specified words in the body text.	allintext:admin password reset	Search for pages containing both "admin" and "password reset" in the body text.
allinurl:	Finds pages containing all specified words in the URL.	allinurl:admin panel	Look for pages with "admin" and "panel" in the URL.
allintitle:	Finds pages containing all specified words in the title.	allintitle:confidential report 2023	Search for pages with "confidential," "report," and "2023" in the title.
AND	Narrows results by requiring all terms to be present.	site:example.com AND (inurl:admin OR inurl:login)	Find admin or login pages specifically on example.com.
OR	Broadens results by including pages with any of the terms.	"linux" OR "ubuntu" OR "debian"	Search for webpages mentioning Linux, Ubuntu, or Debian.
NOT	Excludes results containing the specified term.	site:bank.com NOT inurl:login	Find pages on bank.com excluding login pages.
* (wildcard)	Represents any character or word.	site:socialnetwork.com filetype:pdf user* manual	Search for user manuals (user guide, user handbook) in PDF format on socialnetwork.com.
.. (range search)	Finds results within a specified numerical range.	site:ecommerce.com "price" 100..500	Look for products priced between 100 and 500 on an e-commerce website.
" " (quotation marks)	Searches for exact phrases.	"information security policy"	Find documents mentioning the exact phrase "information security policy".
- (minus sign)	Excludes terms from the search results.	site:news.com -inurl:sports	Search for news articles on news.com excluding sports-related content.

Google Dorking
https://www.exploit-db.com/google-hacking-database
Finding Login Pages:

    site:example.com inurl:login
    site:example.com (inurl:login OR inurl:admin)

Identifying Exposed Files:

    site:example.com filetype:pdf
    site:example.com (filetype:xls OR filetype:docx)

Uncovering Configuration Files:

    site:example.com inurl:config.php
    site:example.com (ext:conf OR ext:cnf) (searches for extensions commonly used for configuration files)

Locating Database Backups:

    site:example.com inurl:backup
    site:example.com filetype:sql

### Web Archives:

https://web.archive.org/

### Automation Recon:

https://github.com/thewhiteh4t/FinalRecon :  A Python-based reconnaissance tool offering a range of modules for different tasks like SSL certificate checking, Whois information gathering, header analysis, and crawling. Its modular structure enables easy customisation for specific needs.

Option	Argument	Description
-h, --help		Show the help message and exit.
--url	URL	Specify the target URL.
--headers		Retrieve header information for the target URL.
--sslinfo		Get SSL certificate information for the target URL.
--whois		Perform a Whois lookup for the target domain.
--crawl		Crawl the target website.
--dns		Perform DNS enumeration on the target domain.
--sub		Enumerate subdomains for the target domain.
--dir		Search for directories on the target website.
--wayback		Retrieve Wayback URLs for the target.
--ps		Perform a fast port scan on the target.
--full		Perform a full reconnaissance scan on the target.

https://github.com/lanmaster53/recon-ng :  A powerful framework written in Python that offers a modular structure with various modules for different reconnaissance tasks. It can perform DNS enumeration, subdomain discovery, port scanning, web crawling, and even exploit known vulnerabilities.

https://github.com/laramies/theHarvester :  Specifically designed for gathering email addresses, subdomains, hosts, employee names, open ports, and banners from different public sources like search engines, PGP key servers, and the SHODAN database. It is a command-line tool written in Python.

https://github.com/smicallef/spiderfoot : An open-source intelligence automation tool that integrates with various data sources to collect information about a target, including IP addresses, domain names, email addresses, and social media profiles. It can perform DNS lookups, web crawling, port scanning, and more.

https://osintframework.com/ : A collection of various tools and resources for open-source intelligence gathering. It covers a wide range of information sources, including social media, search engines, public records, and more.


