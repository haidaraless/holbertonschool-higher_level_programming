#!/usr/bin/python3

"""
A script that adds all arguments to Python list
and save them into a file
"""


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
file_name = "add_item.json"

"""loads from file then save to json file"""
try:
    item_list = load_from_json_file(file_name)
except FileNotFoundError:
    item_list = []

item_list.extend(sys.argv[1:])
save_to_json_file(item_list, file_name)
