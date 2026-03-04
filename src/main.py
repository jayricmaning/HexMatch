#!/usr/bin/env python3

import argparse
from functions import (
    walk_dir,
    find_duplicate,
    display_duplicates,
    grab_duplicates,
    select_duplicates,
    trash_duplicates,
    delete_duplicates,
)


def main():
    print("Starting Twin-File Detective...")

    parser = argparse.ArgumentParser(
        description="Twin-File-Detective: A tool for finding and deleting copies of files"
    )
    parser.add_argument(
        "-sc", "--scan", action="store_true", help="Scans directory for all duplicates"
    )
    parser.add_argument(
        "-v", "--versbose", action="store_true", help="Display complete file paths"
    )

    selection_group = parser.add_mutually_exclusive_group()
    selection_group.add_argument(
        "-a", "--all", action="store_true", help="Select all duplicate files"
    )
    selection_group.add_argument(
        "-s", "--select", nargs="+", type=int, help="Manually select file duplicates"
    )

    action_group = parser.add_mutually_exclusive_group()
    action_group.add_argument(
        "-r", "--remove", action="store_true", help="Send files to trash"
    )
    action_group.add_argument(
        "-d", "--delete", action="store_true", help="Permanently delete files"
    )

    args = parser.parse_args()
    data_map = walk_dir()
    twins = find_duplicate(data_map)
    all_candidates = grab_duplicates(twins)

    if not twins:
        print("no duplicates were found")
        return

    if args.scan:
        display_duplicates(twins)

    if args.all:
        if args.remove:
            trash_duplicates(all_candidates)
            print(
                f"Successfully moved the following files to trash/recycle bin {len(all_candidates)}"
            )
        elif args.delete:
            delete_duplicates(all_candidates)
            print(f"Successfully deleted {len(all_candidates)}!")

    elif args.select:
        selected_candidates = select_duplicates(all_candidates, args.select)
        if args.remove:
            trash_duplicates(selected_candidates)
            print(
                f"Successfully moved the following files to trash/recycle bin {len(selected_candidates)}"
            )
        elif args.delete:
            delete_duplicates(selected_candidates)
            print(f"Successfully deleted {len(selected_candidates)}!")


if __name__ == "__main__":
    main()
