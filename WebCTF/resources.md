# Web Application Security & Pentesting Toolkit

A curated reference list of learning paths, exploitation cheat sheets, testing guides, and prevention frameworks focusing on SQL Injection and Business Logic vulnerabilities.

---

## 1. SQL Injection (SQLi)

### Fundamentals & Technical Guides
* **[GeeksforGeeks: SQL Injection (SQLi)](https://www.geeksforgeeks.org/sql-injection/)**  
  Foundational tutorial explaining SQL injection mechanics, error-based, union-based, and blind vectors, alongside standard code remediation.
* **[GeeksforGeeks: MySQL SQL Injection](https://www.geeksforgeeks.org/mysql/mysql-sql-injection/)**  
  Technical breakdown of database-specific attack surfaces, blind boolean/time delays, and out-of-band exfiltration on MySQL systems.

### Practice Labs & Structured Learning
* **[PortSwigger Web Security Academy: SQL Injection Learning Path & Labs](https://portswigger.net/web-security/learning-paths/sql-injection)**  
  Hands-on interactive lab environment covering UNION attacks, hidden data retrieval, blind conditional responses, and error-based data extraction.
* **[PortSwigger SQL Injection Main Reference & Cheat Sheet](https://portswigger.net/web-security/sql-injection)**  
  Theoretical overview covering syntax discrepancies across Oracle, Microsoft SQL Server, PostgreSQL, and MySQL.

### Defensive Engineering & Cheat Sheets
* **[OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)**  
  Industry standard for secure development practices, detailing parameterized queries (prepared statements), stored procedure safety, and allow-list input validation.
* **[PentestMonkey SQL Injection Cheat Sheets](https://pentestmonkey.net/category/cheat-sheet/sql-injection)**  
  Renowned quick-reference compilation providing syntax tables for privilege escalation, schema dumping, time delays, and out-of-band queries across backends:
  * [MySQL SQL Injection Cheat Sheet](https://pentestmonkey.net/cheat-sheet/sql-injection/mysql-sql-injection-cheat-sheet)
  * [PostgreSQL SQL Injection Cheat Sheet](https://pentestmonkey.net/cheat-sheet/sql-injection/postgres-sql-injection-cheat-sheet)
  * [MSSQL SQL Injection Cheat Sheet](https://pentestmonkey.net/cheat-sheet/sql-injection/mssql-sql-injection-cheat-sheet)
  * [Oracle SQL Injection Cheat Sheet](https://pentestmonkey.net/cheat-sheet/sql-injection/oracle-sql-injection-cheat-sheet)

---

## 2. Business Logic Vulnerabilities

### Interactive Labs & Attack Vectors
* **[PortSwigger Web Security Academy: Business Logic Vulnerabilities](https://portswigger.net/web-security/logic-flaws)**  
  Core modules detailing how flawed assumptions in design lead to client-side control abuse, broken workflow state machines, and authentication bypasses.
* **[PortSwigger Business Logic Labs & Examples](https://portswigger.net/web-security/logic-flaws/examples)**  
  Targeted challenges covering excessive trust in client parameters, multi-step transaction circumvention, and race conditions.

### Methodology & Testing Frameworks
* **[OWASP Web Security Testing Guide (WSTG) - Business Logic Testing](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/)**  
  Standardized methodology (Category 4.10: `WSTG-BUSL`) for auditing application workflow integrity:
  * **WSTG-BUSL-01:** Test Business Logic Data Validation
  * **WSTG-BUSL-02:** Test Ability to Forge Requests
  * **WSTG-BUSL-03:** Test Integrity Checks
  * **WSTG-BUSL-04:** Test for Process Timing
  * **WSTG-BUSL-05:** Test Number of Times a Function Can Be Used (Limits)
  * **WSTG-BUSL-06:** Test for the Circumvention of Workflows
  * **WSTG-BUSL-07:** Test Defenses Against Application Misuse
  * **WSTG-BUSL-08:** Test Upload of Unexpected File Types
  * **WSTG-BUSL-09:** Test Upload of Malicious Files
* **[OWASP Business Logic Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Business_Logic_Security_Cheat_Sheet.html)**  
  Architectural patterns for enforcing state machines on the server, preventing concurrency flaws, and establishing atomic transaction boundaries.
