#!/usr/bin/python3
"""
This module use json to save object to file
"""

import json

def save_to_json_file(my_obj, filename):
    """ Function that saves my_obj to filename
    as json
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
