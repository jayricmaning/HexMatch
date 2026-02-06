import os
from functions import walk_dir, find_duplicate, display_duplicates

def main():
    print("🚀 Starting Twin-File Detective...")
    data_map = walk_dir()
    twins = find_duplicate(data_map)

    if twins:
        print(f"\n Done! Found {len(twins)} sets of duplicate files!")
        display_duplicates(twins)
    if twins is None:
        print(f"\n No duplicates found")




if __name__ == "__main__":
    main()
