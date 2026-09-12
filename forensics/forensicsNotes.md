Notes:

An IMG file is a raw disk image — it's a byte-for-byte copy of a storage device or partition.
A real hard drive or USB looks like this physically:
[sector 0][sector 1][sector 2]...[sector N]
An IMG file is just that exact same sequence of bytes saved as a file. Nothing is compressed or modified — it's a 1:1 clone.

Common extensions you'll see:
Extension Meaning
.img      Generic raw disk/partition image
.dd       Created with the dd tool (same thing)
.iso      CD/DVD image (also raw)
.vmdk     VMware virtual disk.
vhd       Windows virtual disk

They're all essentially the same idea — a file that represents a disk.




# Introduction to Digital Forensics and Reverse Engineering

## Digital Forensics

Digital forensics is the science of examining digital evidence to determine what happened during an incident.

Imagine that someone broke into a computer. How would you prove it? You would examine evidence such as:

- **Files and metadata:** When were the files created or modified? What software created them? Who accessed them?
- **Network traffic:** What data was transmitted, where was it sent, and which systems communicated?
- **Memory and logs:** Which processes were running? Which accounts logged in? What commands or actions were recorded?

### Why Is Digital Forensics Important?

Digital forensics helps investigators understand digital evidence and answer critical questions:

- **What happened?** Was there an intrusion, data leak, or unauthorized modification?
- **Who did it?** Can the actions be linked to a user, account, device, or system?
- **When did it happen?** Timelines are essential for reconstructing a sequence of events.
- **How did it happen?** Understanding the techniques used helps investigators close security gaps and prevent similar incidents.

---

## Metadata

Metadata is **data about data**. It consists of details embedded in, or stored alongside, files that describe when, how, and sometimes by whom they were created or modified.

Every time you create or edit a file, additional information may be saved with it.

### Key Information Found in Metadata

- Creation, modification, and access timestamps
- Author names, usernames, and computer names
- Software and software versions used to create or edit the file
- Device information
- Geolocation data, such as GPS coordinates

> **Note:** Metadata can be modified or removed, so it should not be treated as reliable proof on its own. Investigators should verify it using other evidence.

### Essential Utility: ExifTool

