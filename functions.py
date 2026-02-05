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
    print(f"found duplicates {duplicates}")
    return duplicates
    
    

    



