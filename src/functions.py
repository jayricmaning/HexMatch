import os
import xxhash 
from send2trash import send2trash
from collections import defaultdict

def compare_file_size(file_paths):
    size_map = defaultdict(list)
    for path in file_paths:
        try: 
            size = os.path.getsize(path)
            size_map[size].append(path)
        except (OSError, PermissionError):
            continue

    return {size: paths for size, paths in size_map.items() if len(paths) > 1}

def hash_generator(size_map):
    hashes_to_files = defaultdict(list)
    for path_list in size_map.values():
        for path in path_list:
            h = xxhash.xxh3_64()
            try:         
                with open(path, 'rb') as f:
                    # 131072 (128KB) is the buffer size for efficient sequential disk reads
                    while chunk := f.read(131072):
                        h.update(chunk)
                file_hash = h.hexdigest()
                hashes_to_files[file_hash].append(path)

            except (OSError, PermissionError) as e:
                print(f"Skipping {os.path.basename(path)}: {e}")

    return {h: paths for h, paths in hashes_to_files.items() if len(paths) > 1}
    
def walk_dir():
    target_path = os.getcwd()
    hash_map = defaultdict(list)
    dupe_counter = 0
    skip_list = {
        'Windows', '$Recycle.Bin', 'System Volume Information', 'ProgramData', 'Program Files', 'Program Files (x86)', 'System',
         'Riot Games', 'XboxGames', '.git', 'node_modules', '__pycache__', '.vscode'       
    }

    for root, dirs, files in os.walk(target_path): 
        dirs[:] = [d for d in dirs if d not in skip_list and not d.startswith('.')]
        for f in files:
            if ":" in f:
                continue
            file_paths = os.path.join(root, f)
            file_hash = hash_generator(file_paths)

            if file_hash:
                if file_hash in hash_map:
                    dupe_counter += 1
                    original_path = hash_map[file_hash][0]
                    print(f"[{dupe_counter}] Twin Found!")
                    print(f"    New: {f}")
                    print(f"    Original: {os.path.basename(original_path)}")
                hash_map[file_hash].append(file_paths)
            
    return hash_map

def find_duplicate(hash_map):
    duplicates = {}
    for file_hash, paths in hash_map.items():
        if len(paths) > 1:
            duplicates[file_hash] = paths
    return duplicates
    

def display_duplicates(duplicates):
    number = 0
    for value in duplicates.values():
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