[ExifTool](https://exiftool.org/) is a command-line tool used to read, write, and edit metadata in many file formats, including JPG, PNG, PDF, DOCX, MP4, and MOV.

```bash
exiftool image.jpg
```

---

## Extracting Readable Strings

Strings are sequences of human-readable characters embedded in binary files. Extracting them is often a useful first step when quickly assessing a file's contents or possible purpose.

String extraction can reveal artifacts such as:

- Hardcoded credentials or API keys
- IP addresses or domain names used for network connections
- File paths or registry keys used by a program
- Commands, function names, and imported libraries
- Error messages that provide clues about the program's functionality

### Tools

Basic command-line tools include:

- `strings`: Extracts printable character sequences from a file
- `grep`: Searches extracted output for specific patterns
- `cat`: Displays the contents of text files

Example:

```bash
strings suspicious_file | grep -iE "password|key|http|flag"
```

Advanced analysis may require specialized tools such as:

- **FLOSS:** Extracts and decodes obfuscated strings from malware
- **PE-bear:** Inspects the structure of Windows Portable Executable files

---

## File Carving

### Extracting Embedded Files

In file analysis, carving can be used to extract objects embedded within another file—for example, an executable or archive hidden inside a document.

This technique searches binary data for recognizable file headers, footers, and structures, often called **file signatures** or **magic bytes**, to determine where an embedded file begins and ends.

### Tools

- **binwalk:** Automatically identifies and extracts many embedded files and data structures
- **xxd:** Creates a hexadecimal dump of a file for manual inspection

Examples:

```bash
binwalk suspicious_file
binwalk -e suspicious_file
xxd suspicious_file | less
```

### Whole-Disk File Recovery

When applied to a large data source, such as a disk image, file carving attempts to recover files whose filesystem metadata has been lost, damaged, or deleted. It searches the raw disk data for known file signatures instead of relying entirely on the filesystem's directory records.

File carving is an important technique for recovering deleted files, although recovered files may be incomplete or fragmented.

### Data-Wiping Tip

Deleting a file normally removes its filesystem reference but may leave recoverable data behind. Secure erasure may require device-appropriate methods such as full-disk encryption, an approved secure-erase command, cryptographic erasure, or verified wiping software.

> **Important:** Repeated overwriting is not always reliable for SSDs because of wear leveling and hidden storage areas. Follow the device manufacturer's secure-erasure guidance.

---

## Steganography in Practice

Steganography is the practice of hiding information inside another file, such as an image or audio file, so that the existence of the hidden data is not obvious.

### Common Tools

- **zsteg:** Detects and extracts data hidden in PNG and BMP images, especially data stored in bit planes
- **steghide:** Embeds or extracts data in supported image and audio formats; extraction may require a passphrase

Examples:

```bash
zsteg image.png
steghide extract -sf image.jpg
```

---

## Network Forensics

Network forensics involves capturing, recording, and analyzing network traffic, often stored in packet-capture files such as `.pcap` or `.pcapng` files.

Analyzing network traffic can reveal:

- Cleartext credentials transmitted over insecure protocols
- Files transferred through protocols such as HTTP, FTP, or SMB
- Suspicious connections to external IP addresses or domains
- Command-and-control (C2) traffic associated with malware
- Evidence of scanning, exploitation attempts, or data exfiltration

### Key Tools

- **Wireshark:** A widely used tool for packet inspection, filtering, protocol analysis, and stream reconstruction
- **NetworkMiner:** Extracts artifacts such as files, images, messages, hosts, and credentials from supported network captures

> **Legal and ethical note:** Only capture or inspect network traffic when you have authorization to do so.

---

## From Digital Forensics to Reverse Engineering

| Field | Main Purpose |
| --- | --- |
| **Digital forensics** | Investigating incidents and reconstructing events using digital evidence |
| **Reverse engineering** | Understanding how software works by analyzing its structure and behavior |

These areas often overlap. During a malware investigation, for example, forensic analysis may identify a suspicious executable, while reverse engineering helps determine exactly what that executable does.

---

## Introduction to Reverse Engineering

Reverse engineering is the process of analyzing software to understand its functionality, design, and implementation without relying on its original source code.

In cybersecurity, it is commonly used for:

- Malware analysis
- Vulnerability research
- Understanding undocumented file formats or protocols
- Analyzing suspicious program behavior

### Static Analysis

Static analysis examines a program **without executing it**. Analysts use tools such as disassemblers and decompilers to study the program's structure and reconstruct its logic.

#### Key Goals

- Identify the program's entry point
- Map control flow, including branches, loops, and function calls
- Identify imported functions and API calls
- Search for hardcoded domains, IP addresses, file paths, strings, or cryptographic constants
- Detect suspicious functionality or obfuscation

#### Primary Tools

- **Ghidra:** A free and open-source reverse-engineering framework with disassembly and decompilation features
- **IDA:** A widely used disassembler and debugger; some editions include decompilation support

> A decompiler produces a high-level approximation of the original source code. It usually cannot restore the exact original variable names, comments, or program structure.

### Dynamic Analysis

Dynamic analysis observes a program **while it is running**, usually inside a controlled environment such as a virtual machine or sandbox.

It can reveal:

- Files created, modified, or deleted
- Registry changes
- Processes and child processes
- Network connections
- Memory activity
- Runtime-decrypted strings or configuration data

> **Safety note:** Suspicious software should only be executed in an isolated, controlled environment designed for malware analysis.

---

## Android Application Analysis

Android application packages (`.apk` files) are ZIP-based archives that commonly contain:

- `AndroidManifest.xml`: Declares application components, permissions, and configuration
- `classes.dex`: Contains compiled Dalvik bytecode
- `res/`: Contains application resources
- `assets/`: Contains bundled application assets
- `lib/`: May contain native libraries for different processor architectures
- `META-INF/`: Contains signing-related metadata in many APK formats

Security analysis often involves decompiling or disassembling an APK to inspect its code, permissions, components, resources, and network behavior.

### Common Tools

- **JADX-GUI:** Converts Dalvik bytecode into readable Java-like source code and provides a graphical interface for browsing the application
- **Android Studio:** Can inspect APK contents, debug applications, analyze resources, and monitor application behavior

> Decompilation does not reproduce the exact original source code. Names and logic may also be difficult to understand when the application has been obfuscated.

---

## Quick Tool Reference

| Task | Tool |
| --- | --- |
| Inspect file metadata | ExifTool |
| Extract readable strings | `strings`, FLOSS |
| Search extracted text | `grep` |
| View file bytes in hexadecimal | `xxd` |
| Detect or extract embedded files | binwalk |
| Analyze image steganography | zsteg, steghide |
| Analyze packet captures | Wireshark, NetworkMiner |
| Analyze native executables statically | Ghidra, IDA, PE-bear |
| Decompile Android APKs | JADX-GUI |
| Inspect and debug Android applications | Android Studio |
