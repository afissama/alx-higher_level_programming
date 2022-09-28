#!/usr/bin/python3
"""
This module use json to save object to file
"""
import json


def load_from_json_file(filename):
    """
    This function creates an Object from JSON file
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
