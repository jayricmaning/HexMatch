markdown
# HexMatch 🔍

**HexMatch** is command-line utility for identifying and managing duplicate files. By utilizing 64-bit cryptographic hashing (**xxHash**), it ensures high data accuracy—detecting "identical twins" even if they have different filenames.

## ✨ Key Features
- **Data-First Matching:** Uses file content (Hex hashes), not just names, to find duplicates.
- **Safety First:** Option to move files to the native Trash/Recycle Bin so you can recover them if needed.
- **Command Line Ready:** Built with mutually exclusive flag groups to prevent conflicting actions.

## 🚀 Installation

Ensure you have Python 3.10+ installed. To install HexMatch globally on your system:

```bash
git clone https://github.com
cd hexmatch
pip install .
```
Use code with caution. To save on processing time, HexMatch is configured to only compare the initial 128KB of each file. While this provides near-instant results, there is a theoretical (though extremely low) risk of a false positive if two different files share identical headers. I recommend using the -r (--remove) over -d (--delete) option for important files. 

## 🛠 How to Use
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

## 📖 Command Options

| Flag | Long Name | Description |
| :--- | :--- | :--- |
| `-sc` | `--scan` | Scans the directory and displays found duplicates. |
| `-a` | `--all` | Targets **all** redundant copies found. |
| `-s` | `--select` | Targets specific files by index (e.g., `-s 1 4`). |
| `-r` | `--remove` | **Action:** Sends targeted files to the Trash/Recycle Bin. |
| `-d` | `--delete` | **Action:** Permanently deletes targeted files (caution!). |


## 🛡 License
Distributed under the MIT License. See LICENSE for more information.


