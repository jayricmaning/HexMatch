# HexMatch 🕵️‍♂️
HexMatch is a lightweight Python CLI tool designed to hunt down and eliminate duplicate files efficiently. It uses a smart hashing strategy (Head + Tail hashing) to quickly identify identical files without reading every single byte of large files.

## 🚀 Features

Fast Scanning: Uses xxhash for high-speed performance.
Smart Hashing: Checks file sizes first, then hashes only the first and last 64KB to verify identity.
Safe Deletion: Supports moving files to the Trash/Recycle Bin using send2trash or permanent deletion.
System Protection: Automatically skips sensitive system directories and common development folders (like .git and node_modules).


## 🛠️ Installation
Clone the repository:
```bash
git clone <repo>
cd HexMatch
pip install .
```

Install dependencies:
This tool requires xxhash for hashing and send2trash for safe file removal.

```bash
pip install .
```
*Make sure that you have installed python3 and github with file path added to environment variables in Windows

## 📖 How It Works
HexMatch follows a 3-step verification process to ensure accuracy and speed:
Walk: Scans your current working directory (and subdirectories), skipping system-critical folders.
Size Match: Groups files with identical sizes. If a file's size is unique, it's ignored immediately.
H3-Hashing: For files with matching sizes, it generates a hash based on the first 64KB and last 64KB. This detects duplicates (even in multi-GB videos) in milliseconds.

## 💻 Usage
Run the script from your terminal using various flags to control the behavior.
1. Scan for duplicates
To see what duplicates exist in your current folder:
```bash
python main.py --scan
```

2. Move ALL duplicates to Trash
If you want to clean up everything quickly and safely:
```bash
python main.py --all --remove
```

3. Permanently delete specific duplicates
If you ran a scan and saw that items #1 and #3 are junk:
```bash
python main.py --select 1 3 --delete
```
*This permanently deletes files. Use with caution!

## Argument Reference
Flag	Short	Description
--scan	-sc	Scans and lists duplicate groups found.
--all	-a	Targets all identified duplicates (excluding the original).
--select	-s	Manually choose which duplicates to target (e.g., -s 1 4 5).
--remove	-r	Action: Move targeted files to Trash/Recycle Bin.
--delete	-d	Action: Permanently delete targeted files.

## ⚠️ Disclaimer
Use with caution. While the tool includes a "skip list" for system directories, always ensure you have backups before performing permanent deletions (-d). The author is not responsible for accidental data loss.

## ⚖️ License

This project is licensed under the [MIT License](https://opensource.org). 