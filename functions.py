import os
import xxhash
from collections import defaultdict

def hash_generator(file_path):
    h = xxhash.xxh3_64()

    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(131072):
                h.update(chunk)
        return h.hexdigest()
    except EOFError:
        return None
    
def walk_dir():
    target_path = os.getcwd()
    hash_map = defaultdict(list)
    for root, dirs, files in os.walk(target_path): 
        for file in files:
            if ":" in file:
                continue
            file_path = os.path.join(root, file)
            file_hash = hash_generator(file_path)

            if file_hash:
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
    duplicate_files = []
    for key,value in duplicates.items():
        for path in value[1:]:
            duplicate_files.append(path)
#       print(duplicate_files)
    return duplicate_files


def select_duplicates(duplicate_files, selection):
    selected = []
    for item in range(0, len(selection)):
        selected.append(duplicate_files[selection+1])
