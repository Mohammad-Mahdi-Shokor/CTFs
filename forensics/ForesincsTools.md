The following commands and utilities are essential for digital forensics and steganography challenges in CTFs on Linux.

> **Note:** Many of these utilities do not come pre-installed. You can fetch most via `apt install <package>` or through GitHub/pip.

---

### Metadata & Carving

| Tool / Command | Common Use Case | Real-World Command Example |
| :--- | :--- | :--- |
| `exiftool` | Inspect EXIF metadata (author, GPS coordinates, hidden comments, timestamps) | `exiftool suspicious.jpg` |
| `binwalk -e` | Recursively scan and carve embedded files (firmware, appended archives) | `binwalk -e --matryoshka target.bin` |
| `unzip` | Unpack zip archives or list contents without extracting to disk | `unzip -l archive.zip` |
| `zipinfo` | Inspect zip headers, compression types, file permissions, and comments | `zipinfo -v archive.zip` |

---

### File Inspection & Byte Editing

| Tool / Command | Common Use Case | Real-World Command Example |
| :--- | :--- | :--- |
| `strings` | Extract ASCII/Unicode text; ideal for flags in binaries or uncompressed memory dumps | `strings -n 6 file.bin \| grep -i "flag{"` |
| `grep` | Filter output or search text patterns recursively across directories | `grep -rioE "CTF\{[^}]+\}" ./extracted_dir/` |
| `xxd` | Generate a hex dump of a file or inspect headers/footers | `xxd file.bin \| head -n 20` |
| `hexeditor` | View and edit magic bytes / file signatures directly via curses UI | `hexeditor corrupted_header.png` |
| `basenc` | Decode raw binary bitstreams (MSB/LSB) or alternative encodings | `echo "01100001" \| basenc -d --base2msbf` |

---

### Image Steganography

| Tool / Command | Common Use Case | Real-World Command Example |
| :--- | :--- | :--- |
| `steghide` | Extract password-protected payloads embedded in JPEG, BMP, WAV, or AU files | `steghide extract -sf stego.jpg -p "pass123"` |
| `stegseek` | High-speed dictionary cracker for `steghide` (cracks rockyou.txt in seconds) | `stegseek stego.jpg /usr/share/wordlists/rockyou.txt` |
| `zsteg` | Detect and extract LSB (Least Significant Bit) data from PNG and BMP files | `zsteg -a target.png` |
| `stegolsb` | Recover data hidden via specific LSB bit-plane depths/channels | `stegolsb steglsb -r -i secret.png -n 2 -o secret_output` |
| `stegosuite` | Steganography tool for image embedding/extracting with encryption | `stegosuite extract -k "password" file.jpg` |
| `stegsolve` | Java GUI tool to cycle through bit planes, color inversion, and image XOR | `java -jar bin/stegsolve.jar` |
| `eog` | Quickly display an image from the terminal | `eog flag.png &` |
| `zbarimg` | Decode QR codes, barcodes, and Datamatrix symbols from images | `zbarimg --raw qr_code.png` |

---

### Text & Network Forensics

| Tool / Command | Common Use Case | Real-World Command Example |
| :--- | :--- | :--- |
| `stegsnow` | Detect and unhide messages concealed using whitespace (tabs/spaces) at line endings | `stegsnow -p "1234" hidden.txt` *(omit `-p` if no password)* |
| `wireshark` | Analyze network traffic captures (`.pcap`/`.pcapng`), follow streams, and export objects | `wireshark capture.pcap &` |

---

### Disk & Filesystem Forensics (The Sleuth Kit)

| Tool / Command | Common Use Case | Real-World Command Example |
| :--- | :--- | :--- |
| `fls` | List deleted files and display their corresponding inode numbers | `fls -rd disk.img` |
| `icat` | Dump the raw contents of an inode directly into a recovered file | `icat disk.img 14285 > recovered_file.pdf` |

---

### Useful Websites

* [Digi-Cloak](https://kaushalmeena.github.io/digi-cloak/) — Browser-based tool for locking and unlocking payload data embedded in images.
* [CyberChef](https://gchq.github.io/CyberChef/) — All-in-one web app for chaining decoding, decompressing, and cipher routines.
* [Aperi’Solve](https://www.aperisolve.com/) — Automated online image analysis running `zsteg`, `steghide`, `exiftool`, and plane breakdown in parallel.
