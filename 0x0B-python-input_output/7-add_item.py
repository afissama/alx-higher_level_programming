#!/usr/bin/python3
"""
This script adds all arguments to a Python list
and save them to a file
"""

if __name__ == "__main__":
    import sys
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    my_list = []

    if (len(sys.argv) > 1):
        my_list = sys.argv[1:]
    save_to_json_file(my_list, "add_item.json")
