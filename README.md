
# HexMatch 

HexMatch is a lightweight Python CLI tool designed to hunt down and eliminate duplicate files efficiently. It uses a smart hashing strategy (Head + Tail hashing) to quickly identify identical files without reading every single byte of large files. Works on Windows and Linux. 

## Key Features
- **Fast Scanning:** Uses xxhash for high-speed performance. Checks file sizes first, then hashes only the first and last 64KB to verify identity
- **Safe Deletion:** Option to move files to the native Trash/Recycle Bin so you can recover them if needed.
- **System Protection:** Provides a "config.txt" file users can add directories to skip. This automatically skips sensitive system directories and common development folders (like .git and node_modules).
- **Command Line Ready:** Simple CLI commands for quick and convinient use. Check below for "Command Options"


## Installation

Ensure you have Python 3.10+ and git installed. To install HexMatch globally on your system:

```bash
git clone https://github.com/jayricmaning/HexMatch.git
cd hexmatch
pip install .
```
To save on processing time, HexMatch is configured to only compare the initial 128KB of each file. While this provides near-instant results, there is a theoretical (though extremely low) risk of a false positive if two different files share identical headers. I recommend using the -r (--remove) over -d (--delete) option for important files. 

## How to Use
HexMatch uses a Selection + Action logic. You must pick what to target and how to handle it.

### 1. Scan and Review
See exactly what duplicates exist before taking action.
```bash
hexmatch --scan
```

### 2. Move All to Trash
The safest way to clean your drive. Moves every redundant copy to the Recycle Bin.
```bash
hexmatch --all --remove
```

### 3. Selective Permanent Deletion 
Target specific files (by the numbers shown in --scan) for immediate, permanent removal.
```bash
hexmatch --select 1 3 5 --delete
```

## Command Options

| Flag | Long Name | Description |
| :--- | :--- | :--- |
| `-sc` | `--scan` | Scans the directory and displays found duplicates. |
| `-a` | `--all` | Targets **all** redundant copies found. |
| `-s` | `--select` | Targets specific files by index (e.g., `-s 1 4`). |
| `-r` | `--remove` | **Action:** Sends targeted files to the Trash/Recycle Bin. |
| `-d` | `--delete` | **Action:** Permanently deletes targeted files (caution!). |


## 🛡 License
Distributed under the MIT License. See LICENSE for more information.
