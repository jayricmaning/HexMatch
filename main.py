import os
import argparse
from .functions import (walk_dir, 
                       find_duplicate, 
                       display_duplicates, 
                       grab_duplicates,
                       select_duplicates,
                       delete_duplicates)

def main():
    print("Starting Twin-File Detective...")

    parser = argparse.ArgumentParser(description="Twin-File-Detective: A tool for finding and deleting copies of files")
    parser.add_argument("-d", "--display", action="store_true", help="Displays all found duplicates")
    parser.add_argument("-a", "--all", action="store_true", help="Automatically deletes all found copies of files")
    parser.add_argument("-s", "--select", nargs="+", type=int, help="Selectively delete file duplicates")
    
    args = parser.parse_args()
    data_map = walk_dir()
    twins = find_duplicate(data_map)
    all_candidates = grab_duplicates(twins)
   

    if not twins:
        print("no duplicates were found")
        return
    
    if args.display:
        display_duplicates(twins)

    if args.all:
        delete_duplicates(all_candidates)
        print(f"Sucesfuly deleted {len(all_candidates)}!")

    if args.select:
        selected_candidates = select_duplicates(all_candidates, args.select)
        delete_duplicates(selected_candidates)



if __name__ == "__main__":
    main()
