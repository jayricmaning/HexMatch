import os
import xxhash
from send2trash import send2trash
from collections import defaultdict

def hash_generator(file_path):
    h = xxhash.xxh3_64()

    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(131072):
                h.update(chunk)
        return h.hexdigest()
    except (PermissionError, EOFError):
        return None
    
def walk_dir():
    target_path = os.getcwd()
    hash_map = defaultdict(list)
    dupe_counter = 0
    skip_list = {
        'Windows', '$Recycle.Bin', 'System Volume Information', #skip these directories
        '.git', 'node_modules', '__pycache__', '.vscode'       
    }

    for root, dirs, files in os.walk(target_path): 
        dirs[:] = [d for d in dirs if d not in skip_list and not d.startswith('.')]
        counter = 0
        for f in files:
            if ":" in f:
                continue
            file_path = os.path.join(root, f)
            file_hash = hash_generator(file_path)

            if file_hash:
                if file_hash in hash_map:
                    dupe_counter += 1
                    original_path = hash_map[file_hash][0]
                    print(f"[{dupe_counter}] Twin Found!")
                    print(f"    New: {f}")
                    print(f"    Original: {os.path.basename(original_path)}")
                hash_map[file_hash].append(file_path)
            
    return hash_map

def find_duplicate(hash_map):
    duplicates = {}
    for file_hash, paths in hash_map.items():
        if len(paths) > 1:
            duplicates[file_hash] = paths
    return duplicates
    

def display_duplicates(duplicates):
    number = 0
    for key,value in duplicates.items():
        file_name = []
        number += 1
        for item in value:
            file_name.append(os.path.basename(item))   
 #           split_item = item.split('/')
 #           file_name.append(split_item[-1])    
        print(f"  {number}. {file_name[0]} ({len(file_name)} duplicates)")
    return duplicates


def grab_duplicates(duplicates):
    #return a list of copies of a file exept the original file
    duplicate_files = []
    for key,value in duplicates.items():
        for path in value[1:]:
            duplicate_files.append(path)
#       print(duplicate_files)
    return duplicate_files


def select_duplicates(duplicate_files, selected_item):
    #return a list of selected items from the duplicate_files list
    selected = []
    for number in selected_item:
        index = number - 1
        if 0 <= index < len(duplicate_files):
            selected.append(duplicate_files[index])
        else:    
            print(f"Skipping {number}: no such file exists!")
    return selected

def trash_duplicates(selected=[]):
    try:
        for file in selected:
            send2trash(file)
            print(f"Sucessfully moved to trash: {file}")
    except Exception as e:
        print(f"Could not delete {file}. Error: {e}")

def delete_duplicates(selected_files):
    for file in selected_files:
        try:
            os.remove(file)
            print(f"Permanently Deleted: {os.path.basename(file)}")

        except (PermissionError, OSError) as e:
            print(f"Skip: Could not delete {os.path.basename(file)}. (Error: {e})")